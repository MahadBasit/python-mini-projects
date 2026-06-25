from pyfiglet import Figlet
import requests

figlet = Figlet()
figlet.setFont(font = 'digital')

try:
    response = requests.get('https://api.chucknorris.io/jokes/random')
    o = response.json()
    s = o['value']
    print(figlet.renderText(s))


except requests.RequestException:
    print("Error")