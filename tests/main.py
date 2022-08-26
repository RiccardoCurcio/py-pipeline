import unittest
import asyncio
from pypipelines import pipeline, asyncpipeline, eventlooppipeline, asynceventlooppipeline


def one(input):
    return input + " ONE "


def two(input):
    return input + " TWO "


def three(input, *args):
    return input + " THREE " + "".join(args)


def four(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"


async def asyncone(input):
    return input + " ONE "


async def asynctwo(input):
    return input + " TWO "


async def asyncthree(input, *args):
    return input + " THREE " + "".join(args)


async def asyncfour(input, a, b, c):
    return input + " FOUR " + f"{a}" + f"{b}" + f"{c}"


class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        result = pipeline(
            input="TEST ",
            pipe=[
                one,
                two
            ]
        )
        self.assertEqual(result, "TEST  ONE  TWO ")

    def test_pipeline_with_args(self):
        result = pipeline(
            input="TEST ",
            pipe=[
                one,
                two,
                [three, " DD ", " EE ", " FF "],
                [four, " XX ", " YY ", " ZZ "]
            ]
        )
        self.assertEqual(
            result, "TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ ")

    def test_asyncpipeline(self):
        result = asyncio.run(
            asyncpipeline(
                input="TEST ",
                pipe=[
                    asyncone,
                    asynctwo
                ]
            )
        )
        self.assertEqual(result, "TEST  ONE  TWO ")

    def test_asyncpipeline_with_args(self):
        result = asyncio.run(
            asyncpipeline(
                input="TEST ",
                pipe=[
                    asyncone,
                    asynctwo,
                    [asyncthree, " DD ", " EE ", " FF "],
                    [asyncfour, " XX ", " YY ", " ZZ "]
                ]
            )
        )
        self.assertEqual(
            result, "TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ ")

    def test_eventlooppipeline(self):
        def callback(input):
            self.assertEqual(input, "TEST  ONE  TWO ")

        eventlooppipeline(
            input="TEST ",
            pipe=[
                one,
                two
            ],
            callback=callback
        )

    def test_eventlooppipeline_with_args(self):
        def callback(input):
            self.assertEqual(input, "TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ ")

        eventlooppipeline(
            input="TEST ",
            pipe=[
                one,
                two,
                [three, " DD ", " EE ", " FF "],
                [four, " XX ", " YY ", " ZZ "]
            ],
            callback=callback
        )

    def test_asynceventlooppipeline(self):
        def callback(input):
            self.assertEqual(
                input, "TEST  ONE  TWO ")

        asynceventlooppipeline(
            input="TEST ",
            pipe=[
                asyncone,
                asynctwo
            ],
            callback=callback
        )

    def test_asynceventlooppipeline_with_args(self):
        def callback(input):
            self.assertEqual(
                input, "TEST  ONE  TWO  THREE  DD  EE  FF  FOUR  XX  YY  ZZ ")

        asynceventlooppipeline(
            input="TEST ",
            pipe=[
                asyncone,
                asynctwo,
                [asyncthree, " DD ", " EE ", " FF "],
                [asyncfour, " XX ", " YY ", " ZZ "]
            ],
            callback=callback
        )
        


if __name__ == '__main__':
    unittest.main()
