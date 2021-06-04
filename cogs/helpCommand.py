from discord.ext import commands
import asyncio, discord

class helpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title=f'Help',
                           description=f'`!help` - Zeigt diese Hilfe an!\n'
                                       f'`!clear <count>` - Löscht Nachrichten beliebig(Clear Rolle erforderlich)\n'
                                       f'`!ping` - Zeigt deine Latenz von dir bis zum Host an!\n'
                                       f'`!gm/!gn` - Ihr wünscht allen eine/n gute/n Morgen/Nacht!\n'
                                        f'`!meme` - Zeigt ein Meme an',
                           color=0x30DF40)
        em.set_footer(text=f'Angefordert von {ctx.author.name}',
                      icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(helpCommand(client))
    print('helpCommand ist geladen')