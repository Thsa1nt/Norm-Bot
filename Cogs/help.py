import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    # HELP
    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        embed = discord.Embed(
            title = 'Help',
            description = 'Use `.help <category>` for extended information on that command.',
            color = discord.Color.light_grey()
        )
        embed.add_field(name = 'Fun', value = '`ping`, `8ball`')
        embed.add_field(name = 'Actions', value = '`comfort`, `slap`')
        embed.add_field(name = 'Currency', value = '`balance`, `beg`, `work`, `gamble`')

        await ctx.send(embed=embed)

    # FUN
    @help.command()
    async def fun(self,ctx):
        embed = discord.Embed(
            title = 'Fun',
            description = 'All of the fun commands!',
            color = discord.Color.green()
        )
        embed.add_field(name= 'Ping', value = 'Sends Pong! \n`n.ping`')
        embed.add_field(name= '8ball', value = 'Gives you an answer to a yes or no quesstion. \n`n.8ball <question>`')
        
        await ctx.send(embed=embed)

    # ACTIONS
    @help.command()
    async def actions(self,ctx):
        embed = discord.Embed(
            title = 'Actions',
            description = 'All of the actions you can do.',
            color = discord.Color.gold()
        )
        embed.add_field(name= 'Comfort', value = 'Comfort a member! \n`n.comfort <member>`')
        embed.add_field(name= 'Slap', value = 'Slap a member in the face! \n`n.slap <member>`')
        
        await ctx.send(embed=embed)

    # CURRENCY
    @help.command()
    async def currency(self,ctx):
        embed = discord.Embed(
            title = 'Currency',
            description= 'Everything you need to know about the economy.',
            color = discord.Color.red()
        )
        embed.add_field(name = 'Balance', value = 'Gives the balance of a member. \n`n.balance [member]`')
        embed.add_field(name = 'Beg', value = 'Beg for money. \n`n.beg`')
        embed.add_field(name = 'Work', value = 'Work for more money! \n`n.work`')
        embed.add_field(name = 'Gamble', value = 'Gamble for the chance of doubling your bet. \n`n.gamble <amount>`')
        
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Help(bot))