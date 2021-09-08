import discord
import json
import random
from discord.ext import commands

amounts = {}

def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)


class Currency(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        global amounts
        try:
            with open('amounts.json') as f:
                amounts = json.load(f)
        except FileNotFoundError:
            print("Could not load amounts.json")
            amounts = {}

    @commands.command()
    async def balance(self, ctx):
        id = str(ctx.message.author.id)
        if id in amounts:
            embed = discord.Embed(
                description= f'Balance: {amounts[id]} coins.',
                color = discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            amounts[id] = 0
            _save()
            embed = discord.Embed(
                description= f'Balance: {amounts[id]} coins.',
                color = discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        id = str(ctx.message.author.id)
        amount = random.randint(25, 200)
        amounts[id] += amount
        _save()
        await ctx.send(f'You were given {amount} coins.')
            

    @commands.command()
    async def save(self):
        _save()

def setup(bot):
    bot.add_cog(Currency(bot))