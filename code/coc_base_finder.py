from argparse import ArgumentParser, Namespace
from utils import open_window, pyautogui, time, find_base_with

parser = ArgumentParser(description='Find a Clash of Clans base that meets your resource criteria.')
parser.add_argument('gold', metavar='gold', type=int, help='The minimum amount of gold you want a base to have.')
parser.add_argument('elixir', metavar='elixir', type=int, help='The minimum amount of elixir you want a base to have.')
parser.add_argument('dark_elixir', metavar='dark_elixir', type=int, help='The minimum amount of dark elixir you want a base to have.')
parser.add_argument('attack', metavar='attack', type=bool, help='Whether you want to autoattack with giant barch or not. (True or False)')

args: Namespace = parser.parse_args()

gold = args.gold
elixir = args.elixir
dark_elixir = args.dark_elixir
auto_attack = args.attack

open_window("Clash of Clans")
criteria_found = False
print("Starting attack...")
pyautogui.click(x=200, y=1000)
time.sleep(1)
pyautogui.click(x=1350, y=700)
while not criteria_found:
    print("Finding next base...")
    criteria_found = find_base_with(gold, elixir, dark_elixir)
    if criteria_found:
        print("Village that matches criteria found!")
    else:
        pyautogui.click(x=1700, y=850)

if (auto_attack):
    auto_attack
