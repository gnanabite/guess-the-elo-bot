import discord
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)