from discord.ext import commands
import discord, asyncio
from main import client


class Exapmple(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        
        #Code
        
        

def setup(client):
    client.add_cog(Example(client))
    print('Der Example-Cog ist geladen')
