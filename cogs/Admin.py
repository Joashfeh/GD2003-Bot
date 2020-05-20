import discord
from discord.ext import commands

id_blacklist = [257016086522888192]

class Admin(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def clear(self, ctx, amount : int):
        if ctx.author.id == 189971597795262464:
            await ctx.channel.purge(limit=amount)
            print("Cleared", amount, "Messages")
        else:
            await ctx.send('You do not have the permissions to clear messages.')
            print("no.")
                
    @clear.error
    async def clear_error_handler(self, ctx, error):
        await ctx.send('```py\n{}: {}\n```'.format(type(error).__name__, str(error)))       
        
def setup(client):
    client.add_cog(Admin(client))