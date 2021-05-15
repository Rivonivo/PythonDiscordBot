from discord.ext import commands
import discord, asyncio
from main import client


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')




def setup(client):
    client.add_cog(Ping(client))
    print('Der Ping-Cog ist geladen')