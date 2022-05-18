
def _getReaction(_messageText):
    #Der Text wird aus der Nachricht genommen und kompletzt ins lowercase gebracht
    lowtext = ' ' + _messageText.lower()
    
    #überprüfen , ob keywords in der Nachricht vorkommen
    if 'sus' in lowtext:
        return('<:sus:801890994869895199> SUS')
    elif 'katze' in lowtext or 'kadse' in lowtext:
        return('Kadse <:Catluv:838495070130536468>')
    elif 'jonas' in lowtext:
        return('Jonas du Sinkst')    
    elif 'focus' in lowtext or 'fokus' in lowtext:
        return('Ich hab in den Focus gekaggert :)')
    elif 'xd' in lowtext or 'lol' in lowtext:
        return('XDDDDDD') 
    elif 'ez' in lowtext or 'easy' in lowtext or 'gg' in lowtext:
        return('GG EZ')
    elif 'moin' in lowtext or 'hallo' in lowtext:
        return('Moin!')  
    elif ' ben' in lowtext or 'knecht' in lowtext:
        return('Knecht 💀')
    elif 'fortnite' in lowtext:
        return('FORTNITE')
        return('https://tenor.com/view/fortnite-snake-eyes-orange-justice-dancing-dance-gif-22082452')
    elif 'ente' in lowtext or 'duck' in lowtext:
        return('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Mallard_male_female.jpg/580px-Mallard_male_female.jpg')
    elif 'ass' in lowtext or 'booty' in lowtext or 'arsch' in lowtext or 'popo' in lowtext:
            return('booty hypnotic make you want more')
    elif 'banana' in lowtext or 'banane' in lowtext:
        return(':banana:')
        #return('https://cdn.discordapp.com/attachments/933129013185085530/971434786482688071/unknown.png')
    #elif 'amelie' in lowtext or 'finn' in lowtext:
    #    return('https://cdn.discordapp.com/attachments/789562687054413836/964913032692117514/unknown.png')
    