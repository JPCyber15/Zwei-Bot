import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_member_join(member):
    await member.send("Welcome to the Black Forest Discord and thank you for showing interest in our Guild to apply there are a few steps.\n1st Step: Join the Discord and change your nickname to your IGN( Easy :smiley:  )\n\n2nd Step: Go down to the #recruitment-application channel and post an application. An example of what to post will be provided on the channel and will also be pinned there. The information provided can been edited when ever needed.\n  -Information needed:\n    ~IGN\n    ~Account level\n    ~Raid stats(Lap Clears, Boss and Aid count)\n    ~Unit Screenshots\n     -This can be either your Friends list or your units in general. The more we know the better the odds are. You can also point out any notable units you'd like to recognize.\n\n3rd Step: Private message the Captain or Vice-Captain of the guild to notify us of your application\n\n4th Step: Once your Application is accepted send an ingame application to the guild for use to accept and we will get to it as soon as someone is avalable.\n\nThank you for Applying to the guild and we wish you the best of luck in the submission of you Applications.\n\nIf there are any updates in regards to recruitment they can be viewed in #recruitment-information or they will be Pmed to you if they are in regards to you.") 
@client.command()
async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
        
@client.command()
async def unload(ctx,extension):
        client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        
client.run('NTk5OTg4OTQxODAxNzgzMzE3.XSubnQ.65Zq9meoTzBxgqUZHMozDJ5W6fY')
