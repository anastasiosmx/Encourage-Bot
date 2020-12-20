import discord 
import os
import requests
import json
import random
from keep_alive import keep_alive


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "stenaxwrimenos", "angry", "miserable", "depressing", "katathlipsi"]

starter_encouragment = [
  "Cheer up!",
  "Hang in there.",
  "You are a great bot! I mean.. person.",
  "Dont feel bad! Type $inspire and i will help you cheer up!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+ json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send('''
    Welcome to the help section
    - $help    | Prints help message
    - $hello   | Welcome message 
    - $inspire | Returns you an inspiration quote
    ''')

  if message.content.startswith('$hello'):
    await message.channel.send('Helloooo!!! :D')
  
  if message.content.startswith('$inspire'):
    await message.channel.send(get_quote())

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(starter_encouragment))

keep_alive()
client.run(os.getenv('TOKEN'))
