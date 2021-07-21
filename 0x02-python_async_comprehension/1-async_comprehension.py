#!/usr/bin/env python3
""" Module """
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ async for """    
    return result = [i async for i in async_generator()]

