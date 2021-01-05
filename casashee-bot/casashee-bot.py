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

# define all types of squares -- normal, hill, and capital
N, H, C = "normal","hill","capital"

# define all types of pieces -- army, camp, tower
A, C, T = "army","camp","tower"

# holds the current state of a casashee game
current_game_state = np.zeros((5,5))

# starting state of a casashee game
initial_game_state = [[]]

# game_state_to_message
# takes a 2d array of characters representing the state of a square on the board,
# and converts this to the appropriate visual representation of the board
# def game_state_to_message(state):

client.run(TOKEN)
