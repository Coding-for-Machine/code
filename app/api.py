import asyncio
import aiohttp




# get data using post_id
async def get_data_id(url, post_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}/{post_id}") as response:
            if response.status==200:
                return response.json()
            else:
                return response.status

# post data
async def post_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status==201:
                return await response.json()
            else:
                return await response.status

# put data

async def update_data(url, post_id, data):
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{url}/{post_id}", json=data) as response:
            if response.status==200:
                return await response.json()
            else:
                return await response.status

# delete data
async def detete_data(url, post_id):
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{url}/{post_id}") as response:
            if response.status==200:
                return await response.json()
            else:
                return await response.status
            

