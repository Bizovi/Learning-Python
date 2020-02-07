# 06_async_rand.py
import asyncio
import random

# ANSI colors
colors = (
	"\033[0m",   # End of color
	"\033[36m",  # Cyan
	"\033[91m",  # Red
	"\033[35m",  # Magenta
)

async def make_random(idx: int, threshold: int = 6) -> int:
	"""
	Main coroutine which runs concurrently across 3 inputs
	:param idx: Index determining the color
	:param threshold: Threshold above which is successful
	:return: the successful random integer
	"""

	print(colors[idx + 1] + f"Initiated makerandom({idx}).")
	i = random.randint(0, 10)
	while i <= threshold:
		print(colors[idx + 1] + f"makerandom({idx}) == {i} too low; retrying.")
		await asyncio.sleep(idx + 1)
		i = random.randint(0, 10)
	# sneaky introduction of the end of color
	print(colors[idx + 1] + f"---> Finished: makerandom({idx}) == {i}" + colors[0])
	return i


async def main():
	"""Serves the chain of smaller coroutines together, and gather tasks (futures)
	by mapping the central coroutine across some iterable or pool (range(3)) / url set
	"""
	res = await asyncio.gather(*(make_random(i, 10-i-1) for i in range(3)))
	return res


if __name__ == "__main__":
	random.seed(444)
	r1, r2, r3 = asyncio.run(main())
	print()
	print(f"r1: {r1}, r2: {r2}, r3: {r3}")
