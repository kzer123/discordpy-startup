# -*- coding: utf-8 -*-

import discord
import os
from datetime import datetime, timedelta

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 665898689302233129 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(684472113150689281)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg) 
 
client.run(token)
