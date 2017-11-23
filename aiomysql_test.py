# !/usr/bin/env python
#-*-coding:utf-8-*-
#导入模块

#普通连接
import asyncio
import aiomysql_test

loop = asyncio.get_event_loop()

async  def test_example():
    conn = await aiomysql_test.connect(host='127.0.0.1', port=3306,
                                       user='root', password='', db='mysql',
                                       loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())

# #异步的连接池 pool
# import asyncio
# import aiomysql
#
#
# async def test_example(loop):
#     pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
#                                       user='root', password='',
#                                       db='mysql', loop=loop)
#     async with pool.acquire() as conn:
#         async with conn.cursor() as cur:
#             await cur.execute("SELECT 42;")
#             print(cur.description)
#             (r,) = await cur.fetchone()
#             assert r == 42
#     pool.close()
#     await pool.wait_closed()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_example(loop))
#
# #对象关系映射SQLAlchemy - Object Relationship Mapping 可以随意定义表结构，轻松调用查询、插入等操作方法
#
# import asyncio
# import sqlalchemy as sa
#
# from aiomysql.sa import create_engine
#
#
# metadata = sa.MetaData()
#
# tbl = sa.Table('tbl', metadata,
#                sa.Column('id', sa.Integer, primary_key=True),
#                sa.Column('val', sa.String(255)))
#
#
# async def go(loop):
#     engine = await create_engine(user='root', db='test_pymysql',
#                                  host='127.0.0.1', password='', loop=loop)
#     async with engine.acquire() as conn:
#         await conn.execute(tbl.insert().values(val='abc'))
#         await conn.execute(tbl.insert().values(val='xyz'))
#
#         async for row in conn.execute(tbl.select()):
#             print(row.id, row.val)
#
#     engine.close()
#     await engine.wait_closed()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(go(loop))
