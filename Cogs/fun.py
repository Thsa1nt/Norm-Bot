import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def comfort(self,ctx):
        title_list = ['(づ ◕‿◕ )づ', '⊂((・▽・))⊃', '(.づσ▿σ)づ.', '⊂( ◜◒◝ )⊃', '(づ￣ ³￣)づ']
        url_list = [
            'https://c.tenor.com/DCMl9bvSDSwAAAAd/pat-head-gakuen-babysitters.gif',
            'https://c.tenor.com/vcGsz5CfDs4AAAAC/peach-cat-peach.gif',
            'https://c.tenor.com/PiWq4kaQ6fkAAAAC/tonton-tonton-sticker.gif',
            'https://c.tenor.com/7jma_SAQl9YAAAAC/big-hero6-hug.gif',
            'https://c.tenor.com/uW0B9nSn4DsAAAAC/there-there-cats.gif'
        ]

        embed = discord.Embed(
            title = random.choice(title_list),
            color = discord.Color.blue()   
            )    
        embed.set_image(url=random.choice(url_list))
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.reply('Pong!')


    @commands.command(aliases = ['8ball'])
    async def _8ball(self,ctx, *, question):
        responses = ["It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
        await ctx.send(f'Question: {question}\nAsnwer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Fun(bot))