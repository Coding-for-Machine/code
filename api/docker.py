import aiofiles
import aiodocker
import io
import os

async def create_image(image_name: str):
    """Docker imidjni ishga tushirish"""
    client = aiodocker.Docker()
    try:
        container = await client.containers.run(
            config={
                "Image": image_name,
                "Tty": True,
            },
            name="code_runner",
            restart_policy={"Name": "always"},
            detach=True
        )
        print(f"Konteyner '{image_name}' muvaffaqiyatli ishga tushirildi.")
        return container
    except Exception as e:
        print(f"Xato: {e}")
        return None


async def file_connect(container, file_path, container_path='/data'):
    """Faylni konteynerga yuklash"""
    try:
        async with aiofiles.open(file_path, 'rb') as f:
            file_data = io.BytesIO(await f.read())
        await container.put_archive(container_path, file_data)
        print(f"'{file_path}' fayli '{container_path}' ga konteynerda uzatildi.")
    except Exception as e:
        print(f"Fayl uzatishda xatolik: {e}")


async def code_run_in(container, language, file_name):
    """Kodni konteyner ichida bajarish"""
    commands = {
        "cpp": f"g++ /data/{file_name} -o /data/output && /data/output",
        "python": f"python /data/{file_name}",
        "go": f"go run /data/{file_name}",
        "java": f"javac /data/{file_name} && java -cp /data {file_name.split('.')[0]}",
        "javascript": f"node /data/{file_name}",
    }

    if language not in commands:
        return {"error": "Qo'llab-quvvatlanmaydigan dasturlash tili."}

    try:
        exec_instance = await container.exec_run(
            cmd=commands[language],
            stdout=True,
            stderr=True
        )
        result = await exec_instance.read_out()
        error = await exec_instance.read_err()

        return {
            "result": result.decode() if result else None,
            "error": error.decode() if error else None
        }
    except Exception as e:
        return {"error": f"Xatolik: {e}"}


async def logs(container):
    """Konteynerning loglarini o'qish"""
    try:
        log_output = await container.log(stdout=True, stderr=True)
        print("Konteyner loglari:")
        for line in log_output:
            print(line)
        return log_output
    except Exception as e:
        print(f"Loglarni o'qishda xatolik: {e}")
        return None


async def status_check(container):
    """Konteyner holatini tekshirish"""
    try:
        container_info = await container.show()
        status = container_info.get("State", {}).get("Status", "")
        if status != "running":
            print("Konteyner ishlamayapti. Qayta ishga tushirilmoqda...")
            await container.start()
            print("Konteyner qayta ishga tushirildi.")
        else:
            print("Konteyner ishlayapti.")
        return status
    except Exception as e:
        print(f"Konteyner holatini tekshirishda xatolik: {e}")
        return None


async def cleanup(container):
    """Ishdan keyin konteynerni o'chirish"""
    try:
        await container.delete(force=True)
        print("Konteyner muvaffaqiyatli o'chirildi.")
    except Exception as e:
        print(f"Konteynerni o'chirishda xatolik: {e}")


def validate_filename(file_name):
    """Fayl nomini validatsiya qilish"""
    if ".." in file_name or file_name.startswith("/") or "\\" in file_name:
        raise ValueError("Noto'g'ri fayl nomi.")
    if not file_name:
        raise ValueError("Fayl nomi bo'sh bo'lishi mumkin emas.")
    return file_name


async def main():
    # Konteyner yaratish
    image_name = "python:3.9"
    container = await create_image(image_name)
    if not container:
        return

    # Faylni konteynerga yuklash
    file_path = "test.py"
    try:
        validate_filename(file_path)
        await file_connect(container, file_path)
    except ValueError as e:
        print(f"Validatsiya xatoligi: {e}")
        return

    # Kodni konteynerda bajarish
    result = await code_run_in(container, "python", "test.py")
    print("Natija:", result)

    # Loglarni ko'rish
    await logs(container)

    # Konteynerni tozalash
    await cleanup(container)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
