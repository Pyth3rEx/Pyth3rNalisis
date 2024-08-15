#Imports
from pyfiglet import Figlet
from colorama import init
from colorama import Fore, Back, Style

#Functions
def printBanner (version): #Requires modules pyfiglet & colorama
    custom_fig = Figlet(font='ogre')
    print(Fore.GREEN + custom_fig.renderText('Pyth3rNalisis'))
    print('Pyth3rNalisis v' + str(version))
    print('Made by Pyth3rEx - https://pyth3rex.github.io')
    print('===============')
    print(Style.RESET_ALL)
    return