# py-pipeline
pipeline in python3

## Install
```shell
$ pip3 install py-pipeline
```

## Clone rthi repository and local install
```shell
$ pip3 install --upgrade .
```
## Run test
```shell
$ python3 -m unittest -v tests/main.py 
```

## Examples

### Simple pipeline
create a pipeline with functions

```py
def pipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]) -> Any:
```

Example
```py
from pypipeline import pipeline

def one(input):
    return input + " ONE "


def two(input):
    return input + " TWO "


def three(input, *args):
    return input + " THREE " + "".join(args)


def four(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"


if __name__ == "__main__":
    result = pipeline(
        input="TEST ",
        pipe=[
            one,
            two,
            [three, " DD ", " EE ", " FF "],
            [four, " XX ", " YY ", " ZZ "]
        ]
    )
    print(result)
```

```shell
$ python3 main.py 
TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ 
```

### Simple async pipeline

```py
async def asyncpipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[]) -> Any:
```

Example

```py
from pypipeline import asyncpipeline
import asyncio


async def asyncone(input):
    return input + " ONE "


async def asynctwo(input):
    return input + " TWO "


async def asyncthree(input, *args):
    return input + " THREE " + "".join(args)


async def asyncfour(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"


if __name__ == "__main__":
    result = asyncio.run(asyncpipeline(
            input="TEST ",
            pipe=[
                asyncone,
                asynctwo,
                [asyncthree, " DD ", " EE ", " FF "],
                [asyncfour, " XX ", " YY ", " ZZ "]
            ]
        ))
    print(result)
```

```shell
$ python3 main.py 
TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ 
```


### Simple event loop pipeline

```py
def eventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None) -> None:
```

Example

```py
from pypipeline import eventlooppipeline
from time import sleep


def one(input):
    return input + " ONE "


def two(input):
    return input + " TWO "


def three(input, *args):
    return input + " THREE " + "".join(args)


def four(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"


def twoSleep(input):
    sleep(2)
    return input + " BB (sleep 2) "


def callback(input):
    print("CALLBACK", input)


if __name__ == "__main__":
    eventlooppipeline(
        input="ciao",
        pipe=[
            one,
            two,
            twoSleep,
            [three, " DD ", " EE ", " FF "],
            [four, " XX ", " YY ", " ZZ "]
        ],
        callback=callback)
    print("Event loop running...")
```

```shell
$ python3 main.py 
Event loop running...
CALLBACK ciao ONE  TWO  BB (sleep 2)  THREE  DD  EE  FF  FOUR  XX  YY  ZZ 
```

### Simple event loop async pipeline


```py
def asynceventlooppipeline(input:Any=None, pipe:Union[List[Callable], List[Union[List, Callable]]]=[], callback:Union[Callable, None] = None) -> None:
```

Example

```py
from pypipeline import asynceventlooppipeline
from time import sleep

async def asyncone(input):
    return input + " ONE "


async def asynctwo(input):
    return input + " TWO "


async def asyncthree(input, *args):
    return input + " THREE " + "".join(args)


async def asyncfour(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"

async def asynctwoSleep(input):
    sleep(2)
    return input + " BB (async sleep 1) "

def callback(input):
    print("CALLBACK", input)

if __name__ == "__main__":
    asynceventlooppipeline(
            input="TEST ",
            pipe=[
                asyncone,
                asynctwo,
                asynctwoSleep,
                [asyncthree, " DD ", " EE ", " FF "],
                [asyncfour, " XX ", " YY ", " ZZ "]
            ],
            callback=callback
        )
    print("Event loop running...")
```

```shell
$ python3 main.py 
Event loop running...
CALLBACK TEST  ONE  TWO  BB (async sleep 1)  THREE  DD  EE  FF  FOUR  XX  YY  ZZ
```