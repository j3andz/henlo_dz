#!/usr/bin/env python3

import aiohttp
from aiohttp import web

async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

app = web.Application()
app.add_routes([web.get('/', index)])

if __name__ == '__main__':
    web.run_app(app)
