import os
import time

print("Listening for iPhone commands... Press Ctrl+C to stop.")

while True:
	try: 
		with os.popen("sudo timeout 1 hcitool req") as stream:
			print("Data packet recived from iPhone!")
	except KeyboardInterrupt:
		break
	time.sleep(0.5)

