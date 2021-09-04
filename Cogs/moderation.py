import discord
from discord.ext import commands

class Moderation(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot

    #Events
    #@commands.Cog.listener()
    #async def on_ready(self):
    #    print('Bot is ready.')
    
    #Commands
    @commands.command()
    async def clear(self,ctx, member: discord.Member, amount=1):
        await ctx.channel.purge(limit= amount + 1)
        
    @commands.command()
    async def kick(self,ctx, member : discord.Member, *, reason=None):
        if ctx.author == member:
            embed = discord.Embed(
            description= 'Error/You cannot kick yourself.',
            color= discord.Color.red()
        )
            await ctx.send(embed=embed)
        else:
            await member.kick(reason = reason)
            embed = discord.Embed(
                description= f'{member.mention} has been kicked.',
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def ban(self,ctx, member : discord.Member, *, reason=None):
        if ctx.author == member:
            embed = discord.Embed(
            description= 'Error/You cannot ban yourself.',
            color= discord.Color.red()
        )
            await ctx.send(embed=embed)
        else:
            await member.ban(reason = reason)
            embed = discord.Embed(
                description= f'{member.mention} has been banned.',
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)

    @commands.command()
    async def unban(self,ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
            embed = discord.Embed(
                description= f'{member} has been unbanned.',
                color = discord.Color.green()
            )
            await ctx.send(embed=embed)
            return


def setup(bot):
    bot.add_cog(Moderation(bot))