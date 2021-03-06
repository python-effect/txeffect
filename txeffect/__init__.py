# -*- test-case-name: effect.test_twisted -*-

"""
Twisted integration for the Effect library.

This is largely concerned with bridging the gap between Effects and Deferreds,
and also implementing Twisted-specific performers for standard Intents.

The most important functions here are :func:`perform`,
:func:`make_twisted_dispatcher`, and :func:`deferred_performer`.

Note that the core effect library does *not* depend on Twisted, but this module
does.
"""

from functools import partial

from twisted.internet.defer import Deferred
from twisted.internet.task import deferLater

from effect import Delay, ParallelEffects, perform as base_perform, TypeDispatcher
from effect.parallel_async import perform_parallel_async
from effect._utils import wraps  # whoah there


def deferred_to_box(d, box):
    """
    Make a Deferred pass its success or fail events on to the given box.
    """
    d.addCallbacks(box.succeed, lambda f: box.fail(f.value))


def make_twisted_dispatcher(reactor):
    """
    Create a dispatcher that knows how to perform certain built-in Intents
    with Twisted-specific implementations.
    """
    return TypeDispatcher(
        {
            ParallelEffects: perform_parallel_async,
            Delay: deferred_performer(partial(perform_delay, reactor)),
        }
    )


def deferred_performer(f):
    """
    A decorator for performers that return Deferreds.

    The function being decorated is expected to take a dispatcher and an intent
    (and not a box), and may return a Deferred. The wrapper function
    that this decorator returns will accept a dispatcher, an intent, and a box
    (conforming to the performer interface). The wrapper deals with
    putting the Deferred's result into the box.

    Example::

        @deferred_performer
        def perform_foo(dispatcher, foo):
            return do_side_effecting_deferred_operation(foo)
    """

    @wraps(f)
    def deferred_wrapper(*args, **kwargs):
        box = args[-1]
        pass_args = args[:-1]
        try:
            result = f(*pass_args, **kwargs)
        except Exception as e:
            box.fail(e)
        else:
            if isinstance(result, Deferred):
                deferred_to_box(result, box)
            else:
                box.succeed(result)

    return deferred_wrapper


def perform_delay(reactor, dispatcher, delay):
    """
    Perform a :obj:`effect.Delay` with Twisted's
        :func:`twisted.internet.task.deferLater`.
    """
    return deferLater(reactor, delay.delay, lambda: None)


def perform(dispatcher, effect):
    """
    Perform an effect, returning a Deferred that will fire with the effect's
    ultimate result.
    """
    d = Deferred()
    eff = effect.on(success=d.callback, error=lambda e: d.errback(e))
    base_perform(dispatcher, eff)
    return d
