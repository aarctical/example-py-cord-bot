import discord
import json

with open('configuration.json') as cfg:
    config = json.load(cfg)

def GetActivity():
    tmp = config['activity-type']
    if tmp == "watching":
        activity = discord.Activity(type=discord.ActivityType.watching, name=config['activity-data'])
    elif tmp == "listening":
        activity = discord.Activity(type=discord.ActivityType.listening, name=config['activity-data'])
    elif tmp == "playing":
        activity = discord.Activity(type=discord.ActivityType.playing, name=config['activity-data'])
    elif tmp == "competing":
        activity = discord.Activity(type=discord.ActivityType.competing, name=config['activity-data'])
    elif tmp == "streaming":
        activity = discord.Activity(type=discord.ActivityType.streaming, name=config['activity-data'])
    else:
        print("Invalid Activity type (listening/watching/playing/streaming/competing)... Terminating program.")
        quit()
    return activity

def GetStatus():
    tmp = config['status']
    if tmp == "dnd":
        status = discord.Status.dnd
    elif tmp == "idle":
        status = discord.Status.idle
    elif tmp == "online":
        status = discord.Status.online
    elif tmp == "invisible":
        status = discord.Status.invisible
    elif tmp == "offline":
        status = discord.Status.offline
    elif tmp == "streaming":
        status = discord.Status.streaming
    else:
        print("Invalid Status type (dnd/idle/offline/online/streaming)... Terminating program.")
        quit()
    return status