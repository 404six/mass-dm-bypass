# import necessary libraries
from discord.ext import commands
import json
import requests

# create a new discord bot instance
bot = commands.Bot(command_prefix="", self_bot=True)

# load config data from a JSON file
with open('config.json') as c:
  cfg = json.load(c)
  # extract the token from the config data
  token = cfg["token"]

# helper function to make HTTP requests to the Discord API
def discord_api(endpoint, data):
  url = f"https://discord.com/api/{endpoint}"
  headers = {
    "authorization": token,
    "content-type": "application/json",
    "accept": "application/json"
  }
  # send the http request and parse the JSON response
  response = requests.post(url, headers=headers, data=json.dumps(data))
  return response.json()

# helper function to send a message to a user via dm
def send(user):
  # open a dm channel with the specified user
  open_dm = discord_api('/users/@me/channels', {"recipient_id": user})
  # send the message specified in the config file to the user
  discord_api("/channels/" + open_dm["id"] + "/messages",
              {"content": cfg["message"]})

# event handler that runs when the bot is ready to receive messages
@bot.event
async def on_ready():
  # loop through all the members of the guild specified in the config file
  for guild in bot.guilds:
    if guild.id == cfg["guild"]:
      for member in guild.members:
        # send a message to each member using the `send()` function
        send(member.id)

# start the bot and connect to the discord api using the provided token
bot.run(token)
