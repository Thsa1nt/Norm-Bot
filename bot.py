import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

invite_link = 'https://discord.com/oauth2/authorize?client_id={0}&scope=bot&permissions={1}'.format(878977777074835487, 268528774)
print(invite_link)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
status = cycle(['Still Testing', 'Fixing bugs'])
bot.remove_command('help')

@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready.')

@bot.event
async def on_command_error(error):
    if isinstance(error,commands.MissingRequiredArgument):
        return
    elif isinstance(error, commands.CommandNotFound):
        return
    raise error

@bot.event
async def on_member_join(member : discord.Member):
    default_role = discord.utils.get(member.guild.roles, id=883596677234176030)
    await member.add_roles(default_role)
    channel = bot.get_channel(883597617009917982)
    await channel.send('Welcome {}!'.format(member.mention))

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

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

bot.run('ODc4OTc3Nzc3MDc0ODM1NDg3.YSJB2A.3uNvzlz9QSwoBIw1HDYYMksmbsk')