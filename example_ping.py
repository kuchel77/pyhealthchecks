"""Example usage of pyaftership."""
import asyncio
import aiohttp
from pyhealthchecks import pyhealthchecks


async def example():
    """Get pending packages."""
    async with aiohttp.ClientSession() as session:
        health_check = pyhealthchecks.HealthChecks(
            LOOP,
            ping_url="https://hc-ping.com/cf85d4b2-f859-40e9-b7ec-52810b09e35d",
            session=session
        )

        result = await health_check.update_connection()
        print("Result %s", result)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
