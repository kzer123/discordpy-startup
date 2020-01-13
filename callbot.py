# -*- coding: utf-8 -*-

import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 665898689302233129 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(666246704668082186)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg) 
 
client.run("NjY2MTcxNjY2MDU3MDAzMDE5.XhwdNQ.ua8IV6TATMVeV-XO1ZZCACtuI2I")