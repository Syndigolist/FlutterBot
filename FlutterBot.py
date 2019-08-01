import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "/")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_member_join(member):
    print(f'Welcome to the server, {member}! ^-^')

@client.event
async def on_member_remove(member):
    print(f':( See you later, {member}...')

@client.command()
async def ping(ctx):
    await ctx.send('Pong! ^^')
                    
@client.command()
async def howcute(ctx, *, person):
    responses = ['is very cute!!! ^^']
    await ctx.send(f'{person} is very cute!!! ^^')

@client.command()
async def alpaca(ctx):
    alpacas = ['https://imgur.com/VKAlGVV',
               'https://imgur.com/Fkm46S3',
               'https://imgur.com/a/HGTMuwM',
               'https://imgur.com/IDVS2xz',
               'https://imgur.com/a/NZ3BK6T',
               'https://imgur.com/Q15lgJe',
               'https://imgur.com/a/3tyj645',
               'https://imgur.com/ycdGcnM',
               'https://imgur.com/zwBRYXK',
               'https://imgur.com/a/hrhhkYt',
               'https://imgur.com/undefined',
               'https://imgur.com/a/t1plban',
               'https://imgur.com/a/9U0w2L7',
               'https://imgur.com/a/3VpJvjK',
               'https://imgur.com/gxGEM2E',
               'https://imgur.com/rO1Jl9D',
               'https://imgur.com/uRcIoH4',
               'https://imgur.com/Yiab3ha',
               'https://imgur.com/dgZIKsD',
               'https://imgur.com/rDNGN23',
               'https://imgur.com/9PxVvVr',
               'https://imgur.com/6A1dEil',
               'https://imgur.com/Q16S3jc',
               'https://imgur.com/8JEQEYW',
               'https://imgur.com/mnJce6N',
               'https://imgur.com/dJeuE2z',
               'https://imgur.com/JtCyWpD',
               'https://imgur.com/mDgn7qv',
               'https://imgur.com/3MNrZRp',
               'https://imgur.com/7iNO3CW']
    alpaca = random.choice(alpacas)
    await ctx.send('{}'.format(alpaca))

client.run("")
