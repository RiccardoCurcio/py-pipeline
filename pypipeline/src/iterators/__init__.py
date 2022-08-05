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

from typing import Callable, Iterator, Any
from pypipeline.src.exceptions import PipeLineException

def iterate(listOfCallable: Iterator, input: Any) -> Any:
    """_summary_

    Args:
        listOfCallable (Iterator): _description_
        input (Any): _description_

    Raises:
        PipeLineException: _description_

    Returns:
        Any: _description_
    """
    call = next(listOfCallable, None)
    if isinstance(call, Callable):
        return iterate(listOfCallable, call(input))
    elif isinstance(call, list) and isinstance(call[0], Callable):
        return iterate(listOfCallable, call[0](input, *call[1:]))
    elif call is None:
        return input
    else:
        raise PipeLineException("Not valid pipeline")

async def asynciterate(listOfCallable: Iterator, input: Any) -> Any:
    """_summary_

    Args:
        listOfCallable (Iterator): _description_
        input (Any): _description_

    Raises:
        PipeLineException: _description_

    Returns:
        Any: _description_
    """
    call = next(listOfCallable, None)
    if isinstance(call, Callable):
        return await asynciterate(listOfCallable, await call(input))
    elif isinstance(call, list) and isinstance(call[0], Callable):
        return await asynciterate(listOfCallable, await call[0](input, *call[1:]))
    elif call is None:
        return input
    else:
        raise PipeLineException("Not valid pipeline")
