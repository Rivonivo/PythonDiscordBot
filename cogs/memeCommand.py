import random, aiohttp, discord, asyncio
from discord.ext import commands

class memecommand(commands.Cog):
    def __init(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        if ctx.channel.id == 850289264477732894:

            embed = discord.Embed(title='', description='')
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                    await ctx.send(embed=embed)
        if not ctx.channel.id == 850289264477732894:
            await ctx.send(f'Du kannst nur in <#850289264477732894> Memes anfragen!')


def setup(client):
    client.add_cog(memecommand(client))
    print('Der memecommand-Cog ist geladen!')