import time
import requests
import xml.etree.ElementTree as ET
from pypresence import Presence, ActivityType
import config # congig.py file

# --- CONFIGURATION ---
LARGE_IMAGE_KEY = 'github'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
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
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                # Remove username and clean up
                clean_title = title.replace(f"{config.GITHUB_USER} ", "").strip()
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

if __name__ == "__main__":
    main()
