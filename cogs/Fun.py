import discord
from discord.ext import commands
import random
import json

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
            
    @commands.group()
    async def yixing(self, ctx):
        with open("embedlinks.json", "r+") as f:
            db = json.load(f)
            # reading
                  
        if ctx.author.id in id_blacklist:
            return
        
        if ctx.invoked_subcommand is None:
            try:
                quote = random.choice(db['yixing'])
                
                embed = discord.Embed(colour=discord.Colour.blue(),
                                      title="Yixing Quotes",
                                      description=quote
                                      )
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                
                await ctx.send(embed=embed)
            except Exception as e:
                print(str(e))
        
    @yixing.command()
    async def add(self, ctx, *, quote):   
        if ctx.author.id == 189971597795262464:
            with open("embedlinks.json", "r+") as f:
                db = json.load(f)
                # updating
                f.seek(0)
                f.truncate(0)
                db['yixing'].append(quote)
                json.dump(db, f, indent=4, sort_keys=True)
            
    @yixing.command(name='list')
    async def __list(self, ctx):
        with open("embedlinks.json", "r+") as f:
            db = json.load(f)
                
            embed = discord.Embed(colour=discord.Colour.blue(),
                                  title="Yixing Quotes",
                                  description="\n".join(db['yixing'])
                                  )
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            
            await ctx.send(embed=embed)
        
        
            
            
def setup(client):
    client.add_cog(Fun(client))