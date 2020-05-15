import discord
from discord.ext import commands
import datetime
import asyncio

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
           
        # Monday
        if day == "Monday":
            if tme == "07:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Personal Career Strategies is starting in 10 minutes')
                await asyncio.sleep(1)
                break
            if tme == "11:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Introduction to Coding is starting in 10 minutes')
                await asyncio.sleep(1)
                break            
            if tme == "14:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Object Oriented Programming is starting in 10 minutes')
                await asyncio.sleep(1)
                break
                
            # Tuesday
        if day == "Tuesday":
            if tme == "13:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Concept Ideation is starting in 10 minutes')
                await asyncio.sleep(1)
                break
                
            # Wednesday    
        if day == "Wednesday":
            if tme == "11:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Story Through Audio & Visual is starting in 10 minutes')
                await asyncio.sleep(1)   
                break
            if tme == "16:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Understanding Singapore is starting in 10 minutes')
                await asyncio.sleep(1)   
                break
                
            # Friday    
        if day == "Friday":
            if tme == "07:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Linear Algebra is starting in 10 minutes')
                await asyncio.sleep(1)
                break
            if tme == "09:50:00":
                await discord.abc.Messageable.send(ch, '@everyone Effective Communication Skills is starting in 10 minutes')
                await asyncio.sleep(1)
                break
            if tme == "13:00:00":
                await discord.abc.Messageable.send(ch, '@everyone niggas go watch your lectures :>')
                await asyncio.sleep(1)
                break
            if tme == "20:38:00":
                await discord.abc.Messageable.send(ch, 'test')
                await asyncio.sleep(1)
                break

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

@client.command()
async def clear(ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        print("Cleared", amount, "Messages")
        
@client.command()
async def time(ctx):
    await ctx.send('The time now is', datetime.datetime.strftime("%H:%M:%S"))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments')   
            
client.run(TOKEN)