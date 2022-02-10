import discord
from discord.ext import commands
import os

TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix='//')

@bot.command()
async def ping(ctx):
  await ctx.channel.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def getpfp(ctx):
  member = ctx.author
  await ctx.send(member.avatar_url)

bot.run(TOKEN)
