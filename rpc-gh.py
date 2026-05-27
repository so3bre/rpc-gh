import time
import requests
import xml.etree.ElementTree as ET
from pypresence import Presence, ActivityType
import config # congig.py file
from datetime import datetime, timezone, timedelta

# --- CONFIGURATION ---
LARGE_IMAGE_KEY = 'github'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# Available ActivityType options:
# ActivityType.PLAYING
# ActivityType.STREAMING
# ActivityType.LISTENING
# ActivityType.WATCHING
# ActivityType.COMPETING

# Select your activity mode
SELECTED_ACTIVITY = ActivityType.COMPETING
# --- END CONFIG ---

RPC = Presence(config.APPLICATION_ID)

def get_latest_activity():
    try:
        url = f"https://github.com/{config.GITHUB_USER}.atom"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            entry = root.find('{http://www.w3.org/2005/Atom}entry')

            if entry is not None:
                # Get activity title
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                clean_title = title.replace(f"{config.GITHUB_USER} ", "").strip()

                # --- LOGIC START ---
                # Get the update time from the XML
                updated_str = entry.find('{http://www.w3.org/2005/Atom}updated').text
                updated_dt = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))

                # If the last activity was more than 30 minutes ago, return None
                if datetime.now(timezone.utc) - updated_dt > timedelta(minutes=30):
                    return None
                # --- LOGIC END ---

                return clean_title
    except Exception as e:
        print(f"Error: {e}")
    return None

def main():
    try:
        RPC.connect()
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    try:
        while True:
            activity = get_latest_activity()
            if activity:
                RPC.update(
                    details="GitHub",
                    state=activity,
                    large_image=LARGE_IMAGE_KEY,
                    activity_type=SELECTED_ACTIVITY,
                    buttons=[{"label": "View Profile", "url": config.GITHUB_URL}]
                )
            else:
                RPC.clear()

            time.sleep(60)

    except KeyboardInterrupt:
        print("\nStopping script...")
    finally:
        print("Cleaning up RPC...")
        RPC.close()

if __name__ == "__main__":
    main()
