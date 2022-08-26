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
from typing import Any, Union, List, Callable, Iterator
from pypipelines.src.iterators import iterate, asynciterate


def pipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]) -> Any:
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].

    Returns:
        Any: _description_
    """
    return iterate(listOfCallable=iter(pipe), input=input)

async def asyncpipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]) -> Any:
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].

    Returns:
        Any: _description_
    """
    return await asynciterate(listOfCallable=iter(pipe), input=input)

def eventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None) -> None:
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].
        callback (Union[Callable, None], optional): _description_. Defaults to None.
    """
    def __run(loop: AbstractEventLoop, listOfCallable: Iterator, input: Any, callback:Union[Callable, None] = None):
        """_summary_

        Args:
            loop (AbstractEventLoop): _description_
            listOfCallable (Iterator): _description_
            input (Any): _description_
            callback (Union[Callable, None], optional): _description_. Defaults to None.
        """
        asyncio.set_event_loop(loop)
        callback(iterate(listOfCallable=listOfCallable, input=input)) if callback is not None else None
        loop.close()

    loop:AbstractEventLoop = asyncio.new_event_loop()
    thread:Thread = Thread(target=__run, args=(loop, iter(pipe), input, callback))
    thread.start()


def asynceventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None) -> None:
    """_summary_

    Args:
        input (Any, optional): _description_. Defaults to None.
        pipe (Union[List[Callable], List[Union[List, Callable]]], optional): _description_. Defaults to [].
        callback (Union[Callable, None], optional): _description_. Defaults to None.
    """
    def __run(loop: AbstractEventLoop, listOfCallable: Iterator, input: Any, callback:Union[Callable, None] = None):
        """_summary_

        Args:
            loop (AbstractEventLoop): _description_
            listOfCallable (Iterator): _description_
            input (Any): _description_
            callback (Union[Callable, None], optional): _description_. Defaults to None.
        """
        asyncio.set_event_loop(loop)
        callback(asyncio.run(asynciterate(listOfCallable=listOfCallable, input=input))) if callback is not None else None
        loop.close()

    loop: AbstractEventLoop = asyncio.new_event_loop()
    thread:Thread = Thread(target=__run, args=(loop, iter(pipe), input, callback))
    thread.start()
