from discord.ext import commands
import asyncio, discord
from main import client
class clear(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    @commands.has_role(846641785316704277)
    async def clear(self, ctx, count):
        count = int(count)
        try:
            count += 1
            await ctx.channel.purge(limit=count)
            embed = discord.Embed(title='Clear',
                                  description=f"Es wurden {str(count - 1)} Nachrichten gelöscht!",
                                  color=0x23ba65)
            await ctx.send(embed=embed, delete_after=10)

        except:
            return False



def setup(client):
    client.add_cog(clear(client))
    print('clear-Cog ist geladen')