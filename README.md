# QuickReplaySorter

A simple and automated replay, video, and screenshot organizer designed specifically for World of Tanks and OBS.

## Features
* **One-Button Save (`Ctrl+F12`)**: Instantly gathers your latest OBS recording, completed match replay, and OBS screenshot, bundling them into a dedicated map folder.
* **OBS Integration**: Automatically utilizes OBS for both video and screenshot captures to bypass game DirectInput restrictions.
* **Smart Folder Naming**: Reads the finished `.wotreplay` file to automatically name your destination folders using the map and tank name.
* **Temp File Filter**: Safely ignores active `temp.wotreplay` files to ensure only completed matches are archived.

## How It Works
1. Finish a match and press `Ctrl+F12` (bound to stop recording and trigger screenshots in OBS).
2. The script waits 3 seconds to ensure both the OBS video and screenshot are fully written to the disk.
3. It bundles the latest files (Video, Replay, Screenshot) and moves them into a newly generated folder in your sorted directory.

## Requirements
* Python 3.x
* `keyboard` module

To install the required module, run:
```bash
pip install keyboard
