import os
import discord
from discord.colour import Color
from discord.ext import commands
import random
import time

from discord.message import Message

client = commands.Bot(command_prefix="!")

@client.command()
async def akmping(ctx):
    await ctx.send(f"**AKMBot Is Currently On: {round(client.latency * 1000)} ms**")

@client.command()
@commands.has_permissions(administrator=True)
async def akmpurge(ctx, ammount = 25):
    await ctx.channel.purge(limit=ammount)

@client.command()
async def akmcommands(ctx):
    embedcmd=discord.Embed(title="AKMBot Help Page", description="Our bot currently has 6 commands. Here is our help page on them!", color=0xAD00FF )
    embedcmd.add_field(name="!akmhelpmod", value="This command will show all of our bots moderation and administration commands available.", inline=False) 
    embedcmd.add_field(name="!akmhelpgames", value="This command will show all of our bots minigame commands.", inline=False) 
    embedcmd.add_field(name="!akmhelpfun", value="This command will show all of our bots fun commands", inline=False)
    await ctx.send(embed=embedcmd)

@client.command()
@commands.has_permissions(administrator=True)
async def akmkick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def akmban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(administrator=True)
async def akmunban(ctx, *, member):
    banusers = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banusers:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)

@client.command()
async def akmhelpmod(ctx):
    embedcmd=discord.Embed(title="AKMBot Help Page: Moderation and Administration", description="The creator of this bot originally designed this for administration, here are some of his commands!", color=0xAD00FF )
    embedcmd.add_field(name="!akmpurge", value="Purges the past 25 messages in the server", inline=False)
    embedcmd.add_field(name="!akmunban", value="Unbans the user from the server so they can rejoin", inline=False)
    embedcmd.add_field(name="!akmkick", value="Kicks the given user from the server", inline=False)
    embedcmd.add_field(name="!akmban", value="Bans the given user permanently", inline=False)
    await ctx.send(embed=embedcmd)

@client.command()
async def akmnumgame(ctx, *, message):
    await ctx.send(f"**Your guess was: {message}, the Real number was: ||{random.randint(1,9)}||**")

@client.command()
@commands.has_permissions(administrator=True)
async def akmunmute(ctx, member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="muted")
   await member.remove_roles(mutedRole)
   await ctx.send(f"**Muted: {member}**")

@client.command()
@commands.has_permissions(administrator=True)
async def akmmute(ctx, member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="muted")
   await member.add_roles(mutedRole)
   await ctx.send(f"**Muted: {member}**")

@client.event
async def on_ready():
    print("Ready To Play!")

client.run("TOKEN HERE")