#!usr/bin/env python3
# -*- coding: utf-8 -*-

__auther__ = "Zjl1204"

# web application

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,time,json
from datetime import datetime

from aiohttp import web

# 返回一个页面a
def index(request):
    return web.Response(body=b'<h1>Awsome</h1>')

#协程
@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_router('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'172.0.0.1',9000)
    logging.info('server started at http://172.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
