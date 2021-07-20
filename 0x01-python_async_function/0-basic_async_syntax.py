#!/usr/bin/env python3
""" Module """
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """ Awaits for a random amount of time (10s default) """
    rand = uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
