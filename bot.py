import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import invert
from random import choice
from bot_logic import get_duck_image_url
import nacl
import youtube_dl
import os
import requests 
from random import choice



password_help = '!password (lenght)'
hello_help = '!hello'
bye_help = '!bye'
heh_help = '!heh (lenght)'
inv_help = '!inv (text)'
eco_help1 = '!ecology'
eco_help2 = '!ecology2'
eco_help3 = '!ecology3 (type)'
item = ''
print(os.listdir('images'))

file_path = "deutch.mp3"
full_path = os.path.abspath(file_path)
print(full_path)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    
@bot.command()
async def password(ctx, pass_lenght = 10):
    await ctx.send(gen_pass(pass_lenght))
    
@bot.command() 
async def bye(ctx):
    await ctx.send(f'Пока {client.user}!')
    
@bot.command() 
async def inv(ctx, text):
    await ctx.send(invert(text))

@bot.command() 
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ran_mem(ctx):
    ran_mem = choice(os.listdir('images'))
    with open(f'images/{ran_mem}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 
           
@bot.command()
async def help_mes(ctx):
    help_text = f"{password_help}\n{hello_help}\n{bye_help}\n{heh_help}\n{inv_help}\n{eco_help1}\n{eco_help2}\n{eco_help3}"
    await ctx.send(help_text)
    
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
    
    
    
    
    
    
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
    
    
@bot.command()
async def play(ctx, file_path = full_path):
    if not ctx.voice_client:
        await ctx.invoke(join)

    source = discord.FFmpegPCMAudio(file_path)
    ctx.voice_client.play(source)
    
@bot.command()
async def pause(ctx):
    ctx.voice_client.pause()
    
@bot.command()
async def resume(ctx):
    ctx.voice_client.resume()
    
@bot.command()
async def stop(ctx):
    ctx.voice_client.stop()
    
    
    
    
    
    
    



@bot.command()
async def ecology(ctx):
    await ctx.send('https://youtu.be/SYANKsRfNdU?si=AW_eylgYCxu76hnZ')
    
@bot.command()
async def ecology2(ctx):
    await ctx.send('''
                   \n1 Сортировка на месте: Для начала процесса переработки мусор сортируется на месте сбора. 
                   Люди могут разделять мусор на разные контейнеры для бумаги, пластика, стекла и металла. 
                   Это позволяет легко перерабатывать отходы и уменьшать загрязнение.\n 
                   2 Переработка бумаги: Собранная бумага перерабатывается, превращая ее в новую бумагу. 
                   Это способствует сохранению лесов и уменьшению вырубки деревьев.\n 
                   3 Переработка стекла: Стекло может быть рафинировано и использовано для производства 
                   новых стеклянных изделий.\n 
                   4 Переработка пластика: Пластик можно переплавить и использовать 
                   для создания новых пластиковых продуктов. Это позволяет сократить использование нефти для 
                   производства пластика.\n 
                   5 Мусоросжигание: Мусоросжигательные заводы сжигают отходы с высокой температурой, 
                   чтобы производить энергию. Это может быть полезным для выработки электроэнергии.\n 
                   6 Утилизация опасных отходов: Опасные отходы, такие как химические вещества и медицинские отходы, 
                   должны быть обработаны специализированными методами для предотвращения загрязнения окружающей среды.\n 
                   7 Повторное использование: Другой способ уменьшения мусора - это внимательное использование товаров, 
                   а также переработка их для повторного использования, например, путем ремонта или перепродажи.\n 
                   ''')

@bot.command()
async def ecology3(ctx,item = 'пластик'):
    if item == 'пластик':
        await ctx.send('''\n1 Соберите пластиковые изделия.\n
                       2 Очистите их от остатков пищи или жидкостей.\n
                       3 Удалите неперерабатываемые части например, крышки и этикетки.\n
                       4 Сортируйте пластик по типу если возможно.\n
                       5 По возможности, сжимайте или разбирайте пластик, чтобы сократить объем.\n
                       6 Сдайте пластик в местный пункт сбора или контейнер для переработки.''')
    if item == 'бумага':
        await ctx.send('''\n1 Соберите бумагу для переработки.\n
                        2 Убедитесь, что бумага чиста от любых остатков пищи или жидкостей.\n
                        3 Удалите неперерабатываемые материалы, такие как металлические скрепки или пластиковые окончания ручек.\n
                        4 Если бумага сильно загрязнена или имеет пластиковые покрытия, возможно, она не пригодна для переработки\n
                        5 в домашних условиях. Лучше отправить ее в специализированный пункт сбора.\n
                        6 Положите подготовленную бумагу в контейнер для переработки бумаги или сдайте ее в местный пункт сбора.''')
    if item == 'стекло':
        await ctx.send('''\n1 Соберите стекло для переработки, такие как бутылки или стеклянные контейнеры.\n
                        2 Очистите стекло от остатков напитков или еды.\n
                        3 Удалите неперерабатываемые материалы, такие как металлические крышки.\n
                        4 Если стекло разбито, не пытайтесь его склеивать или очищать. Опасайтесь осколков и безопасно утилизируйте их.\n
                        5 Положите подготовленное стекло в контейнер для переработки стекла или сдайте его в местный пункт сбора стекла.''')







    

bot.run("token")
