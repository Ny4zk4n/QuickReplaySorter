# QuickReplaySorter

A simple and automated replay and video sorter designed specifically for World of Tanks. 

## Features
* **One-Button Automation**: Press `Ctrl+F12` after a match to trigger the sorting process.
* **Auto-Screenshot**: Automatically simulates the `PrtSc` key to capture match results before moving files.
* **Smart Folder Naming**: Reads the completed `.wotreplay` file and names the destination folder based on the map and tank played.
* **Multi-File Organization**: Groups your latest OBS video recording, World of Tanks replay, and screenshot together into the newly created map folder.
* **Temp File Filter**: Safely ignores active `temp.wotreplay` files to ensure only finished matches are archived.

## How It Works
1. Finish a match and press `Ctrl+F12`. (This also stops your OBS recording if you have the same hotkey set in OBS).
2. The script instantly taps `PrtSc` to take a World of Tanks screenshot.
3. It waits 3 seconds to ensure both the OBS video and the game screenshot are fully written to the disk.
4. It bundles the three latest files (Video, Replay, Screenshot) and moves them into a newly generated folder in your sorted directory.

## Requirements
* Python 3.x
* `keyboard` module

To install the required module, run:
```bash
pip install keyboard
```

## Configuration
The script is pre-configured with standard paths. If your game or OBS is installed elsewhere, modify the Configuration section at the top of `sorter.py`:
* `DEST_BASE_FOLDER = r"E:\sorted replays"`
* `OBS_FOLDER = r"E:\kayıtlar"`
* `REPLAY_FOLDER = r"E:\World_of_tankseplays"`
* `SCREENSHOT_FOLDER = r"E:\World_of_tanks\screenshots"`
