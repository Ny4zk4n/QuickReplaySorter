import keyboard
import time
import os
import shutil
import glob
from datetime import datetime

# --- Configuration ---
DEST_BASE_FOLDER = r"E:\sorted replays"
OBS_FOLDER = r"E:\kayıtlar"
REPLAY_FOLDER = r"E:\World_of_tanks\replays"
SCREENSHOT_FOLDER = r"E:\kayıtlar"

VIDEO_EXT = "*.mkv"
REPLAY_EXT = "*.wotreplay"
SCREENSHOT_EXT = "*.png"


def get_latest_file(folder, extension, exclude_name=None):
    if not os.path.exists(folder):
        print(f"[-] Directory does not exist: {folder}")
        return None

    search_pattern = os.path.join(folder, extension)
    files = glob.glob(search_pattern)

    if exclude_name:
        files = [
            f for f in files
            if exclude_name.lower() not in os.path.basename(f).lower()
        ]

    if not files:
        return None

    return max(files, key=os.path.getmtime)


def handle_clip_pipeline():
    print("\n[!] Ctrl+F12 detected.")
    print("[!] Waiting 3 seconds for OBS/WoT to finish writing files...")

    time.sleep(3)

    latest_video = get_latest_file(OBS_FOLDER, VIDEO_EXT)

    latest_replay = get_latest_file(
        REPLAY_FOLDER,
        REPLAY_EXT,
        exclude_name="temp.wotreplay"
    )

    latest_screenshot = get_latest_file(
        SCREENSHOT_FOLDER,
        SCREENSHOT_EXT
    )

    # Nothing found
    if not latest_video and not latest_replay and not latest_screenshot:
        print("[-] No new video, replay, or screenshot found.")
        return

    # Use replay filename for folder name
    if latest_replay:
        folder_name = os.path.splitext(
            os.path.basename(latest_replay)
        )[0]
    else:
        folder_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    target_dir = os.path.join(
        DEST_BASE_FOLDER,
        folder_name
    )

    os.makedirs(target_dir, exist_ok=True)

    # -------------------------
    # Move Video
    # -------------------------
    if latest_video:
        try:
            shutil.move(latest_video, target_dir)
            print(f"[+] Moved Video: {os.path.basename(latest_video)}")
        except PermissionError:
            print("[-] Video is locked. OBS may still be writing it.")
        except Exception as e:
            print(f"[-] Error moving video: {e}")

    # -------------------------
    # Move Replay
    # -------------------------
    if latest_replay:
        try:
            shutil.move(latest_replay, target_dir)
            print(f"[+] Moved Replay: {os.path.basename(latest_replay)}")
        except Exception as e:
            print(f"[-] Error moving replay: {e}")

    # -------------------------
    # Move Screenshot
    # -------------------------
    if latest_screenshot:
        try:
            shutil.move(latest_screenshot, target_dir)
            print(f"[+] Moved Screenshot: {os.path.basename(latest_screenshot)}")
        except Exception as e:
            print(f"[-] Error moving screenshot: {e}")

    print(f"[✓] Operation finished.")
    print(f"[✓] Files saved to: {target_dir}\n")


# =========================================================
# HOTKEY
# =========================================================

keyboard.add_hotkey(
    'ctrl+f12',
    handle_clip_pipeline,
    suppress=False
)


print("========================================")
print(" WoT Replay / OBS Clip Organizer")
print("========================================")
print("Ctrl+F12 = SAVE current game")
print("Press Ctrl+C in this console to exit.")
print("========================================")
print("Listening for Ctrl+F12...\n")

keyboard.wait()