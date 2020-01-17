import os

os.system('')

Colors = {
'TextRed' : '\033[91m',
'TextGreen' : '\033[92m',
'TextYellow' : '\033[93m',
'TextBlue' : '\033[94m',
'TextWhite' : '\033[97m',
'TextEnd' : '\033[0m',
'BgRed' : '\033[7;91m',
'BgGreen' : '\033[7;92m',
'BgYellow' : '\033[7;93m',
'BgBlue' : '\033[7;94m',
'BgWhile' : '\033[7;97m',
}

# print('\033[0;97;46m123',TextEnd)
for color in Colors:
    print(Colors[color],'123',Colors['TextEnd'])