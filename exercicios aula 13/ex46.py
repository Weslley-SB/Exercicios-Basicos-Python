#contagem regressiva

import asyncio

async def contagem():
    for i in range(10, -1, -1):
        print(i)
        await asyncio.sleep(1)
        if i == 0:
            print("Boom")

asyncio.run(contagem())