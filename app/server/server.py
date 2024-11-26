import asyncio
import aiofiles
from api import get_data

async def wrate_data(data):
    async with aiofiles.open('data.json', 'w') as f:
        await f.write(data)


url = "https://jsonplaceholder.typicode.com/posts"
print(url)
data = asyncio.run(get_data(url))
print(data)
asyncio.run(wrate_data(data))