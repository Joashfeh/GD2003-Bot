import discord
from discord.ext import commands
import datetime
import asyncio
import random

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

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')

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
    
    cursed_links = ["https://i.imgur.com/qGynhNc.jpg", 
                   "https://i.pinimg.com/564x/14/3d/aa/143daa1829004fb6355cc94ca187e435.jpg",
                   "https://i.imgur.com/ORD46Bl.jpg",
                   "https://i.imgur.com/KnYwCFp.jpg",
                   "https://i.imgur.com/i7foEYM.jpg",
                   "https://i.imgur.com/OXpPeRS.jpg",
                   "https://i.imgur.com/CVHGC23.jpg",
                   "https://i.imgur.com/jMVv3uj.jpg",
                   "https://i.imgur.com/YC0V2M3.jpg",
                   "https://i.imgur.com/2xedmhB.jpg",
                   "https://i.imgur.com/ff03NuR.jpg",
                   "https://i.imgur.com/koQSGlj.jpg",
                   "https://i.imgur.com/Az3DCJl.jpg",
                   "https://i.imgur.com/JBvf8L9.jpg",
                   "https://i.pinimg.com/564x/5a/1e/c6/5a1ec68e8fc6b253e06b9f49ff62af82.jpg",
                   "https://i.pinimg.com/564x/5d/a8/2b/5da82b0e303cd24c3d6fa823b5322c4b.jpg",
                   "https://i.pinimg.com/564x/49/a0/57/49a05725d156ba14981316c905fedd30.jpg",
                   "https://i.pinimg.com/564x/54/f3/c0/54f3c020061db594c48e83b4ec79ed41.jpg",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-01/sub-buzz-26051-1493924228-6.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14100-1493923518-11.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14243-1493923581-2.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-01/sub-buzz-31611-1493926072-5.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-01/sub-buzz-25632-1493923541-3.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22344-1493923414-4.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22202-1493923439-8.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-01/sub-buzz-26118-1493924202-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14165-1493923496-5.png?resize=990:508?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14153-1493923629-3.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22378-1493923704-1.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-03/sub-buzz-21981-1493926233-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-02/sub-buzz-30672-1493926811-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-01/sub-buzz-925-1493926856-5.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/16/asset/buzzfeed-prod-fastlane-01/sub-buzz-3901-1493931222-3.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/16/asset/buzzfeed-prod-fastlane-01/sub-buzz-4032-1493931335-3.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-03/sub-buzz-25203-1493931732-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-01/sub-buzz-904-1493926930-5.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/5/11/asset/buzzfeed-prod-fastlane-03/sub-buzz-7377-1493998812-25.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22826-1493924094-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22821-1493924291-5.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-03/sub-buzz-20203-1493925891-7.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-03/sub-buzz-22594-1493927334-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/16/asset/buzzfeed-prod-fastlane-02/sub-buzz-577-1493931099-6.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14491-1493923964-2.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/15/asset/buzzfeed-prod-fastlane-01/sub-buzz-935-1493926542-8.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/16/asset/buzzfeed-prod-fastlane-01/sub-buzz-3927-1493931291-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-02/sub-buzz-22503-1493924129-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/5/11/asset/buzzfeed-prod-fastlane-01/sub-buzz-21003-1493998845-14.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/16/asset/buzzfeed-prod-fastlane-03/sub-buzz-24782-1493931070-7.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-03/sub-buzz-25203-1493932139-6.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-03/sub-buzz-25339-1493931834-4.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14436-1493923735-2.png?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-02/sub-buzz-654-1493931689-5.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-02/sub-buzz-1400-1493932179-1.jpg?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/14/asset/buzzfeed-prod-fastlane-03/sub-buzz-14420-1493924033-18.jpg?resize=990:742?output-quality=auto&output-format=auto&downsize=640:*",
                   "https://img.buzzfeed.com/buzzfeed-static/static/2017-05/4/17/asset/buzzfeed-prod-fastlane-03/sub-buzz-25738-1493932534-1.jpg?output-quality=auto&output-format=auto&downsize=640:*"]
    
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

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing Arguments')   
            
client.run(TOKEN)