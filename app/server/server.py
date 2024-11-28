import asyncio
import aiohttp
import aiofiles
import json
# get
from api import get_data

# async def get_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             data = await response.json()
#             print("Kelgan ma'lumot:", data)  # Tekshirish uchun
#             return data

async def write_data(data):
    async with aiofiles.open('data.json', mode='w') as f:
        await f.write(json.dumps(data, indent=4, ensure_ascii=False))

async def main():
    try:
        url = "https://jsonplaceholder.typicode.com/todos"
        data = await get_data(url)
        await write_data(data)
        print("Ma'lumot muvaffaqiyatli yozildi!")
    except Exception as e:
        print("Xatolik:", e)


# Asosiy funksiyani bajarish
asyncio.run(main())
