from discord.ext import commands
import discord, asyncio
from main import client
class OnJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if not member.bot:
            welcomeembed = discord.Embed(title=f'Wilkommen',
                                         description=f'Hallo {member} auf diesem Server! Viel Spaß')
            if not member.dm_channel:
                await member.create_dm()
            await member.send(embed=welcomeembed)
            role = discord.utils.get(member.guild.roles, name='Der ist ein guter Junge')
            await member.add_roles(role)


def setup(client):
    client.add_cog(OnJoin(client))
    print('Der OnJoin-Cog ist geladen')