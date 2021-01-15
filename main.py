#!/.anyenv/envs/pyenv/shims/python
# -*- coding: utf-8 -*-

import discord

import apiKey

TOKEN = str(apiKey.TOKEN)

client = discord.Client()

# Unicode絵文字(https://emojipedia.org/)
banana = "🍌"
sweate_drops = "\N{Splashing Sweat Symbol}"

@client.event
async def on_message(message):
  # 発言した特定の人物
  a_person = 627535204164173824

  # 送信者がBotの場合は反応しない
  if message.author.bot:
      return
  # 特定の人が発言した時、リアクションをつける
  if message.author.id == a_person:
    await message.add_reaction(banana)
    await message.add_reaction(sweate_drops)
  
client.run(TOKEN)

