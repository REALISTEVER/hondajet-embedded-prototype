# HondaJet CMS — Raspberry Pi experiments

Arthur Cox III — embedded prototyping for the NCAT HondaJet CMS capstone team. These are the recovered October 8, 2026 scripts, not the complete team system.

`app.py` reads commands from `/dev/rfcomm0` and invokes ALSA volume controls. `ble_control.py` is an early command-monitoring experiment using `hcitool`; its name does not establish working BLE control. The RFCOMM listener does not establish standard iPhone BLE compatibility.

Requires a Linux Raspberry Pi, BlueZ/RFCOMM tools, ALSA utilities, configured Bluetooth hardware and appropriate permissions. Hardware behavior has not been verified in this recovery. Prototype only, not aircraft software.
