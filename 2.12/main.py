from tortoise import Tortoise, run_async
import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger

import models


async def init():
    # Here we create connection to PostgresQL database
    #  also specify the app name of "models"
    #  which contain models from "models"
    await Tortoise.init(
        db_url='postgres://odoo:odoo@172.57.0.4:5432/database_1',
        modules={'models': ['models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


@dataclass
class Source:
    name: str
    url: str


SOURCES = [
    Source("users", "https://jsonplaceholder.typicode.com/users"),
    Source("posts", "https://jsonplaceholder.typicode.com/posts"),
    Source("comments", "https://jsonplaceholder.typicode.com/comments"),
]


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def get_data(source: Source) -> tuple:
    """
    :param source:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch(session, source.url)

    logger.info("Got result for {}, result {}", source.name, result)
    return source.name, result


async def write_data():
    res = await asyncio.wait(
        [get_data(s) for s in SOURCES],
        timeout=5
    )
    # print(res)


if __name__ == '__main__':
    # run_async(init())
    run_async(write_data())
