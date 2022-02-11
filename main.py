import discord
from discord.ext import commands
from discord.ext.commands import MemberConverter
import os

TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix='//')

@bot.event
async def on_ready():
  print('Benzene is ready to go!')

@bot.command()
async def ping(ctx):
  await ctx.channel.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def getpfp(ctx, arg):

  converter = MemberConverter()
  member = await converter.convert(ctx, arg)
  await ctx.send(member.avatar_url)

@bot.command()
async def clear(ctx, amount = 1):
  await ctx.channel.purge(limit = amount+1)

@bot.command(pass_context=True)
@commands.has_role("Admin")
@commands.has_permissions(kick_members=True)
async def kick(ctx, arg):
  converter = MemberConverter()
  member = await converter.convert(ctx, arg)
  await ctx.send('kik')
  await bot.kick(member)


bot.run(TOKEN)
