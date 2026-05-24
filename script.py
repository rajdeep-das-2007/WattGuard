import os
import asyncio
from pprint import pprint

from dotenv import load_dotenv
from kasa import Discover, Device 
from kasa.credentials import Credentials
from kasa.deviceconfig import DeviceConfig, DeviceConnectionParameters, DeviceFamily, DeviceEncryptionType
load_dotenv()

IP = os.environ["TAPO_IP"]
EMAIL = os.environ["TAPO_EMAIL"]
PASSWORD = os.environ["TAPO_PASSWORD"]

creds = Credentials(username=EMAIL, password=PASSWORD);

Plug_config = DeviceConfig(
    host=IP,
    port_override=80,
    credentials=creds,
    connection_type=DeviceConnectionParameters(
        device_family=DeviceFamily.SmartTapoPlug,
        encryption_type=DeviceEncryptionType.Klap
    )
)


async def main():
    # plug = await Discover.discover_single(host=IP, username=EMAIL, password=PASSWORD)
    # if plug is not None:    
    #    
    print("Executing")
    plug = await Device.connect(config=Plug_config)
    if plug is not None:
        await plug.turn_off()
        await plug.disconnect()



if __name__ == "__main__":
    asyncio.run(main())