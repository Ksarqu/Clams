import discord
import json
import requests
from asyncio import sleep
from discord.ext import commands
from datetime import datetime
from random import randint, choice
from google_trans_new import google_translator

bot = commands.Bot(command_prefix="*")
bot.remove_command('help')

with open("config.json") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["TOKEN"]


@bot.event
async def on_ready():
    print('Zalogowany')


@bot.command(name="help")
async def show_help(ctx):
    embed = discord.Embed(title="*help", description="", color=0x0ba800)
    embed.add_field(name="Pod spodem masz linka do komend!", value="https://clamsbot.cf/commands.html", inline=True)
    await ctx.send(embed=embed)
    print(str(ctx.author) + ' wywolal komende help'),


# kostka
@bot.command()
async def kostka(ctx):
    roll = randint(1, 6)
    message = await ctx.send("Rzucam... :game_die:")
    await sleep(1)
    await message.delete()
    await ctx.sed(f"Liczba na kostce to {roll} :game_die:")


# wonz
@bot.command()
async def wonz(ctx):
    await ctx.send("w膮偶 rzeczny")
    await sleep(1)
    await ctx.send("tututu")
    await sleep(1)
    await ctx.send("jest niebezpieczny")


# dzien
names = {0: "Poniedzia艂ek", 1: "Wtorek", 2: "艢roda", 3: "Czwartek", 4: "Pi膮tek", 5: "Sobota", 6: "Niedziela"}


@bot.command()
async def dzien(ctx):
    await ctx.send(f"dzisiaj jest {names[datetime.date.today().weekday()]} :calendar_spiral:")


@bot.command()
async def ktoragodzina(ctx):
    godzina = datetime.now().strftime("%H:%M")
    await ctx.send(f"Teraz jest {godzina}  :alarm_clock:")


@bot.command()
async def omnie(ctx):
    embed = discord.Embed(title="*omnie", description="Witam, Nazywam sie Clams", color=0x0ba800)
    embed.add_field(name=" jestem botem zaprogramowanym przez czaro#3107, s艂u偶臋 do komend 4fun i zabawy!",
                    value="Je艣li potrzebujesz pomocy zwi膮zanej z botem, napisz do w艂a艣ciciela!", inline=True)
    await ctx.send(embed=embed)
    print(str(ctx.author) + "uzyl komendy *omnie")


@bot.command()
async def ping(ctx):
    pong = await ctx.send("Pong! 馃彄")
    await sleep(0.5)
    await pong.delete()
    clams_ping = bot.latency * 1000
    await ctx.send(f'***M贸j ping to: {int(clams_ping)}ms!*** :smile:')


@bot.command()
async def howgay(ctx):
    how_gay = randint(0, 100)
    await ctx.send(f"Jeste艣 gejem w {how_gay}% :rainbow_flag:")


@bot.command()
async def avatar(ctx):
    picture = ctx.author.avatar_url
    await ctx.send(picture)
    await ctx.send("Oto tw贸j awatar :thumbsup:")


@bot.command()
async def iqtest(ctx):
    iq = randint(10, 300)
    message = await ctx.send("Analizuje Twoje wiadomo艣ci...")
    await sleep(6)
    await message.delete()
    await ctx.send(f"Twoje IQ wynosi {iq}pkt. :brain:")


@bot.command()
async def kotek(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await ctx.send("***Oto tw贸j kotek :heart_eyes_cat:***")
    await ctx.send(data['file'])


@bot.command()
async def epicgamerrate(ctx):
    rate = randint(0, 100)
    if rate >= 70:
        await ctx.send(f"Jeste艣 w {rate}% epic gamer, Pogchamp :video_game:")
    else:
        await ctx.send(f"Jeste艣 w {rate}% epic gamerem, troche s艂abo :disappointed:")


@bot.command()
async def lenny(ctx):
    await ctx.send("( 汀掳 蜏蕱 汀掳)")


@bot.command()
async def powtorz(ctx, *, message):
    await ctx.channel.send(message)


@bot.command()
async def backdoor(ctx):
    await ctx.send("not for dog sausage xDDD")


@bot.command()
async def piesek(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await ctx.send("***Oto tw贸j piesek :heart_eyes_cat:***")
    await ctx.send(data['message'])


@bot.command()
async def cytat(ctx):
    site = "https://www.affirmations.dev/"
    g_translator = google_translator()
    get_value = requests.get(site).json()
    text_value = get_value['affirmation']
    translate_text = g_translator.translate(text_value, lang_tgt='pl')
    await ctx.send(f"{translate_text[:-1]}.")


@bot.command(aliases=["trans", "translate"])
async def translator(ctx, message, language='en'):
    g_translator = google_translator()
    translate = g_translator.translate(message, lang_tgt=language)
    await ctx.send(translate)


@bot.command(aliases=["kula", "magiczna"])
async def magicznakula(ctx):
    m = await ctx.send("Pocieram magiczn膮 kul臋... :magic_wand:")
    await sleep(2)
    answer = choice([
        "powiniene艣 to zrobi膰",
        "musisz to zrobi膰",
        "nie r贸b tego",
        "wypada艂o by to zrobi膰",
        "nie polecam tego robi膰"])
    await m.edit(content=f"Magiczna kula m贸wi: {answer} :crystal_ball: ")


@bot.command()
async def hack(ctx, member):
    m = await ctx.send(f"robi sie szefie :D hakujemy pana {member}")
    await sleep(1)
    await m.edit(content=f"Wyszukujemy lokalizacje...")
    await sleep(0.6)
    city = choice([
        "Bydgoszczy!",
        "Wroc艂awiu",
        "Warszawie!",
        "艁odzi!",
        "艢l膮sku!"]
    )
    await m.edit(content=f"U偶ytkownik mieszka w {city}")
    await sleep(4)
    await m.edit(content="Zamawianie 10 ton w臋gla za pobraniem...")
    await sleep(4)
    await m.edit(content="Zam贸wione! Sprawdzanie IP oraz hackowanie API Discord aby zdoby膰 dane personalne...")
    await sleep(4)
    await m.edit(content="Dane Wys艂ane w wiadomo艣ci prywatnej!")
    await sleep(4)
    await m.edit(content="Doxowanie informacji na wykopie zosta艂o uko艅czone!")
    await sleep(4)
    await m.edit(content="Hacked :call_me:")


@bot.event
async def on_command_error(ctx, error):
    await ctx.send("B艂膮d!")
    await ctx.send(f"Tre艣膰 b艂臋du :wrench: \n```{error}```")
    user = await bot.fetch_user(761868897241661490)
    await user.send(f"Clams napotka艂 error!\n```{error}```")

bot.run(TOKEN)
