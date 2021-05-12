from discord.ext import commands
import asyncio, discord

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(ctx, member: discord.Member = None, *, reason=None):
        if reason == None:
            await ctx.send(f'Warum willst du {member.name} kickten?\n'
                           f'Versuche es so erneut: `!kick member.name reason`')
        if not reason == None:
            if not member == None:
                em = discord.Embed(title=f'Kick',
                                   description=f'{member.display_name} wurde gekickt', colro=0xDF1414)
                await ctx.send(embed=em)
                if not member.create_dm:
                    await member.create_dm
                DmEmbed = discord.Embed(title=f'Du wurdest gekickt!',
                                        description=f'du wurdest vom TestServer gekickt! Grund:{reason}',
                                        color=0xDF1414)
                await member.send(embed=DmEmbed)
                await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member = None, *, reason=None):
        if reason == None:
            await ctx.send(f'Warum willst du {member.name} bannen?\n'
                           f'Versuche es so erneut: `!ban member.name reason`')
        if not reason == None:
            if not member == None:

                em = discord.Embed(title=f'Bann',
                                   description=f'{member.display_name} wurde gebannt', colro=0xDF1414)
                await ctx.send(embed=em)
                if not member.create_dm:
                    await member.create_dm
                DmEmbed = discord.Embed(title=f'Du wurdest gebannt!',
                                        description=f'Du wurdest vom TestServer gebannt! Grund:{reason}',
                                        color=0xDF1414)
                await member.send(embed=DmEmbed)
                await member.ban(reason=reason)




def setup(client):
    client.add_cog(Mod(client))
    print('ModCommands sind geladen')