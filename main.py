#Die Discord-Klasse Verwenden (Discord.py)
from multiprocessing.connection import wait
import discord
from discord.ext import commands

#Random Klasse für die random()-Funktion
import random

#Eigene Klassen Importieren
import xmlParse 
import translate

#Alle Intents Einbinden und Bot-Erstellen
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='>')

#OnReady Message im Terminal
@bot.event
async def on_ready():
    print(f'BotID: {bot.user.id} - Name: {bot.user.name}')

#SUS Antwort auf :sus: reaction
@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return
    if payload.emoji.name == 'sus':
        channel: discord.TextChannel = bot.get_channel(payload.channel_id)
        await channel.send(' <:sus:801890994869895199> SUS <:sus:801890994869895199> ')
        print('SUS-Reaction')

#Ping-Command
@bot.command(name='ping')
async def ping(ctx, *, arg):
    await ctx.send('pong '+ arg)

@bot.command(name='echo')
async def _echo(ctx, *, arg):
    await ctx.send(arg)

@bot.command(name='announce')
async def _announce(ctx, *, arg):
    await ctx.send(':bell: :bell: :bell:')
    await ctx.send(f'**{arg}** @everyone')
    await ctx.send(':bell: :bell: :bell:')
    await ctx.message.delete()

@bot.command(aliases=['wähle', 'Wähle', 'choose', 'Choose'])
async def _wahle(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(aliases=['geld','Geld','money','Money','€','$'])
async def _geld(ctx, member: discord.Member = None):
    """Returns the Money Integer for the member from the save.xml"""

    #Wenn kein member angegeben wurde (ist member=None) dann wird der Autor als member benutzt
    #AKA: wenn du keinen anderen meinst, dann dich selber
    if member == None:
        member = ctx.author
    
    #Geld wird vom user aus der XMl geladen
    Geld : int = xmlParse.user_get_Geld(str(member.id))

    #Wenn Geld = None ist, dann gibt es den User noch nicht, und er wird erstellt
    if Geld == None:
        xmlParse.user_new(str(member.id))
        Geld = 0

    #Geld wird vorgelesen
    await ctx.send(f'{member.mention} hat {Geld}€')

@bot.command(aliases=['Einkommen', '$add', 'Einnahmne'])
async def _income(ctx, amountIN, member: discord.Member = None, *, reason = None):
    """"""
    #
     #Wenn kein member angegeben wurde (ist member=None) dann wird der Autor als member benutzt
    #AKA: wenn du keinen anderen meinst, dann dich selber
    if member == None:
        member = ctx.author

    try:
        amount:int = int(amountIN)
    except:
        return

    if amount <= 0:
        return

    newAmount = xmlParse.user_add_Geld(str(member.id),amount)
    await ctx.send(f'{member.mention} hat jetzt {newAmount}€')

@bot.command(aliases=['Ausgabe', '$remove' , 'Strafe'])
async def _expense(ctx, amountIN, member: discord.Member = None, *, reason = None):
    """"""
    #
     #Wenn kein member angegeben wurde (ist member=None) dann wird der Autor als member benutzt
    #AKA: wenn du keinen anderen meinst, dann dich selber
    if member == None:
        member = ctx.author

    try:
        amount:int = int(amountIN)
    except:
        return
    
    amount *= -1

    if amount >= 0:
        return

    newAmount = xmlParse.user_add_Geld(str(member.id),amount)
    await ctx.send(f'{member.mention} hat jetzt {newAmount}€')
    
@bot.command(aliases=['ToDoAdd'])
async def _ToDoAdd(ctx, *, arg):

    xmlParse.ToDo_add_entry(arg)
    await ctx.send(f'"{arg}" wurde der ToDo liste Hinzugefügt')

@bot.command(aliases=['ToDo'])
async def _ToDoDisplay(ctx):

    listcontent = xmlParse.ToDo_get()

    if len(listcontent) == 0 :
        Sendout = "ToDo-Liste ist Leer!"
    else:
        Sendout = "In der ToDo-Liste steht: \n"

        for x in listcontent:
            Sendout += f'{x} \n'

    await ctx.send(Sendout)

@bot.command(aliases=['ToDoClear'])
async def _ToDoClear(ctx):
    xmlParse.ToDo_Clear()
    await ctx.send('Die ToDo-Liste wurde gelöscht!')

@bot.command(aliases=['über', 'Über', 'übersetzten', 'Übersetzen', 'Trans', 'Translate'])
async def _Translate(ctx, toTranslate, LangCode='en'):
    await ctx.send(translate.translateTo(toTranslate, LangCode))

@bot.command(aliases=['Sprachen','sprachen','Languages','languages'])
async def _langs(ctx):
    await ctx.message.delete()
    await ctx.author.send(translate.Languages())

#Antworten auf String-vorkommen in Nachrichten
@bot.event
async def on_message(message):

    #Zuerst werden die Commands vom bot ausgeführt
    await bot.process_commands(message)

    #Wenn der Author ein Bot ist, wird die Nachricht ignoriert
    if message.author.bot:
        return
    
    #Der Text wird aus der Nachricht genommen und kompletzt ins lowercase gebracht
    text = message.content 
    lowtext = ' ' + text.lower()
    
    #Der Channel wird sich zum senden in der Zunkunft gemerkt
    channel = message.channel

    #überprüfen , ob keywords in der Nachricht vorkommen
    if 'sus' in lowtext:
        await channel.send ('<:sus:801890994869895199> SUS')
    elif 'katze' in lowtext or 'kadse' in lowtext:
        await channel.send ('Kadse <:Catluv:838495070130536468>')
    elif 'jonas' in lowtext:
        await channel.send ('Jonas du Sinkst')    
    elif 'focus' in lowtext or 'fokus' in lowtext:
        await channel.send ('Ich hab in den Focus gekaggert :)')
    elif 'xd' in lowtext or 'lol' in lowtext:
        await channel.send ('XDDDDDD') 
    elif 'ez' in lowtext or 'easy' in lowtext or 'gg' in lowtext:
        await channel.send ('GG EZ')
    elif 'moin' in lowtext or 'hallo' in lowtext:
        await channel.send ('Moin!')  
    elif ' ben' in lowtext or 'knecht' in lowtext:
        await channel.send ('Knecht 💀')
    elif 'fortnite' in lowtext:
        await channel.send ('FORTNITE')
        await channel.send ('https://tenor.com/view/fortnite-snake-eyes-orange-justice-dancing-dance-gif-22082452')
    elif 'ente' in lowtext or 'duck' in lowtext:
        await channel.send('https://cdn.discordapp.com/attachments/933129013185085530/971433609292550214/unknown.png')
        #await channel.send('https://cdn.discordapp.com/attachments/933129013185085530/971434786482688071/unknown.png')
    #elif 'amelie' in lowtext or 'finn' in lowtext:
    #    await channel.send('https://cdn.discordapp.com/attachments/789562687054413836/964913032692117514/unknown.png')
    

#Token wird aus der token.xml genommen und eingefügt
token = xmlParse.getToken()
bot.run(token)