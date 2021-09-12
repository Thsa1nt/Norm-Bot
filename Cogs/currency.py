import discord
import json
import random
from discord.ext import commands

amounts = {}

def save():
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
                print("Currency ready.")
        except FileNotFoundError:
            print("Could not load amounts.json")
            amounts = {}


    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        if member == None:
            author_id = str(ctx.message.author.id)
            if author_id not in amounts:
                amounts[author_id] = 0
                save()
            embed = discord.Embed(
                description= f'Balance: {amounts[author_id]} coins.',
                color = discord.Color.red()
            )
        else:
            member_id = str(member.id)
            if member_id not in amounts:
                amounts[member_id] = 0
                save()
            embed = discord.Embed(
                description= f'Balance: {amounts[member_id]} coins.',
                color = discord.Color.red()
            )        
        await ctx.send(embed=embed)
            
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        id = str(ctx.message.author.id)
        amount = random.randint(25, 200)
        amounts[id] += amount
        save()
        await ctx.send(f'You were given {amount} coins.')

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
        id = str(ctx.message.author.id)
        amount = random.randint(250, 1000)
        amounts[id] += amount
        save()
        await ctx.send(f'You were given {amount} coins.')

def setup(bot):
    bot.add_cog(Currency(bot))