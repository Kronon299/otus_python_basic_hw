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
        db_url='postgres://odoo:odoo@172.58.0.4:5432/database_1',
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

    # logger.info("Got result for {}, result {}", source.name, result)
    return source.name, result


async def write_data():
    await init()
    done, _ = await asyncio.wait(
        [get_data(s) for s in SOURCES],
        timeout=5,
        return_when=asyncio.ALL_COMPLETED,
    )
    for s in done:
        res = s.result()
        if res[0] == 'users':
            await user_writer(res[1])
        elif res[0] == 'posts':
            await post_writer(res[1])
        elif res[0] == 'comments':
            await comment_writer(res[1])


async def user_writer(data: list):
    for user in data:
        await models.User.create(
            id=user['id'],
            name=user['name'],
            username=user['username'],
            email=user['email'],
        )


async def post_writer(data: list):
    for post in data:
        await models.Post.create(
            id=post['id'],
            title=post['title'],
            body=post['body'],
            user_id_id=post['userId'],
        )


async def comment_writer(data: list):
    for comment in data:
        await models.Comment.create(
            id=comment['id'],
            name=comment['name'],
            email=comment['email'],
            body=comment['body'],
            post_id_id=comment['postId'],
        )


if __name__ == '__main__':
    run_async(init())
    run_async(write_data())

