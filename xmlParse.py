import string
from traceback import format_exc
import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

def getToken():
    tree = ET.parse('token.xml')
    root = tree.getroot()
    token = root.text
    return token

def mak_usr(userID, usrName=''):
    """Erstellt einen Neuen Benutzer in der XML und speichert diese"""

    tree = ET.parse('save.xml')
    root = tree.getroot()

    newUsr = ET.Element("User")
    newUsr.set("id", str(userID))
    newUsr.text = usrName
    #newUsr = ET.fromstring(f'<User id="{usrID}">{usrName}</User>')
    root.append(newUsr)

    tree.write('save.xml')

def user_new(userID):
    """Erstellt einen neuen leeren User in der XML"""

    #Die XML-Datei wird in Variablen geladen
    tree = ET.parse('save.xml')
    root = tree.getroot()

    #Es wird ein neues User-Element erstellt und die Eigenschaften ID und Geld angefügt
    newUsr = ET.Element("User")
    newUsr.set("id", str(userID))
    newUsr.set("Geld", '0')

    #Der user wird der Root der XML angehangen
    root.append(newUsr)

    #Und der neue baum in der XML gespeichert
    tree.write('save.xml')
    

def user_get_Geld(userID):
    #Die XML-Datei wird in Variablen geladen
    tree = ET.parse('save.xml')
    root = tree.getroot()

    Geld:int=None

    for User in root.findall('User'):
        id = User.get('id')
        if id == userID:
            Geld=User.get('Geld')
    return Geld

def user_add_Geld(userID:str, amount:int):
    """"""
    tree = ET.parse('save.xml')
    root = tree.getroot()

    Geld:int = None
    User =None

    for UserSearch in root.findall('User'):
        id = UserSearch.get('id')
        if id == userID:
            GeldOld=UserSearch.get('Geld')
            User = UserSearch
    
    try:
        Geld:int = int(GeldOld)
    except:
        return
        
    Geld += amount

    User.set("Geld", f'{Geld}')

    tree.write('save.xml')

    return Geld

def ToDo_add_entry(Entry):
    """"""
    
    tree = ET.parse('save.xml')
    root = tree.getroot()

    ToDo = root.find('ToDo')
    newEntry = ET.Element("Entry")
    newEntry.set('Content', str(Entry))

    ToDo.append(newEntry)
    tree.write('save.xml')

def ToDo_get():
    tree = ET.parse('save.xml')
    root = tree.getroot()
    ToDo = root.find('ToDo')
    listcontent = list()
    for x in ToDo.findall('Entry'):
        listcontent.append(x.get('Content'))
    return listcontent

def ToDo_Clear():
    tree = ET.parse('save.xml')
    root = tree.getroot()
    ToDo = root.find('ToDo')

    for x in ToDo.findall('Entry'):
        ToDo.remove(x)

    tree.write('save.xml')