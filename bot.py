import discord
from discord.ext import commands
import json
import random
import datetime
import math

bot = commands.Bot(command_prefix = "*") 
bot.remove_command('help')


with open("./config.json") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["TOKEN"]

@bot.event
async def on_ready():
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
    message = await ctx.send("Rzucam... :game_die:")
    await asyncio.sleep(1)
    roll = randint(1, 6)
    str(roll)
    await message.delete()
    await ctx.send(f"Liczba na kostce to {roll}")

@bot.command()
async def wonz(ctx):
    await ctx.send("wąż rzeczny")
    asyncio.sleep(1)
    await ctx.send("tututu")
    asyncio.sleep(1)
    await ctx.send("jest niebezpieczny")

names = {0: "Poniedziałek", 1: "Wtorek", 2: "Środa", 3: "Czwartek", 4: "Piątek", 5: "Sobota", 6: "Niedziela"}
@bot.command()
async def dzien(ctx):
    await ctx.send(names[datetime.date.today().weekday()])

@bot.command()
async def omnie(ctx):
    embed=discord.Embed(title="*omnie", description="Witam, Nazywam sie Clams", color=0x0ba800)
    embed.add_field(name=" jestem botem zaprogramowanym przez czaro#3107, służę do komend 4fun i zabawy!", value="Jeśli potrzebujesz pomocy związanej z botem, napisz do właściciela!", inline=True)
    await ctx.send(embed=embed)
    await print(str (ctx.author)+ "uzyl komendy *omnie")
    

@bot.command()
async def ping(ctx):
    pong = await ctx.send("Pong! 🏓")
    await asyncio.sleep(0.2)
    await pong.delete()
    ClamsPing = bot.latency * 1000
    await ctx.send(f'***Mój ping to: {math.floor(ClamsPing*100)/100}ms!*** :smile:')
 

bot.run(TOKEN)