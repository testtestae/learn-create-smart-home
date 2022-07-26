import asyncio
from modules.TELEGRAM_module.TELEGRAM_module import TELEGRAM_module
# from modules.MQTT_module.MQTT_module import MQTT_module

DEVICE_LIST = [
    {
        "device": "lamp1",
        "state": None
    }
]


MQTT_TASK_STACK = []

# MQTT_TASK_STACK = [
#   {
#           room: "room1"
#          subroom: "subroom2"
#       device: "lamp1"
#           or
#           topic: "room1/subroom2/lamp1"
#       setState: True/False
#   },
#   {
#       room: "room1"
#       subroom: "subroom3"
#       device: "lamp1"
#       or
#       topic: "room1/subroom3/lamp1"
#       setState: True/False
#   }
# ]


# SPACE_STRUCTURE = [
#     {
#         "_id" : "randNum1"
#         "spaceName": "room",
#         "devices": [],
#         "subRooms": [
#             {
#                 "spaceName": "subroom",
#                 "devices": [
#                     "deviceSerialNumber1",
#                     "deviceSerialNumber2"
#                 ],
#                 "subRooms": []
#             }
#         ]
#     }
# ]

# USER_LIST = [
#     {
#         "name": "Ахмед",
#         "access_SPACE_STRUCTURE": [
#             "randNum1"
#         ],
#         "telegram_id": []
#     }
# ]

async def main():
    await asyncio.create_task(TELEGRAM_module(DEVICE_LIST))
    # await asyncio.create_task(MQTT_module(MQTT_TASK_STACK))


if __name__ == "__main__":
    asyncio.run(main())
