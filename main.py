#Die Discord-Klasse Verwenden (Discord.py)
from multiprocessing.connection import wait
import discord
from discord.ext import commands

#Random Klasse für die random()-Funktion
import random

#Eigene Klassen Importieren
import xmlParse 
import translate
import embeds as E
import reactions as R

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

@bot.command(aliases=['Help','hilfe','Hilfe','?'])
async def _help(ctx):
    embed = E.embed_Help(ctx.author.display_name, ctx.author.avatar_url, bot.command_prefix)
    await ctx.send(embed=embed)

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

        n = 0
        for x in listcontent:
            n+1
            Sendout += f'{n}.{x} \n'

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

    #Der Channel wird sich zum senden in der Zunkunft gemerkt
    channel = message.channel

    #Der Text wird aus der Nachricht genommen
    text = message.content 

    #Reaktion wird aus der Reaktionsliste geholt
    reaction = R._getReaction(text)

    #Reaktionsnachricht Senden
    await channel.send(reaction)
    

#Token wird aus der token.xml genommen und eingefügt
token = xmlParse.getToken()
bot.run(token)