import asyncio
from aiohttp import web

"""Función para indicar que debe de levantar el index.html """
async def handle(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')
async def init_app():
    app = web.Application()
    app.add_routes([
    web.get('/', handle)
    ])
    return app


"""Función que se llama desde el script principal main.py para correr el servidor junto al Bot"""
async def run_server():
    app = await init_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

"""Corremos el Servidor"""
if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop_policy().get_event_loop()
    loop.create_task(run_server())
    print('*Server Iniciado')
    loop.run_forever()
