from discord.ext import commands
import discord, asyncio

class GMGN(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def gm(self, ctx):
        await ctx.send(f'<@{ctx.author.id}> wünscht allen einen guten Morgen!')

    @commands.command()
    async def gn(self, ctx):
        await ctx.send(f'<@{ctx.author.id}> wünscht allen eine gute Nacht!')



def setup(client):
    client.add_cog(GMGN(client))
    print('Der GMGN-Cog ist geladen')