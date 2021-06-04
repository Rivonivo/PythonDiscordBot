import discord, asyncio, os
from discord.ext import commands

client = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())



for file in os.listdir(r'cogs'):
    if file.endswith('.py'):
        extension = file.replace('.py', '')
        try:
            client.load_extension(f'cogs.{extension}')
        except Exception as error:
            print(error)



@client.event
async def on_ready():
    print(f'Bot ist online!')
    print(f'Bot Name: {client.user.name}')
    print(f'Bot ID: {client.user.id}')
    client.loop.create_task(status_task())

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('mit rivonivo (Simon)#1738'))
        await asyncio.sleep(7)
        await client.change_presence(activity=discord.Game('mit den Commands'))
        await asyncio.sleep(7)




client.run('ODQwNDM1NjI2MzE0MTcwNDA4.YJYKqw.2fiBimll5xLvbeEiIynE951Wnh0')