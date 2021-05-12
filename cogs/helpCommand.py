from discord.ext import commands
import asyncio, discord

class helpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title=f'Help',
                           description=f'`!help` - Zeigt diese Hilfe an!\n',
                           color=0x30DF40)
        em.set_footer(text=f'Angefordert von {ctx.author.name}',
                      icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(helpCommand(client))
    print('helpCommand ist geladen')