#!/usr/bin/env python3
""" Module """
import asyncio
import random

async def async_generator():
    rand = 0
    
    for x in range(10):
        rand = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand