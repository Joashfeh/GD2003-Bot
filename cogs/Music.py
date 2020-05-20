import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random

id_blacklist = [257016086522888192]

class Music(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    async def play(self, ctx, song):      
        
        if ctx.author.id in id_blacklist:
            return
        
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        
        if voice and voice.is_connected():
            await voice.move_to(channel)
            return           
        else:
            voice = await channel.connect()
        
        # Play
           
        voice.play(discord.FFmpegPCMAudio(f"{song}.mp3"), after=lambda e: print("Song complete"))
        voice.volume = 100
        voice.is_playing()
        
        print(f"Song Playing: {song}")
        
        if not voice.is_playing():
            await asyncio.sleep(2)
            await voice.disconnect()
        
    
    @commands.command()
    async def stop(self, ctx):
        
        if ctx.author.id in id_blacklist:
            return
        
        global voice
        channel = ctx.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        
        print(channel)
        print(voice)
        
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send(f"left {channel}")
        else:
            await ctx.send("I am not connected to a channel.")
            
    @commands.command()
    async def oceanman(self, ctx):
        await self.play(ctx, 'Ocean Man')
        await ctx.send("OCEAN MAN :ocean: :heart_eyes: Take me by the hand :raised_hand: lead me to the land that you understand :raised_hands: :ocean: OCEAN MAN :ocean: :heart_eyes: The voyage :bike: to the corner of the :earth_americas: globe is a real trip :ok_hand: :ocean: OCEAN MAN :ocean: :heart_eyes: The crust of a tan man :person_wearing_turban: imbibed by the sand :thumbsup: Soaking up the :sweat_drops: thirst of the land :100:")
   
    @commands.command()
    async def crab(self, ctx):
        await self.play(ctx, 'Noisestorm - Crab Rave [Monstercat Release]')
        await ctx.send(":crab:")       
            
    @commands.command()
    async def astronomia(self, ctx):
        from embedlinks import astronomia_titles
        url = random.choice(astronomia_titles)
        
        await self.play(ctx, url)
        await ctx.send(f"Now Playing: {url}")  
            
def setup(client):
    client.add_cog(Music(client))