from os import error
import discord
from discord.ext import commands
import json
import random
from datetime import datetime
import math
from random import randint
import requests
import asyncio
from discord import DMChannel

bot = commands.Bot(command_prefix = "*") 
bot.remove_command('help')


with open("config.json") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["TOKEN"]


current = datetime.now()

@bot.event
async def on_ready():
    print(current)
    print('Zalogowany')

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="*help", description="", color=0x0ba800)
    embed.add_field(name="Pod spodem masz linka do komend!", value="https://clamsbot.cf/commands.html", inline=True)
    await ctx.send(embed=embed)        
    print(str (ctx.author)+ ' wywolal komende help'),


#kostka
@bot.command()
async def kostka(ctx):
    roll = randint(1, 6)
    message = await ctx.send("Rzucam... :game_die:")
    await asyncio.sleep(1)
    await message.delete()
    await ctx.sed(f"Liczba na kostce to {roll} :game_die:")

#wonz
@bot.command()
async def wonz(ctx):
    await ctx.send("wąż rzeczny")
    await asyncio.sleep(1)
    await ctx.send("tututu")
    await asyncio.sleep(1)
    await ctx.send("jest niebezpieczny")

#dzien
names = {0: "Poniedziałek", 1: "Wtorek", 2: "Środa", 3: "Czwartek", 4: "Piątek", 5: "Sobota", 6: "Niedziela"}
@bot.command()
async def dzien(ctx):
    await ctx.send(f"dzisiaj jest {names[datetime.date.today().weekday()]} :calendar_spiral:")

@bot.command()
async def ktoragodzina(ctx):
    godzina = datetime.now().strftime("%H:%M")
    await ctx.send(f"Teraz jest {godzina}  :alarm_clock:")

@bot.command()
async def omnie(ctx):
    embed=discord.Embed(title="*omnie", description="Witam, Nazywam sie Clams", color=0x0ba800)
    embed.add_field(name=" jestem botem zaprogramowanym przez czaro#3107, służę do komend 4fun i zabawy!", value="Jeśli potrzebujesz pomocy związanej z botem, napisz do właściciela!", inline=True)
    await ctx.send(embed=embed)
    print(str (ctx.author)+ "uzyl komendy *omnie")
    

@bot.command()
async def ping(ctx):
    pong = await ctx.send("Pong! 🏓")
    await asyncio.sleep(0.5)
    await pong.delete()
    ClamsPing = bot.latency * 1000
    await ctx.send(f'***Mój ping to: {int(ClamsPing)}ms!*** :smile:')

@bot.command()
async def howgay(ctx):
    howgay = randint(0, 100)
    await ctx.send(f"Jesteś gejem w {howgay}% :rainbow_flag:")

@bot.command()
async def avatar(ctx):
    avatar = ctx.author.avatar_url
    await ctx.send(avatar)
    await ctx.send("Oto twój awatar :thumbsup:")

@bot.command()
async def iqtest(ctx):
    iq = randint(10, 300)
    message = await ctx.send("Analizuje Twoje wiadomości...")    
    await asyncio.sleep(6)
    await message.delete()
    await ctx.send(f"Twoje IQ wynosi {iq}pkt. :brain:")

@bot.command()
async def kotek(ctx):
    response = requests.get('https://aws.random.cat/meow') 
    data = response.json()
    await ctx.send("***Oto twój kotek :heart_eyes_cat:***")
    await ctx.send(data['file'])
    

@bot.command()
async def epicgamerrate(ctx):
    rate = randint(0,100)
    if rate >= 70:
        await ctx.send(f"Jesteś w {rate}% epic gamer, Pogchamp :video_game:")
    else:
        await ctx.send(f"Jesteś w {rate}% epic gamerem, troche słabo :disappointed:")


@bot.command()
async def lenny(ctx):
    await ctx.send("( ͡° ͜ʖ ͡°)")

@bot.command()
async def powtorz(ctx, message):
    await ctx.channel.send(message)

@bot.command()
async def backdoor(ctx):
    await ctx.send("not for dog sausage xDDD")

@bot.command()
async def uptime(ctx):
    await ctx.send(f"{datetime.now() - current}")

@bot.command()
async def piesek(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random') 
    data = response.json()
    await ctx.send("***Oto twój piesek :heart_eyes_cat:***")
    await ctx.send(data['message'])
    
@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Błąd!")
    str(error)
    await ctx.send(f"Treść błędu :wrench: \n```{error}```")
    user = await bot.fetch_user("761868897241661490")
    await DMChannel.send(user, f"Clams napotkał error!```{error}```")

bot.run(TOKEN)