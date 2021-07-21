#!/usr/bin/env python3
""" Module """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float]:
    """ async function """
    rand = 0

    for x in range(10):
        rand = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand
