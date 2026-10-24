import os
import time
import sys

print("=========================================")
print("Listening for iPhone Bluetooth commands...")
print("Keep music playing in your AirPods!")
print("=========================================")


device_path = "/dev/rfcomm0"

if not os.path.exists(device_path):
    os.system("sudo rfcomm release 0 2>/dev/null")
    os.system("sudo rfcomm watch hci0 1 &")
    time.sleep(1)

while True:
    try:
     
        with open(device_path, "r") as ble_stream:
            for line in ble_stream:
                command = line.strip().lower()
                if not command:
                    continue

                print(f" Received from iPhone: {command}")

                if command == "volume up":
                    os.system("amixer set Master 10%+")
                    print("🔊 Turned volume UP 10%")

                elif command == "volume down":
                    os.system("amixer set Master 10%-")
                    print("🔉 Turned volume DOWN 10%")

                elif command == "mute":
                    os.system("amixer set Master toggle")
                    print("🔇 Muted/Unmuted Audio")

    except KeyboardInterrupt:
        print("\nStopping listener script.")
        sys.exit()
    except Exception as e:
   
        time.sleep(1)
