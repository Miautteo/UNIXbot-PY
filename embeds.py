import discord

from discord.ext import commands

def embed_Help(_authorName, _authorIcoURL, _prefix: str):
    p = _prefix
    embed = discord.Embed(title = "Alle Befehle", description = f'Alle Befehle dieses Bots. Das Prefix ist "{_prefix}".', color=discord.Color.blue())
    embed.set_author(name = _authorName, icon_url = _authorIcoURL)
    embed.add_field(name = 'Standartbefehle', value = f'**{p}Hilfe** -> Zeigt diesen Dialog an.\n**{p}announce _Nachricht_** -> Nimmt deine Nachricht und gibt sie laut wieder.\n**{p}Wähle _<Option1>_ _<Option2>_ ...**  -> Wählt aus den gegebenen Optionen aus.\n**{p}ToDo** -> Gibt die ToDo-Liste aus.\n**{p}ToDoAdd _<ToDo>_** -> Fügt das gegebene ToDo der ToDo-Liste hinzu.', inline=False)
    embed.add_field(name = 'Befehle Für Geld', value = f'**{p}Geld _<User>_** -> Gibt den Kontostand des Nutzers an.\n**{p}Einkommen _<Amount>_ _[User]_ _[Grund]_** -> Der user gewinnt _Amount_ an Geld.\n**{p}Ausgabe _<Amount>_ _[User]_ _[Grund]_** -> Der user verliert _Amount_ an Geld.', inline=False)
    embed.add_field(name = 'Reaktionen',value = f'Wenn eines dieser Wörter in deinen Nachrichten erkannt wird, fogt die entsprechende Reaktion vom Bot.\n"sus" -> "SUS"\n"katze"/"kadse" -> "Kadse"\n"jonas" -> "Jonas du Stinkst!"\n"Moin"/"Hallo" -> "Moin!"\n**Es gibt noch weitere Versteckte Reaktionen**', inline=False)
    return embed