import discord
from discord.ext import commands
import random

def getList(dict):
    return list(dict.keys())

class Actions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gecko(self, ctx):
        geckos = {
            'smiling gecko': 'https://cdn.discordapp.com/attachments/795740317092544552/935073364840685649/2Q.png',
            'taxi gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935073458931515402/Z.png',
            'vibing gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935073668306972732/PJWXa05ce2ff8838bb92.png',
            'smoking croc' : 'https://cdn.discordapp.com/attachments/795740317092544552/935073798758207518/d3821626c12da4b566e6f439b625bbe1.png',
            'flying gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935073927091339315/bef84a9d193e228cfd535e9c271d9b7c.png',
            'police gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935074540869005322/gecko-police.png',
            'dancing gecko' : 'https://c.tenor.com/Mk4acoRU3isAAAAd/grooving-lizard.gif',
            'floating gecko' : 'https://c.tenor.com/ptIiB1fu0jgAAAAC/crocodile.gif',
            'party gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935075086287929344/Dancing_Song.jpg',
            'rare song gecko' : 'https://cdn.discordapp.com/attachments/795740317092544552/935075086677991454/Songecko.png'
        }
        gecko = random.choice(getList(geckos))
        embed = discord.Embed(
            description = f'You got the {gecko}! :D',
            color = discord.Color.green()
        )
        embed.set_image(url=geckos[gecko])
        await ctx.send(embed=embed)

    @commands.command()
    async def headpat(self, ctx, member: discord.Member):
        url_list = [
            'https://c.tenor.com/Tvsh9ev5H1gAAAAC/pat-dinosaurs.gif',
            'https://c.tenor.com/suz8j0HrrXEAAAAC/its-gonna-be-okay-hug.gif',
            'https://c.tenor.com/1I1pGUd3xWkAAAAC/mala-mishra-jha-pat-head.gif',
            'https://c.tenor.com/s7lGkoIAieYAAAAC/so-cute-cat.gif',
            'https://c.tenor.com/Av63tpT8Y14AAAAC/pat-head.gif',
            'https://c.tenor.com/f29x6FBv9TUAAAAC/monika-headpat-not-mine-btw.gif',
        ]
        if ctx.author == member:
            await ctx.send(f'You pat yourself on the head!')
        elif ctx.message.author.id == 230745107039518721 and member.id == 848269809899536405:
            embed = discord.Embed(
                description = f'{ctx.author.name} is giving {member.display_name} headpats ^^',
                color = discord.Color.orange()
            )
            embed.set_image(url='https://c.tenor.com/N41zKEDABuUAAAAC/anime-head-pat-anime-pat.gif')
            await ctx.send(embed=embed)
        elif ctx.message.author.id == 848269809899536405 and member.id == 230745107039518721:
            embed = discord.Embed(
                description = f'{ctx.author.name} is giving {member.display_name} headpats ^^',
                color = discord.Color.orange()
            )
            embed.set_image(url='https://media.discordapp.net/attachments/837304886700933152/848006740243251230/petpet.gif')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                description = f'{ctx.author.name} is giving {member.display_name} headpats ^^',
                color = discord.Color.orange()
            )
            embed.set_image(url=random.choice(url_list))
            await ctx.send(embed=embed)


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
                description = f'{ctx.author.name} comforts {member.display_name} {random.choice(hugs)}',
                color = discord.Color.blue()   
                )    
            embed.set_image(url=random.choice(url_list))
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss (self, ctx, member: discord.Member):
        emoji_list = [':flushed:', ':smirk:']
        url_list = [
            'https://c.tenor.com/Aaxuq2evHe8AAAAC/kiss-cute.gif',
            'https://c.tenor.com/lzAcq8iGn7kAAAAC/laughing-out.gif',
            'https://c.tenor.com/pmtj0zH1g2wAAAAC/kissdofull.gif',
            'https://c.tenor.com/wNHym8pk0a4AAAAC/love-anime.gif',
            'https://c.tenor.com/7T1cuiOtJvQAAAAC/anime-kiss.gif'
        ]
        if ctx.author == member:
            await ctx.send(f'You can\'t kiss yourself {ctx.author.name} smh.')
        elif (ctx.message.author.id == 698537464083513344 and member.id == 511698290035916810) or (ctx.message.author.id == 511698290035916810 and member.id == 698537464083513344):
            embed = discord.Embed(
                description = f'{ctx.author.name} is kissing {member.display_name}! {random.choice(emoji_list)}',
                color = discord.Color.dark_red(),
            )
            embed.set_image(url='https://c.tenor.com/dYolCGLIsXsAAAAC/boys-gay.gif')
            await ctx.send(embed=embed)
        else: 
            embed = discord.Embed(
                description = f'{ctx.author.name} is kissing {member.display_name}! {random.choice(emoji_list)}',
                color = discord.Color.dark_red()
            )
            embed.set_image(url=random.choice(url_list))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Actions(bot))