#!/usr/bin/env python3
""" Module """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Task excecution n times """
    delays = []
    s_delays = []

    for x in range(n):
        task = await task_wait_random(max_delay)
        delays.append(task)

    while delays:
        minimum = delays[0]
        for x in delays:
            if x < minimum:
                minimum = x
        s_delays.append(minimum)
        delays.remove(minimum)

    return s_delays
