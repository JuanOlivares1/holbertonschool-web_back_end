#!/usr/bin/env python3
""" Module """
import asyncio
from random import uniform


async def wait_random(max_delay: int=10) -> float:
    """ Awaits for a random amount of time (10s default) """
    rand = uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
