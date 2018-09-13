# async_programming.py
# tasks waiting for IO, for external tasks, files, db, response 70%
# js: press a button, no freeze (because of async) -> nginx, nodeJS (APIs)
#   Principal thread -> Task Task tasks (can respond to the user)
#   Secondary thread getting tasks
# event-driven architecture, managed by the programming language entirely

import asyncio

# 1. Courutines
#   queue of tasks (secondary `loop` get and process),
#       while main keep getting tasks
#   cooperative multitasking
# 2. Futures (promises JS, callback in C), you owe me this response
# 3. Tasks

# The tasks, experiment afterwards with some sleeping time!!
async def say_hello():
    print("Hello World")

async def dummy():
    print("Whaaaatsup")

async def perform_task():
    print('perf task, waiting for result')
    result1 = await subtask1()
    print('waiting for result2')
    result2 = await subtask2(result1)
    return(result1, result2)

async def subtask1():
    print("perform subtask 1")
    return "result1"

async def subtask2(result1):
    print("perform subtask 2")
    return "result2"


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # can have multiple asyncs executed in a loop
    loop.run_until_complete(say_hello())
    loop.run_until_complete(dummy())
    loop.run_until_complete(perform_task())
    loop.close()

# Treading, Async: IOBound tasks
#   Threading: Under 1000 is faster, over slower (stack and context switch)
#       Django with threadinv vs iohttp wrk -c 500 -t   "nginx > apache"
#   Async: Over 1000
