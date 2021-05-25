import discord
from discord.ext import commands
import colorama 
import os
from colorama import Fore
client = commands.Bot(command_prefix = 'a niglet', help_command = None)
# this made me attract 100 gurls at my door 

colorama.init()
token = input("Input Token>>")
@client.event
async def on_ready():
 os.system('cls')
 print(f'''
{Fore.MAGENTA} ██╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
{Fore.MAGENTA}████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
{Fore.MAGENTA}██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
{Fore.MAGENTA}██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
{Fore.MAGENTA}██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
{Fore.MAGENTA}╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝
{Fore.MAGENTA}                     By oAaron#0002              
{Fore.MAGENTA}                      [1] Mass Dm 
{Fore.MAGENTA}                      [2] Mass Friend [Soon]                                                 
''')
 fuck = input(f"{Fore.GREEN}Select>>")
 if fuck == '1':
  input2 = input(f"{Fore.GREEN}What Should I Send?>>")
  for user in client.user.friends:                
   await user.send(f"{input2}")
   print(f"{Fore.GREEN}[+] Sent{Fore.WHITE} {input2} To {user}")

client.run(token, bot = False)