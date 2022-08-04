# Copyright (c) 2020 <Riccardo Curcio>
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
from asyncio import AbstractEventLoop
from threading import Thread
from typing import Any, Union, List, Callable
from pypipeline.src.iterators import iterate, asynciterate


def pipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]):
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    return iterate(iter(pipe), input)

def asyncpipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]):
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].

    Returns:
        _type_: _description_
    """
    return asyncio.run(asynciterate(iter(pipe), input))

def eventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None):
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].
        callback (Union[Callable, None], optional): _description_. Defaults to None.
    """
    def __run(loop: AbstractEventLoop, listOfCallable: Any, input: Any, callback:Union[Callable, None] = None):
        """_summary_

        Args:
            loop (_type_): _description_
            listOfCallable (_type_): _description_
            input (_type_): _description_
            callback (function): _description_
        """
        asyncio.set_event_loop(loop)
        callback(iterate(listOfCallable, input)) if callback is not None else None
        loop.close()

    loop = asyncio.new_event_loop()
    t = Thread(target=__run, args=(loop, iter(pipe), input, callback))
    t.start()


def asynceventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None):
    def __run(loop, listOfCallable, input, callback):
        asyncio.set_event_loop(loop)
        callback(asyncio.run(asynciterate(listOfCallable, input))) if callback is not None else None
        loop.close()
    loop = asyncio.new_event_loop()
    t = Thread(target=__run, args=(loop, iter(pipe), input, callback))
    t.start()
