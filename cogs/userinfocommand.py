from discord.ext import commands
import discord, asyncio

class UserinfoCommand(commands.Cog, name='UserinfoCommand'):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        em = discord.Embed(title=f'Dies ist eine Userinfo für {member.display_name}',
                           color=0x22a7f0)

        em.add_field(name='Server beigetreten',
                     value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                     inline=True)

        em.add_field(name='Discord beigetreten',
                     value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                     inline=True)
        rollen = ''
        for role in member.roles:
            if not role.is_default():
                rollen += '{} \r\n'.format(role.mention)
        if rollen:
            em.add_field(name='Rollen', value=rollen, inline=True)
        em.set_thumbnail(url=member.avatar_url)
        em.set_footer(text=f'Developer Rivonivo (Simon)#1738')
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(UserinfoCommand(client))
    print('Der UserinfoCommand-Cog ist geladen')