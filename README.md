# Discord Mass DM Selfbot

This is a Python script that allows you to send direct messages (DMs) to multiple users on Discord at once, without triggering the "captcha-required" error. This error can occur when you send a direct message using a selfbot, but this script works around that limitation by not triggering the captcha challenge that appears and resuming the message sending process.

## Installation

To use this script, you'll need to have Python 3 installed on your computer. You can download it from the [official website](https://www.python.org/downloads/).

You'll also need to install the following Python packages:

- [discord.py-self](https://github.com/dolfies/discord.py-self)
- [requests](https://pypi.org/project/requests/)

You can install these packages using the following command:

pip install discord.py-self requests

## Usage

To use this script, you'll need to modify the `config.json` file in the same directory as the script. The file should have the following structure:

```json
{
  "token": "TOKEN_HERE",
  "message": "MESSAGE_HERE",
  "guild": GUILD_ID_HERE
}
```

Please replace TOKEN_HERE with your Discord API token, which you can obtain from the Chrome DevTools. Additionally, replace MESSAGE_HERE with the message that you want to send to each user, and replace GUILD_ID_HERE with the ID of the guild that the script will retrieve all members from.

Once you've set up the `config.json` file, you can run the script using the following command:

```css
python main.py
```

The script will automatically send the message to each user in the specified guild.

Note: This script is intended for educational purposes only, and should not be used to spam or harass other users on Discord. Use it responsibly and at your own risk.

```
this script was created by me.
```
