# import asyncio
# async def say_greeting():

#     print('hello')
#     await asyncio.sleep(1)
#     print('world')

# def main():
#     say_greeting()
#     print('hello everyone')


# asyncio.run(main())

# import asyncio

# async def foo():
#     print("Foo started")
#     await asyncio.sleep(1)
#     print("Foo finished")

# async def bar():
#     print("Bar started")
#     await asyncio.sleep(2)
#     print("Bar finished")

# async def main():
#     tasks = [foo(), bar()]
#     await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())

# async def call_spotify_api():
#     print("spotify call started")
#     await asyncio.sleep(1)
#     print("spotify call finished")

import asyncio
import time
async def call_foursquare_api():
    print("foursquare call started")
    await asyncio.sleep(2)
    print("foursquare call finished")

start_time = time.time()
async def main():
    await asyncio.gather(call_foursquare_api(), call_foursquare_api(), call_foursquare_api(), call_foursquare_api())
    
if __name__ == "__main__":
    asyncio.run(main())
    end_time = time.time()
    delta = end_time - start_time
    print(delta)
