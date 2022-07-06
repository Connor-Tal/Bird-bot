import datetime
import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
guild = os.getenv('GUILD')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

#commands    
@bot.event
async def on_ready():
    print(bot.user.name,"has connected to", guild)

@bot.event
async def on_member_join(member):
    newbie = discord.utils.get(member.guild.roles, id = 993562619854200995)
    await member.add_roles(newbie)
    await member.send("Welcome to birds server!")

@bot.command(name = 'roll', help = 'Simulates rolling dice. !roll <number of dice>, <number or sides> ')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name = 'hello', help = 'Says hello. !hello')
async def hello(ctx):
    languages = [
        'Hola', 'Hello', 'Namaste', 'Konnichiwa', 'Guten tag', 'Hallo', 'Bonjour', 'Salam', 'Ciao', 'Shalom','Bonjou/Bonswa'
    ]
    hellovar = random.choice(languages)
    await ctx.send(hellovar)

@bot.command(name = 'ping', help = 'pong! !ping')
async def ping(ctx):
    await ctx.send('Pong!')
    await ctx.sent('/nick a')

@commands.has_permissions(ban_members=True)
@bot.command(name = 'ban', help = 'ADMIN ONLY bans a person !ban <member name> <reason>')
async def ban(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    await ctx.guild.ban(member, reason=reason)
    await ctx.send(f"{member.mention} has been **banned**", delete_after=1)
    embed = discord.Embed(title="Ban Log", description=f"{member.mention} has been **banned** by {ctx.author.mention}\n\nReason: `{reason}`\n\nbanned from: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"Ban log - Banned user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed, delete_after=1)
    await ctx.message.delete()
    await ctx.message.delete()
    print(f"Sucsessfully banned {member.name}")

@commands.has_permissions(ban_members=True)
@bot.command(name = 'kick', help = 'ADMIN ONLY kicks a member !kick <member name> <reason>')
async def kick(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    await ctx.guild.kick(member, reason=reason)
    await ctx.send(f"{member.mention} has been **kicked**", delete_after=1)
    embed = discord.Embed(title="Kick Log", description=f"{member.mention} has been **kicked** by {ctx.author.mention}\n\nReason: `{reason}`\n\nkicked from: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"kick log - kicked user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed, delete_after=1)
    await ctx.message.delete()
    await ctx.message.delete()
    print(f"Sucsessfully kicked {member.name}")

@commands.has_permissions(ban_members=True)
@bot.command(name = 'unban', help = 'ADMIN ONLY unbans a member !unban <member name> <reason>')
async def unban(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    await ctx.guild.unban(member, reason=reason)
    await ctx.send(f"{member.mention} has been **unbanned**", delete_after=1)
    embed = discord.Embed(title="Unban Log", description=f"{member.mention} has been **unbanned** by {ctx.author.mention}\n\nReason: `{reason}`\n\nUnbanned from: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"Unban log - Banned user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed, delete_after=1)
    await ctx.message.delete()
    await ctx.message.delete()
    print(f"Sucsessfully unbanned {member.name}")
   
@commands.has_permissions(ban_members=True)
@bot.command(name = 'mute', help = 'ADMIN ONLY mutes a member !mute <member name> <reason>')
async def mute(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    role = discord.utils.get(member.server.roles, name='Punished')
    await bot.add_roles(member, role)
    await ctx.send(f"{member.mention} has been **Muted**", delete_after=1)
    embed = discord.Embed(title="Mute Log", description=f"{member.mention} has been **Muted** by {ctx.author.mention}\n\nReason: `{reason}`\n\nMuted in: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"Mute log - Muted user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed,delete_after=1)
    await ctx.message.delete()
    await ctx.message.delete()
    print(f"Sucsessfully muted {member.name}")
    
@commands.has_permissions(ban_members=True)
@bot.command(name = 'unmute', help = 'ADMIN ONLY unmutes a member !unmute <member name> <reason>')
async def unmute(ctx, member:discord.User, *, reason=None):
    if reason == None:
        reason = f"No Reason Provided"
    role = discord.utils.get(member.server.roles, name='Punished')
    await bot.remove_roles(member, role)
    await ctx.send(f"{member.mention} has been **Unmuted**", delete_after=1)
    embed = discord.Embed(title="Unmute Log", description=f"{member.mention} has been **Unmuted** by {ctx.author.mention}\n\nReason: `{reason}`\n\nUnmuted in: `{ctx.guild.name}`", color=0x1355ed)
    embed.add_field(name="User", value=f"{member}", inline=True)
    embed.add_field(name="UserID", value=f"{member.id}", inline=True)
    embed.add_field(name="Moderator", value=f"{ctx.author}", inline=True)
    embed.set_footer(text=f"Mute log - Muted user: {member.name}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed,delete_after=1)
    await ctx.message.delete()
    await ctx.message.delete()
    await user.edit(mute=False)
    print(f"Sucsessfully muted {member.name}")

bot.run(token)
