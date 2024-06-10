from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv)==1:
    a=input("Input:")
    font = random.choice(fonts)
    figlet.setFont(font=font)
    print(figlet.renderText(a))
    sys.exit(0)

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    font=sys.argv[2]
    if font not in fonts:
        sys.exit("Invalid font name")
    else:
        a=input("Input:")
        figlet.setFont(font=font)
        print(figlet.renderText(a))
        sys.exit(0)

else:
    sys.exit("Invalid usage")
