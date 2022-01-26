import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands.errors import CommandOnCooldown

invite_link = 'https://discord.com/oauth2/authorize?client_id={0}&scope=bot&permissions={1}'.format(878977777074835487, 268528774)
print(invite_link)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="n.", intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status= discord.Status.online, activity= discord.Game("n.help"))
    print('Bot is ready.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        return
    elif isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, CommandOnCooldown):
        if error.retry_after < 60:
            await ctx.send('Wait {0}s to use the command again.'.format(round(error.retry_after, 1)))
        elif error.retry_after >= 60 and error.retry_after < 3600:
            await ctx.send('Wait {0}min to use the command again.'.format(round(error.retry_after / 60, 1)))
        return
    raise error

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been loaded.',
        color= discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been unloaded.',
        color= discord.Color.blue()
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')
    bot.load_extension(f'Cogs.{extension}')
    embed = discord.Embed(
        description= f'{extension} has been reloaded.',
        color= discord.Color.blue() 
    )
    await ctx.send(embed=embed)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run('ODc4OTc3Nzc3MDc0ODM1NDg3.YSJB2A.3uNvzlz9QSwoBIw1HDYYMksmbsk')