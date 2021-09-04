import discord
import os
from discord.colour import Color
from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
status = cycle(['Still Testing', 'Fixing bugs'])
bot.remove_command('help')

@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been loaded.',
        color= discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been unloaded.',
        color= discord.Color.green()
    )
    await ctx.send(embed=embed)

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')
    bot.load_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been reloaded.',
        color= discord.Color.green()
    )
    await ctx.send(embed=embed)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

bot.run('ODc4OTc3Nzc3MDc0ODM1NDg3.YSJB2A.3uNvzlz9QSwoBIw1HDYYMksmbsk')