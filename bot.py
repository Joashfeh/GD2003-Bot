import discord
from discord.ext import commands
from discord.utils import get
import datetime
import asyncio
import os

client = commands.Bot(command_prefix = '!')   

id_blacklist = [257016086522888192]

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 189971597795262464:
        client.load_extension(f'cogs.{extension}')
        
        await ctx.send(f'{extension} loaded.')
    else:
        await ctx.send('You do not have the permissions to run this command')
    
@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 189971597795262464:
        client.unload_extension(f'cogs.{extension}')
        
        await ctx.send(f'{extension} unloaded.')
    else:
        await ctx.send('You do not have the permissions to run this command')
        
@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 189971597795262464:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        
        await ctx.send(f'{extension} reloaded.')
    else:
        await ctx.send('You do not have the permissions to run this command') 
   
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
async def time(ctx):
    
    if ctx.author.id in id_blacklist:
        return
    
    await ctx.send('The time now is ' + str(datetime.datetime.now().strftime("%H:%M:%S")))
    print (datetime.datetime.now())        
        
@client.event
async def on_message(message):
    
    if message.author.id in id_blacklist:
        return
    
    msg = message.content.lower()
    msg = msg.replace(" ", "")
    
    if message.author == client.user:
        return
    if 'nig' in msg or 'nibba' in msg:
        role = discord.utils.get(message.guild.roles, name="nigger")
        if role in message.author.roles:    
            await discord.abc.Messageable.send(message.channel, ':regional_indicator_n::regional_indicator_i::regional_indicator_g::regional_indicator_g::regional_indicator_a: ')
        else:
            ping = "{0.author.mention} Hey you can't say that".format(message)
            await discord.abc.Messageable.send(message.channel, ping)
    
    await client.process_commands(message)
            
        
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')    
    
with open('token.txt', 'r') as f:
    token = f.readline()
client.run(token)