import discord
from discord.ext import commands
import json
from random import randint
import datetime
import asyncio
import math
import os
import youtube_dl
from ffmpeg import *

client = commands.Bot(command_prefix = "*") 
client.remove_command('help')

with open("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["TOKEN"]

@client.event
async def on_ready():
    print('Zalogowany')

@client.command()
async def help(ctx):
    embed=discord.Embed(title="*help", description="", color=0x0ba800)
    embed.add_field(name="Pod spodem masz linka do komend!", value="https://clamsbot.cf/commands.html", inline=True)
    await ctx.send(embed=embed)        
    print(str (ctx.author)+ ' wywolal komende help'),


#kostka
@client.command()
async def kostka(ctx):
    message = await ctx.send("Rzucam... :game_die:")
    await asyncio.sleep(1)
    roll = randint(1, 6)
    str(roll)
    await message.delete()
    await ctx.send(f"Liczba na kostce to {roll}")

@client.command()
async def wonz(ctx):
    await ctx.send("wonsz rzeczny")
    asyncio.sleep(1)
    await ctx.send("tututu")
    asyncio.sleep(1)
    await ctx.send("jest niebezpieczny")

@client.command()
async def dzien(ctx):
    dayNumber = datetime.datetime.today().weekday()
    if dayNumber == 0:
        weekday = 'Poniedzialek'
        await ctx.send(weekday+' ')
    elif dayNumber == 1:
        weekday = 'Wtorek'
        await ctx.send(weekday)
    elif dayNumber == 2:
        weekday = 'Sroda'
        await ctx.send(weekday)
    elif dayNumber == 3:
        weekday = 'Czwartek'
        await ctx.send(weekday)
    elif dayNumber == 4:
        weekday = 'Piatek'
        await ctx.send(weekday)
    elif dayNumber == 5:
        weekday = 'Sobota'
        await ctx.send(weekday)
    elif dayNumber == 6:
        weekday = 'Niedziela'
        await ctx.send(weekday)

@client.command()
async def omnie(ctx):
    embed=discord.Embed(title="*omnie", description="Witam, Nazywam sie Clams", color=0x0ba800)
    embed.add_field(name=" jestem botem zaprogramowanym przez czaro#3107, służę do komend 4fun i zabawy!", value="Jeśli potrzebujesz pomocy związanej z botem, napisz do właściciela!", inline=True)
    await ctx.send(embed=embed)
    await print(str (ctx.author)+ "uzyl komendy *omnie")
    

@client.command()
async def ping(ctx):
    pong = await ctx.send("Pong! 🏓")
    await asyncio.sleep(0.5)
    await pong.delete()
    ClamsPing = client.latency * 1000
    await ctx.send(f'***Mój ping to: {math.floor(ClamsPing*100)/100}ms!*** :smile:')
    
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='muzyka')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio',
        'default_search': 'auto',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

 
client.run(TOKEN)