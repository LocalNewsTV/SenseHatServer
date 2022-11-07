#!/usr/bin/python3
import asyncio, traceback
from senseHandler import ClientHandler
from IP import HOST, PORT

async def main():
    handler = ClientHandler()
    server = await asyncio.start_server(handler.handle_request, HOST, PORT)
    await server.serve_forever()
    traceback.print_exec
asyncio.run(main())
