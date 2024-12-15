import aiofiles
import aiodocker
import io

async def create_image(image_name: str):
    client = aiodocker.Docker()
    containers = await client.containers.run(
        image_name,
        detach=True,
        ttp=True,
        restart_poling={"name": "always"}
    )
    return containers

async def file_cannacts(container, file_path, container_path='/data'):
    async with aiofiles.open(file_path, 'rb') as f:
        file_data = io.BytesIO(await f.read())
        await container.put_archive(container_path, file_data)
        print(f"{file_path} file uzatildi {container_path} cantenerga")

async def code_run_in(contaner, language, fiel_name):
    commands = {
        "cpp": f"g++ /data/{fiel_name}",
        "python": f"python /data/{fiel_name}",
        "go": f"go run /data/{fiel_name}",
        "java": f"java /data/{fiel_name}",
        "javascript": f"node /data/{fiel_name}",
    }
    if language not in commands:
        return {"error": "til mavjud emas"}
    result = contaner.exec_run(commands[language], stdout=True, stderr=True)
    return {'result': result.output.decode(), "error": result.autput}

    
