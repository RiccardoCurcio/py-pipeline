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

from typing import Any, Union, List, Callable
from pypipeline.src.exceptions import PipeLineException

def pipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]):
    # send_loop = asyncio.new_event_loop()
    # t = Thread(target=iterate, args=(send_loop, self.__event, self.__eventMapping, data))
    # t.start()
    return iterate(iter(pipe), input)

def iterate(listOfCallable, input):
    # asyncio.set_event_loop(loop)
    call = next(listOfCallable, None)
    if isinstance(call, Callable):
        return iterate(listOfCallable, call(input))
    elif isinstance(call, list) and isinstance(call[0], Callable):
        return iterate(listOfCallable, call[0](input, *call[1:]))
    elif call is None:
        # loop.close()
        return input
    else:
        # loop.close()
        raise PipeLineException("Not valid pipeline")