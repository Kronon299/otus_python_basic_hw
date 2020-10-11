from time import time
from tortoise import Tortoise, run_async
import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession

import models


async def init():
    # Here we create connection to PostgresQL database
    #  also specify the app name of "models"
    #  which contain models from "models"
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
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
    return source.name, result


async def write_data_1():
    await init()
    done, _ = await asyncio.wait(
        [get_data(s) for s in SOURCES],
        timeout=5,
        return_when=asyncio.ALL_COMPLETED,
    )
    i = 0
    while i < 3:
        if i == 0:
            await writer_caller(done, name='users', writer_func=user_writer)
            i += 1
        if i == 1:
            await writer_caller(done, name='posts', writer_func=post_writer)
            i += 1
        if i == 2:
            await writer_caller(done, name='comments', writer_func=comment_writer)
            i += 1


async def writer_caller(done: set, name: str, writer_func):
    for s in done:
        if s.result()[0] == name:
            await writer_func(s.result()[1])


async def write_data():
    await init()
    done = []
    for s in SOURCES:
        data = await get_data(s)
        done.append(data)
    for res in done:
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
    start_time = time()
    run_async(init())
    run_async(write_data_1())
    print(f'total time: {time() - start_time}')

