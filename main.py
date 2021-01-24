#!/.anyenv/envs/pyenv/shims/python
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

import apiKey
import emoji_list_file

# Botのトークン
TOKEN = str(apiKey.TOKEN)
# 発言した特定の人物
MY = int(apiKey.MY)
UN = int(apiKey.UN)
AUTHOR = int(apiKey.AUTHOR)
DEBUG_CH = int(apiKey.DEBUG_CH)

client = discord.Client()
# bot = commands.Bot(command_prefix='$')

# Unicode絵文字(https://emojipedia.org/)
bananas = emoji_list_file.bananas
emoji_list = emoji_list_file.emoji_list

# for debug
ch = client.get_channel(DEBUG_CH)

print('サーバ起動 ...')
@client.event
async def on_message(message):
  # 送信者がBotの場合は反応しない
  if message.author.bot:
    return
  # 特定の人が発言した時、リアクションをつける
  if message.author.id == MY:
    for item in emoji_list:
      try:
        await message.add_reaction(item)
      except Exception as identifier:
        await ch.send('Raise exception by MY')

  elif message.author.id == UN:
    for item in bananas:
      try:
        await message.add_reaction(item)
      except Exception as identifier:
        await ch.send('Raise exception by UN')
  
client.run(TOKEN)

