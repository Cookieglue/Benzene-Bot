import discord
import os

token = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
  print('Logged {0.user}.format(client)')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('*/'):
    await message.channel.send('Hello!')
client.run(token)