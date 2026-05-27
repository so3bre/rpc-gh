# GitHub Discord RPC 🚀
A lightweight Python script to display your latest GitHub activity in your Discord status using Rich Presence.

## Prerequisites
* **Python 3.x** (installed on your system)
* **pip** (Python package manager)

To install the required libraries, run:
```bash
pip install -r requirements.txt
```

## Installation
Clone this repository to your system:

```bash
git clone https://github.com/so3bre/rpc-gh.git && cd rpc-gh 
```  

## Setup
1. **Create App**: Go to the [Discord Developer Portal](https://discord.com/developers/applications) and click "New Application". You can name it "GitHub" or choose any name you prefer.

2. **App Icon**: In "General Information", upload the image from the `/assets` folder as your app icon.

### Asset Configuration
* **Important**: To ensure the activity logo displays correctly, use a "clearspace" image (padding around the logo).

* Ensure that the image you uploaded as your **App Icon** is named `github` (as specified in your `rpc-gh.py` configuration).

## Configuration
Copy the example config and edit it with your credentials:

```bash
cp config.py.example config.py && nano config.py
```

Fill in your APPLICATION_ID, GITHUB_USER, and GITHUB_URL.

## Systemd Service (Recommended)
To run the script in the background automatically:

1. Copy the example service file:

	```bash
	cp rpc-gh.service.example ~/.config/systemd/user/rpc-gh.service
	```

2. Edit the file (update WorkingDirectory and ExecStart to your path):

	```bash
	nano ~/.config/systemd/user/rpc-gh.service
	```

3. Enable and start the service:

	```bash
	systemctl --user daemon-reload && systemctl --user enable --now rpc-gh.service
	```

## Manage Service
You can use the provided `aliases-rpc-gh.sh` to control the service easily.

**For a single session:**

```bash
source ~/path/to/rpc-gh/aliases-rpc-gh.sh
```

**To make these aliases permanent:**
Append the source command to your shell configuration file (.bashrc for Bash or .zshrc for Zsh):

For Bash:

```bash
echo "source ~/path/to/rpc-gh/aliases-rpc-gh.sh" >> ~/.bashrc
```

For Zsh:

```bash
echo "source ~/path/to/rpc-gh/aliases-rpc-gh.sh" >> ~/.zshrc
```

After doing this, restart your terminal or run `source ~/.bashrc` *(or ~/.zshrc)*.

Then you can use: `rpc-gh-start`, `rpc-gh-stop`, `rpc-gh-status`, `rpc-gh-restart`, `rpc-gh-edit`, `rpc-gh-logs`

## Architecture
* **rpc-gh.py** — The main script logic.

* **config.py** — User settings (ignored by git).

* **config.py.example** — Configuration template.

* **rpc-gh.service.example** — Systemd template for background execution.

* **aliases-rpc-gh.sh** — Shortcut commands.

* **assets/** — Assets for Rich Presence.

## License
MIT
