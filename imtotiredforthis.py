import discord
from discord.ext import commands

client = commands.Bot(command_prefix="j!")

@client.event
async def on_ready():
    print("insomniac?")

@client.command()
async def juniper(ctx):
    await ctx.send("my dev has the attention span of a cracker")

@client.command()
async def test(ctx):
    await ctx.send("this is a test too see if i know what **im** doing!")

@client.command()
async def treehouse(ctx):
    await ctx.send("hi welcome to the treehouse crew! **you're new aren't you?** yeah? yeah! i knew it wellim juniper and i'll be your guide")
    
@client.event
async def on_message(msg):
    if msg.author == client.user:
        return None

    if "juniper" in msg.content:
        await msg.add_reaction("<:space2:792960729120112652>")
    await client.process_commands(msg)

    if "Juniper" in msg.content:
        await msg.add_reaction("<:space2:792960729120112652>")
    await client.process_commands(msg)

    if "jUnIpEr" in msg.content:
        await msg.add_reaction("<:space2:792960729120112652>")
    await client.process_commands(msg)

    if "bee" in msg.content:
        await msg.add_reaction("<:con_Sayu_Bee:792963140136468491>")
    await client.process_commands(msg)

client.run('NzkyOTI2Mjc1ODE1NjA0MjY0.X-k0JA.VNBbmZPjubRBvPYIHVXlwQfMG4w')