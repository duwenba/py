import re

import requests
import asyncio
import aiohttp
import aiofile

url = "https://pri-cdn-tx.xiaoeknow.com/appl2m4pcpu3553/private_index/16683963161fXZxj.m3u8?sign=0bc4eb71c0f48f1041c04e625af63d10&t=6391d9c9"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42",
}
data = {
    "app_id": "appl2m4pcpu3553"
}
name = "day2.m3u8"
erro = 0

def get_m3u8(url, name):
    resp = requests.get(url)
    with open(name, mode="wb") as f:
        f.write(resp.content)
        f.close()


async def download(url, output,n):
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.get(url) as resp:
            if  resp.status != 200:
                print("erro!!",n)
                return
            async with aiofile.async_open(output+".mp4", mode="wb") as f:
                await f.write(await resp.content.read())
                print("完成了一个")


def download2(url, output,n):
    with requests.get(url) as resp:
        if resp.content != 200:
            print("erro!!",n)
            return
        with open(output+".mp4", mode="wb") as f:
            f.write(resp.content)
            print("完成了一个")

async def download_m3u8(name, output):
    with open(name, mode="r", encoding="utf-8") as f:
        tasks = []
        n=0
        for line in f:
            if line.startswith("#"):
                continue
            url = f"https://encrypt-k-vod.xet.tech/529d8d60vodtransbj1252524126/a7bf7e94243791575436244427/drm/{line}"
            download2(url, f"{output}\\{line}", n)
            # tasks.append(asyncio.create_task(download(url, f"{output}\\{line}",n)))
            # n += 1
            # await asyncio.wait(tasks)


if __name__ == "__main__":
    # print()
    get_m3u8(url, name)
    asyncio.run(download_m3u8(name, "output"))
