import discord

from discord.ext import commands

def embed_Help(_prefix: str):
    p=_prefix
    embed = discord.Embed(title="Alle Befehle", description=f'Alle Befehle dieses Bots, das Prefix ist "{_prefix}".', color=discord.Color.blue())
    embed.add_field(name='Standartbefehle', value=f'{p}Hilfe -> Zeigt diesen Dialog an.\n{p}announce **Nachricht** -> Nimmt deine Nachricht und gibt sie laut wieder.\n{p}Wähle **Option1**, **Option2**  -> Wählt aus den gegebenen Optionen aus.\n{p}ToDo -> Gibt die ToDo-Liste aus.\n{p}ToDoAdd **ToDo** -> Fügt das gegebene ToDo der ToDo-Liste hinzu.', inline=False)
    embed.add_field(name='Befehle Für Geld', value=f'{p}Geld **User** -> Gibt den Kontostand des Nutzers an.\n{p}Einkommen **Amount** **User** -> Der user gewinnt **Amount** an Geld.\n{p}Ausgabe **Amount** **User** -> Der user verliert **Amount** an Geld.', inline=False)
    embed.add_field(name='Reaktionen',value=f'Wenn eines dieser Wörter in deinen Nachrichten erkannt wird, fogt die entsprechende Reaktion vom Bot.\n"sus" -> "SUS"\n"katze"/"kadse" -> "Kadse"\n"jonas" -> "Jonas du Stinkst!"\n"Moin"/"Hallo" -> "Moin!"\n**Es gibt noch weitere Versteckte Reaktionen**', inline=False)
    return embed