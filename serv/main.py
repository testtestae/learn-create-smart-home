import asyncio

from packages.MQTT_PACKAGE.MQTT_PACKAGE import MQTT_PACKAGE
from packages.TELEGRAM_PACKAGE.TELEGRAM_PACKAGE import telegram_start

stack = []


async def main():
    await asyncio.create_task(MQTT_PACKAGE())
    await asyncio.create_task(telegram_start())


if __name__ == '__main__':
    asyncio.run(main())
