# Ignore this file: This file is for Initial testing. 

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

creds = Credentials(username=EMAIL, password=PASSWORD)

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
        
        plug_energy = plug.modules[Module.Energy]
        try:
            while True:
                await plug.update()
                power = plug_energy.current_consumption
                current = plug_energy.current
                voltage = plug_energy.voltage

                YELLOW = "\033[93m"
                RESET = "\033[0m"

                print(
                    f"\r"
                    f"Power: {YELLOW}{power:.2f} W{RESET} | "
                    f"Voltage: {YELLOW}{voltage:.1f} V{RESET} | "
                    f"Current: {YELLOW}{current:.3f} A{RESET}",
                    end=""
                )

                await asyncio.sleep(3)

        except (KeyboardInterrupt, asyncio.CancelledError):
            print("\nExecution Stopped")
            await plug.disconnect()

if __name__ == "__main__":
    asyncio.run(main())