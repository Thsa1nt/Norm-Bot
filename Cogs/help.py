import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Use `.help <command>` for extended information on that command.',
            color = discord.Color.light_grey()
        )
        embed.add_field(name = 'Moderation', value = 'clear \nkick \nban \nunban')
        embed.add_field(name = 'Fun', value = 'ping \n8ball')
        embed.add_field(name = 'Actions', value = 'comfort \nslap')

        await ctx.send(embed=embed)

    @help.command()
    async def kick(self,ctx):
        embed = discord.Embed(
            title = 'Kick',
            description = 'Kicks a member from the server.',
            color = discord.Color.light_grey()
        )
        embed.add_field(name = 'Syntax', value = '`.kick <member> [reason]`')

        await ctx.send(embed=embed)
    
    @help.command()
    async def ban(self,ctx):
        embed = discord.Embed(
            title = 'Ban',
            description = 'Bans a member from the server.',
            color = discord.Color.light_grey
        )
        embed.add_field(name = 'Syntax', value = '`.ban <member> [reason]`')

        await ctx.send(embed=embed)
    
    @help.command()
    async def clear(self,ctx):
        embed = discord.Embed(
            title = 'Clear',
            description = 'Clears a certain amount of messages.\nDefault is set to 1. ',
            color = discord.Color.light_grey
        )
        embed.add_field(name = 'Syntax', value = '`.clear [amount]`')

        await ctx.send(embed=embed)

    @help.command()
    async def unban(self,ctx):
        embed = discord.Embed(
            title = 'Unban',
            description = 'Unbans a user from the server.',
            color = discord.Color.light_grey
        )
        embed.add_field(name= 'Syntax', value = '`.unban <user>`')
        
        await ctx.send(embed=embed)

    @help.command()
    async def ping(self,ctx):
        embed = discord.Embed(
            title = 'Ping',
            description = 'Sends Pong!',
            color = discord.Color.light_grey
        )
        embed.add_field(name= 'Syntax', value = '`.ping`')
        
        await ctx.send(embed=embed)

    @help.command(aliases= ['8ball'])
    async def _8ball(self,ctx):
        embed = discord.Embed(
            title = '8ball',
            description = 'Gives you an answer to a yes or no question.',
            color = discord.Color.light_grey
        )
        embed.add_field(name= 'Syntax', value = '`.8ball <question>`')
        
        await ctx.send(embed=embed)

    @help.command()
    async def comfort(self,ctx):
        embed = discord.Embed(
            title = 'Comfort',
            description = 'Comfort a member!',
            color = discord.Color.light_grey
        )
        embed.add_field(name= 'Syntax', value = '`.comfort <member>`')
        
        await ctx.send(embed=embed)

    @help.command()
    async def slap(self,ctx):
        embed = discord.Embed(
            title = 'Slap',
            description = 'Slap a member in the face!',
            color = discord.Color.light_grey
        )
        embed.add_field(name= 'Syntax', value='`.slap <member>`')

def setup(bot):
    bot.add_cog(Help(bot))