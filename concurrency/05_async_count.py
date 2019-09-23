# 05_async_count.py
import asyncio


async def count():
	"""It is a coroutine, because it can pass control to another coroutine for
	some time"""
	print("One")
	await asyncio.sleep(1)  # stands for non-blocking call
	print("Two")

# z() should be an awaitable object (coroutine, .__await__() object iterator)
# async def f(x):
# 	y = await z(x)
# 	return y

# async def g(x):
# 	yield x


async def main():
	"""Single event loop or coordinator, talking to each of the calls to count()
	When each task reaches the sleep, it yells up to the event loop and gives control
	back to it, saying I'm not going to be sleeping for 1 sec, go do something else.
	"""
	await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
	import time

	start_time = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - start_time

	print(f"{__file__} executed in {elapsed:0.2f} seconds")
