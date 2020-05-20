import discord
from discord.ext import commands
import random

id_blacklist = [257016086522888192]

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def cursed(self, ctx):
        
        if ctx.author.id in id_blacklist:
            return
        
        from embedlinks import cursed_links
        
        try: 
            chosen_image = random.choice(cursed_links)
        
            embed = discord.Embed(colour=0xff69b4, 
                                  title="A Cursed Image.",
                                  description="you asked for this"
                                  )
            embed.set_image(url=chosen_image)
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        
            await ctx.send(embed=embed)
        except Exception as e:
            print(str(e))
            
    @commands.command()
    async def yixing(self, ctx):
        
        if ctx.author.id in id_blacklist:
            return
        
        from embedlinks import yixing
        
        try:
            quote = random.choice(yixing)
            
            embed = discord.Embed(colour=discord.Colour.blue(),
                                  title="Yixing Quotes",
                                  description=quote
                                  )
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            
            await ctx.send(embed=embed)
        except Exception as e:
            print(str(e))
        
def setup(client):
    client.add_cog(Fun(client))