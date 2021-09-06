import discord
from discord.ext import commands
import random

class Actions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        url_list = [
            'https://c.tenor.com/PTONt_7DUTgAAAAC/batman-slap-robin.gif',
            'https://c.tenor.com/vr7tTAEuj1QAAAAC/baka-slap.gif',
            'https://c.tenor.com/L0U84S9YTrYAAAAC/pikachu-slap.gif',
            'https://c.tenor.com/mMGM1FfaXLgAAAAC/slap-cat.gif'
        ]
        if ctx.author == member:
            await ctx.send(f'{ctx.author.name}.... you can\'t slap yourself!')
        else:
            embed = discord.Embed(
                description= f'{ctx.author.name} slaps {member.display_name}!!',
                color= discord.Color.gold()
            )
            embed.set_image(url=random.choice(url_list))
            await ctx.send(embed=embed)

    @commands.command()
    async def comfort(self,ctx, member: discord.Member):
        hugs = ['(づ ◕‿◕ )づ', '⊂((・▽・))⊃', '(.づσ▿σ)づ.', '⊂( ◜◒◝ )⊃', '(づ￣ ³￣)づ']
        url_list = [
            'https://c.tenor.com/DCMl9bvSDSwAAAAd/pat-head-gakuen-babysitters.gif',
            'https://c.tenor.com/vcGsz5CfDs4AAAAC/peach-cat-peach.gif',
            'https://c.tenor.com/PiWq4kaQ6fkAAAAC/tonton-tonton-sticker.gif',
            'https://c.tenor.com/7jma_SAQl9YAAAAC/big-hero6-hug.gif',
            'https://c.tenor.com/uW0B9nSn4DsAAAAC/there-there-cats.gif'
        ]

        if ctx.author == member:
            await ctx.send(f'It\'ll be okay {ctx.author.name} {random.choice(hugs)}')
        else:
            embed = discord.Embed(
                description = f'{ctx.author.name} comforts {member.name} {random.choice(hugs)}',
                color = discord.Color.blue()   
                )    
            embed.set_image(url=random.choice(url_list))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Actions(bot))