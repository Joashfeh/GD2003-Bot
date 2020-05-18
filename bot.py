import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import datetime
import asyncio
import random
import os

TOKEN = 'NzA5NzA4OTY0OTE2NjI1NDI5.Xrp2KQ.KEWuDkssI-lKCqaOg8VZzk2-L_c'
client = commands.Bot(command_prefix = '!')   
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('No'))
    ch = client.get_channel(700684373174779925) 
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')  
    
    while True:
        date_time = datetime.datetime.now()
        day = date_time.strftime("%A")
        tme = date_time.strftime("%H:%M:%S")
        await asyncio.sleep(0.1)
        
        if tme == "16:20:00":
            await discord.abc.Messageable.send(ch, '@everyone blaze it')
            await asyncio.sleep(1)
            continue
           
        # Monday
        if day == "Monday":
            if tme == "07:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Personal Career Strategies is starting in 10 minutes')
                await asyncio.sleep(1)
                continue
            if tme == "11:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Introduction to Coding is starting in 10 minutes')
                await asyncio.sleep(1)
                continue           
            if tme == "14:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Object Oriented Programming is starting in 10 minutes')
                await asyncio.sleep(1)
                continue
                
            # Tuesday
        if day == "Tuesday":
            if tme == "13:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Concept Ideation is starting in 10 minutes')
                await asyncio.sleep(1)
                continue
                
            # Wednesday    
        if day == "Wednesday":
            if tme == "11:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Story Through Audio & Visual is starting in 10 minutes')
                await asyncio.sleep(1)   
                continue
            if tme == "16:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Understanding Singapore is starting in 10 minutes')
                await asyncio.sleep(1)   
                continue
                
            # Friday    
        if day == "Friday":
            if tme == "07:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Linear Algebra is starting in 10 minutes')
                await asyncio.sleep(1)
                continue
            if tme == "09:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Effective Communication Skills is starting in 10 minutes')
                await asyncio.sleep(1)
                continue
            if tme == "13:00:00":
                await discord.abc.Messageable.send(ch, '@everyone niggas go watch your lectures :>')
                await asyncio.sleep(1)  
                continue

@client.command()
async def clear(ctx, amount : int):
    if ctx.author.id == 189971597795262464:
        await ctx.channel.purge(limit=amount)
        print("Cleared", amount, "Messages")
    else:
        await ctx.send('You do not have the permissions to clear messages.')
        print("no.")
        
@client.command()
async def time(ctx):
    await ctx.send('The time now is ' + str(datetime.datetime.now().strftime("%H:%M:%S")))
    print (datetime.datetime.now())

@client.command()
async def cursed(ctx):
    
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
    except:
        print("Error")

@client.command()
async def crab(ctx):
    
    discord.opus.load_opus()
    
    url = 'https://www.youtube.com/watch?v=LDU_Txk06tM'
    
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
        
    else:
        voice = await channel.connect()
        
    await ctx.send(":crab:")
    
    # Play
    
    song_there = os.path.isfile("song.mp3")
    
    if song_there:
            os.remove("song.mp3")
    
    print("Someone wants to play music let me get that ready for them...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=True)
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            print(f"Renamed file: {file}\n")
            os.rename(file, 'song.mp3')
            await asyncio.sleep(1)
        
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
    
    print("Song Length: ", info_dict['duration'])
    await asyncio.sleep(info_dict['duration'] + 2)
    await voice.disconnect()

@client.command()
async def astronomia(ctx):
    
    discord.opus.load_opus()
    
    from embedlinks import astronomia
    
    url = random.choice(astronomia)
    
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
        
    else:
        voice = await channel.connect()
    
    # Play
    
    song_there = os.path.isfile("song.mp3")
    
    if song_there:
            os.remove("song.mp3")
    
    print("Someone wants to play music let me get that ready for them...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=True)
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            print(f"Renamed file: {file}\n")
            os.rename(file, 'song.mp3')
            await asyncio.sleep(1)
        
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()
    
    await ctx.send(f"Now Playing {info_dict['title']}")
    
    print("Song Length: ", info_dict['duration'])
    await asyncio.sleep(info_dict['duration'] + 2)
    await voice.disconnect()

@client.command()
async def stop(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"left {channel}")
        

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments')   
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if 'nigga' in str(message.content).lower():
        await discord.abc.Messageable.send(message.channel, ':regional_indicator_n::regional_indicator_i::regional_indicator_g::regional_indicator_g::regional_indicator_a: ')
    
    await client.process_commands(message)
            
client.run(TOKEN)