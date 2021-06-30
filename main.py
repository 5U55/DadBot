import discord, os, random
from keep_alive import keep_alive

client = discord.Client()

reprimainds = ['Language ', 'We don\'t use that language in this household ', 'Watch your mouth ', 'Hey, watch your language ']

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if 'i am ' in message.content.lower():
    await message.channel.send('Hi '+message.content[message.content.lower().index('i am ')+5:len(message.content)]+' I\'m Dad')
  if 'i\'m ' in message.content.lower():
    await message.channel.send('Hi '+message.content[message.content.lower().index('i\'m ')+4:len(message.content)]+' I\'m Dad')
  if 'im ' in message.content.lower():
    if message.content.lower().index('im ') == 0 or message.content[message.content.lower().index('im ')-1] == ' ':
      await message.channel.send('Hi '+message.content[message.content.lower().index('im ')+3:len(message.content)]+' I\'m Dad')
  if message.content.lower() == 'hell':
    await message.channel.send(random.choice(reprimainds)+'{}'.format(message.author.display_name))
  if message.content.lower() == 'heck':
    await message.channel.send(random.choice(reprimainds)+'{}'.format(message.author.display_name))
  if message.content.lower() == 'damn':
    await message.channel.send(random.choice(reprimainds)+'{}'.format(message.author.display_name))
  if message.content.lower() == 'shoot':
    await message.channel.send(random.choice(reprimainds)+'{}'.format(message.author.display_name))
  if 'dad bot' in message.content.lower():
    await message.channel.send('Yes, {} , you said my name?'.format(message.author.display_name))
  if 'dad' in message.content.lower():
    await message.channel.send('Yes, {} , you said my name?'.format(message.author.display_name))
  if 'what\'s up' in message.content.lower():
    await message.channel.send('The sky ;)')
  if 'whats up' in message.content.lower():
    await message.channel.send('The sky ;)')
  if 'wassup' in message.content.lower():
    await message.channel.send('The sky ;)')


keep_alive()
client.run(os.getenv('TOKEN'))
