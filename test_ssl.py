import asyncio
import aiohttp
import ssl

original_init = aiohttp.TCPConnector.__init__
def new_init(self, *args, **kwargs):
    kwargs['ssl'] = False
    original_init(self, *args, **kwargs)

aiohttp.TCPConnector.__init__ = new_init

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://generativelanguage.googleapis.com') as response:
            print(response.status)

asyncio.run(main())
