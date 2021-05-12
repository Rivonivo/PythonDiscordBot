import discord, asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot ist online!')
    print(f'Bot Name: {client.user.name}')
    print(f'Bot ID: {client.user.id}')

@client.command()
async def help(ctx):
    em = discord.Embed(title=f'Help',
                       description=f'`!help` - Zeigt diese Hilfe an!',
                       color=0x30DF40)
    em.set_footer(text=f'Angefordert von {ctx.author.name}',
                  icon_url=ctx.author.avatar_url)
    await ctx.send(embed=em)

@client.command()
@commands.has_permissions(ban_members=True)
async def kick(ctx, member:discord.Member=None,*, reason=None):
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
                            description=f'du wurdest vom TestServer gekickt! Grund:{reason}', color=0xDF1414)
            await member.send(embed=DmEmbed)
            await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member=None,*, reason=None):
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
                            description=f'Du wurdest vom TestServer gebannt! Grund:{reason}', color=0xDF1414)
            await member.send(embed=DmEmbed)
            await member.ban(reason=reason)


client.run('ODQwNDM1NjI2MzE0MTcwNDA4.YJYKqw.IWGGEKatkNeZvUM9W7bUO_y0sgU')