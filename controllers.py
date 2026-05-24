import os
import asyncio
from pprint import pprint
from typing import cast

from dotenv import load_dotenv
from kasa import Device 
from kasa.credentials import Credentials
from kasa.deviceconfig import DeviceConfig, DeviceConnectionParameters, DeviceFamily, DeviceEncryptionType
from kasa.module import Module
load_dotenv()


IP = os.environ["TAPO_IP"]
EMAIL = os.environ["TAPO_EMAIL"]
PASSWORD = os.environ["TAPO_PASSWORD"]
PORT = os.environ["TAPO_PORT"]

creds = Credentials(username=EMAIL, password=PASSWORD)

Plug_config = DeviceConfig(
    host=IP,
    port_override=int(PORT),
    credentials=creds,
    connection_type=DeviceConnectionParameters(
        device_family=DeviceFamily.SmartTapoPlug,
        encryption_type=DeviceEncryptionType.Klap
    )
)

plug = None

async def connect_plug():
    global plug
    if plug is None:
        plug = await Device.connect(config=Plug_config)
    return plug

async def disconnect_plug():
    global plug
    if plug is not None:
        await plug.disconnect()
        plug = None

async def turn_on():
    plug = await connect_plug()
    await plug.turn_on()
    print("Plug ON")

async def turn_off():
    plug = await connect_plug()
    await plug.turn_off()
    print("Plug OFF")