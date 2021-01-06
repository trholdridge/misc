# bot.py
import os
import numpy as np

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "casashee tests"

# dictionary to match tile name with correct custom emoji
emoji_id_dict = {}

client = discord.Client()

@client.event
async def on_ready():
    # connecting to casashee test server
    home_guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{home_guild.name}(id: {home_guild.id})'
    )

    for emoji in home_guild.emojis:
        emoji_id_dict[emoji.name] = str(emoji.id)

    for key, value in emoji_id_dict.items():
        print(key + ": " + value)

client.run(TOKEN)
