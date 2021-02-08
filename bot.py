#!/usr/bin/python3

import os
import discord
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

#client = discord.Client()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!!!")
    for guild in client.guilds:
        if guild.name == GUILD:
            print (
                    f"{client.user} is connected to the following guild:\n"
                    f"{guild.name}(id: {guild.id})"
            )
            break
    print(f"debug: guild.name: {guild.name}")
    for member in guild.members:
        print(f"Guild Member: {member}")
        time.sleep(0.1)

client.run(TOKEN)

