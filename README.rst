txEffect
========

.. image:: https://travis-ci.org/python-effect/txeffect.svg?branch=master
    :target: https://travis-ci.org/python-effect/txeffect
.. image:: https://img.shields.io/pypi/v/txeffect.svg
    :target: https://pypi.python.org/pypi/txeffect

txEffect is a small library for integrating Twisted and Effect, mostly
around Deferred<->Effect interoperation. Documentation is available at
https://txeffect.readthedocs.org/

`Effect`_ is a library for helping you write purely functional code by
isolating the effects (that is, IO or state manipulation) in your code.
Documentation is available at https://effect.readthedocs.org/.

.. _`Effect`: https://github.com/python-effect/effect


Examples
========

Perform an Effect to get a Deferred with `txeffect.perform`_.

.. _`txeffect.perform`: http://txeffect.readthedocs.org/en/latest/api/txeffect.html#txeffect.perform

.. code:: python

    from txeffect import perform
    d = perform(my_dispatcher, some_effect)
    d.addCallback(log.msg)

Implement a performer for an intent that returns a Deferred with
`txeffect.deferred_performer`_.

.. _`txeffect.deferred_performer`: http://txeffect.readthedocs.org/en/latest/api/txeffect.html#txeffect.deferred_performer

.. code:: python

    from twisted.internet.defer import succeed
    from txeffect import deferred_performer

    @deferred_performer
    def perform_foo(dispatcher, intent):
        return succeed('hello, world')

Perform standard `Delay`_ and `parallel`_ effects using asynchronous
implementations with `txeffect.make_twisted_dispatcher`_.

.. _`Delay`: http://effect.readthedocs.org/en/latest/api/effect.html#effect.Delay
.. _`parallel`: http://effect.readthedocs.org/en/latest/api/effect.html#effect.parallel
.. _`txeffect.make_twisted_dispatcher`: http://txeffect.readthedocs.org/en/latest/api/txeffect.html#txeffect.make_twisted_dispatcher

.. code:: python

    from twisted.internet import reactor
    from txeffect import make_twisted_dispatcher

    dispatcher = make_twisted_dispatcher(reactor)
    p_effs = parallel([Effect(Delay(5), Effect(Delay(3), Effect(Delay(1))))])
    perform(dispatcher, p_effs).addCallback(
        lambda: print("5 seconds have passed!"))


Working examples can be found at the `effect-examples`_ GitHub repo.

.. _`effect-examples`: https://github.com/python-effect/effect-examples


Thanks
======

Thanks to Rackspace for allowing me to work on this project, and having an
*excellent* `open source employee contribution policy`_

.. _`open source employee contribution policy`: https://www.rackspace.com/blog/rackspaces-policy-on-contributing-to-open-source/


IRC
===

There is a ``#python-effect`` IRC channel on irc.freenode.net.

License
=======

txEffect is licensed under the MIT license:

Copyright (C) 2014 Christopher Armstrong

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
