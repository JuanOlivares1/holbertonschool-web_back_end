#!/usr/bin/env python3
""" Module """
import asyncio, random


async def wait_random(max_delay = 10):
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
