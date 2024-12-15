import asyncio
import aiohttp
import aiofiles
import json
from decouple import config

# Backenddan JSON ma'lumot olish
async def get_code_json(url_backend):
    async with aiohttp.ClientSession() as session:
        async with session.get(url_backend) as response:
            if response.status == 200:
                return await response.json()  # Ma'lumotni qaytarish
            else:
                print(f"Error: {response.status}, {await response.text()}")
                return None

# JSON ma'lumotni faylga yozish
async def write_file_data(data):
    async with aiofiles.open("get_data_algoritm.json", "w") as f:
        await f.write(json.dumps(data, indent=4))  # JSON ma'lumotni yozish

# Asosiy sikl
async def main():
    url = config("BACEND_URL_ALGORITM",  default="http://localhost:8000/api/code", cast=str) #"http://localhost:8000/api/code"  # Backend URL
    while True:
        # Backenddan ma'lumot olish.
        data = await get_code_json(url)
        if data:  # Ma'lumot muvaffaqiyatli olinsa
            await write_file_data(data)  # Ma'lumotni faylga yozish
            print("Ma'lumot muvaffaqiyatli yozildi!")
        else:
            print("Ma'lumot olishda xatolik yuz berdi.")
        
        # 10 minut kutish
        await asyncio.sleep(600)

# Asosiy funksiyani ishga tushirish
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("---EXIT---")
