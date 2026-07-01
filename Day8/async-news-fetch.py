# async def fetch() awaits asyncio.sleep() to simulate network I/O without blocking. 
# asyncio.gather() runs all fetches concurrently in a single thread. 
# Total elapsed time equals max delay, not sum -- showing true concurrency without multiple threads. 
# This is the exact model used by FastAPI and 
# aiohttp to handle thousands of requests per second.
# Fetch from 3 sources concurrently using asyncio.gather(). 
# Total time should equal max delay, not the sum

import asyncio
import time


async def fetch(source: str, delay: float) -> dict:

    print(f"{source} started")

    # simulate network request
    await asyncio.sleep(delay)


    print(f"{source} finished")


    return {
        "source": source,
        "headlines": [
            f"{source} story 1",
            f"{source} story 2"
        ]
    }

async def main():

    start = time.time()

    results = await asyncio.gather(

        fetch("BBC", 1.5),

        fetch("Times", 2.0),

        fetch("Reuters", 1.2)

    )

    end = time.time()
    elapsed = end - start


    print(
        f"\nDone in {elapsed:.1f} seconds"
    )


    print("\nNews:")


    for news in results:

        print(news)




asyncio.run(main())