from pycaw.pycaw import AudioUtilities
from pypresence import Presence, ActivityType
import threading
from colorama import Fore, Back, Style
import time
import os
import platform
import sys

bot_ID = "YOUR BOPT ID HERE"

banner = f"""{Fore.MAGENTA}

                     ▄████▄   █    ██   ██████ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓    ██▀███   ██▓███   ▄████▄  
                    ▒██▀ ▀█   ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒   ▓██ ▒ ██▒▓██░  ██▒▒██▀ ▀█  
                    ▒▓█    ▄ ▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░   ▓██ ░▄█ ▒▓██░ ██▓▒▒▓█    ▄ 
                    ▒▓▓▄ ▄██▒▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒██    ▒██    ▒██▀▀█▄  ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒
                    ▒ ▓███▀ ░▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒   ░██▓ ▒██▒▒██▒ ░  ░▒ ▓███▀ ░
                    ░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ░  ░   ░ ▒▓ ░▒▓░▒▓▒░ ░  ░░ ░▒ ▒  ░
                      ░  ▒   ░░▒░ ░ ░ ░ ░▒  ░ ░    ░      ░ ▒ ▒░ ░  ░      ░     ░▒ ░ ▒░░▒ ░       ░  ▒   
                    ░         ░░░ ░ ░ ░  ░  ░    ░      ░ ░ ░ ▒  ░      ░        ░░   ░ ░░       ░        
                    ░ ░         ░           ░               ░ ░         ░         ░              ░ ░      
                    ░                                                                            ░        
          {Style.RESET_ALL}                            
"""

rpc = None

bracketopen = f"{Fore.MAGENTA}[{Style.RESET_ALL}"
bracketclosed = f"{Fore.MAGENTA}]{Style.RESET_ALL}"

bracketopen2 = f"{Fore.WHITE}[{Style.RESET_ALL}"
bracketclosed2 = f"{Fore.WHITE}]{Style.RESET_ALL}"

username = os.getlogin()

is_windows = os.name == "nt"
system_text = "Windows" if is_windows else "Linux"
pc_name = platform.node()

def Slow(banner):
    delai = 0.03
    lignes = banner.split('\n')
    for ligne in lignes:
        print(ligne)
        time.sleep(delai)

def main():
 os.system("cls")
 Slow(banner)
 print("")
 time.sleep(0.05)
 print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Set custom RPC{Style.RESET_ALL}")
 time.sleep(0.05)
 print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Exit{Style.RESET_ALL}")
 time.sleep(0.05)
 print("")
 try:
  command = int(input(f"""{Fore.MAGENTA} ┌──({Fore.WHITE}{username}{Fore.MAGENTA})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.MAGENTA}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}"""))
 except Exception:
  main()
 def custom_rpc():
    os.system("cls")
    time.sleep(0.05)
    print(f"{bracketopen}!{bracketclosed} {Fore.MAGENTA}Custom discord RPC{Style.RESET_ALL}")
    print("")
    title_rpc = input(f"{bracketopen}>{bracketclosed} {Fore.MAGENTA}RPC title -> {Style.RESET_ALL}")
    if len(title_rpc) < 1:
      print("")
      print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Must be atleast 1 character long{Style.RESET_ALL}")
      time.sleep(2)
      custom_rpc()
    description_rpc = input(f"{bracketopen}>{bracketclosed} {Fore.MAGENTA}RPC description -> {Style.RESET_ALL}")
    if len(description_rpc) < 2:
      print("")
      print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Must be atleast 2 characters long{Style.RESET_ALL}")
      time.sleep(2)
      custom_rpc()
    print("")
    time.sleep(0.05)
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    time.sleep(0.05)
    print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Listening{Style.RESET_ALL}")
    time.sleep(0.05)
    print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Playing{Style.RESET_ALL}")
    time.sleep(0.05)
    print(f"{bracketopen}{Fore.WHITE}03{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Watching{Style.RESET_ALL}")
    time.sleep(0.05)
    print(f"{bracketopen}{Fore.WHITE}04{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Competing{Style.RESET_ALL}")
    time.sleep(0.05)
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    time.sleep(0.05)
    print("")
    try:
     type_rpc = int(input(f"{bracketopen}>{bracketclosed} {Fore.MAGENTA}RPC type -> {Style.RESET_ALL}"))
    except Exception:
     print("")
     print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Invalid Input{Style.RESET_ALL}")
     time.sleep(2)
     custom_rpc()
    def stop_rpc():
      os.system("cls")
      time.sleep(0.05)
      print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}RPC is running, leave the program open in the background{Style.RESET_ALL}")
      print("")
      print(f"{bracketopen}{Fore.WHITE}01{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Stop RPC{Style.RESET_ALL}")
      time.sleep(0.05)
      print(f"{bracketopen}{Fore.WHITE}02{Style.RESET_ALL}{bracketclosed}{Fore.MAGENTA} Exit{Style.RESET_ALL}")
      time.sleep(0.05)
      print("")
      try:
       commandStop = int(input(f"""{Fore.MAGENTA} ┌──({Fore.WHITE}{username}{Fore.MAGENTA})─[{Fore.WHITE}~/{system_text}/{pc_name}{Fore.MAGENTA}]
 └─{Fore.WHITE}$ {Style.RESET_ALL}"""))
      except Exception:
       time.sleep(0.05)
       print("")
       print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Invalid Input{Style.RESET_ALL}")
       time.sleep(2)
       stop_rpc()

      if commandStop == 1:
        rpc.clear()
        print("")
        time.sleep(0.05)
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}RPC stopped{Style.RESET_ALL}")
        time.sleep(1)
        main()
      elif commandStop == 2:
        rpc.clear()
        sys.exit()
      else:
        print("")
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Invalid Input{Style.RESET_ALL}")
        time.sleep(2)
        stop_rpc()

    try:
         if type_rpc == 1:
            try:     
             def run_rpc_listen():
              global rpc
              rpc = Presence(bot_ID)
              rpc.connect()
              rpc.update(
               details=title_rpc,
               state=description_rpc,
               activity_type=ActivityType.LISTENING,
              )
             rpc_thread = threading.Thread(target=run_rpc_listen, daemon=True)
             rpc_thread.start()
             stop_rpc()
            except Exception:
             time.sleep(0.05)
             print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Failed to run RPC{Style.RESET_ALL}")
             main()
         elif type_rpc == 2:
            try:
             def run_rpc_play():
              global rpc
              rpc = Presence(bot_ID)
              rpc.connect()
              rpc.update(
               details=title_rpc,
               state=description_rpc,
               activity_type=ActivityType.PLAYING,
              )
             rpc_thread = threading.Thread(target=run_rpc_play, daemon=True)
             rpc_thread.start()
             stop_rpc()
            except Exception:
             time.sleep(0.05)
             print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Failed to run RPC{Style.RESET_ALL}")
             main()
         elif type_rpc == 3:
            try:
             def run_rpc_watch():
              global rpc
              rpc = Presence(bot_ID)
              rpc.connect()
              rpc.update(
               details=title_rpc,
               state=description_rpc,
               activity_type=ActivityType.WATCHING,
              )
             rpc_thread = threading.Thread(target=run_rpc_watch, daemon=True)
             rpc_thread.start()
             stop_rpc()
            except Exception:
             time.sleep(0.05)
             print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Failed to run RPC{Style.RESET_ALL}")
             main()
         elif type_rpc == 4:
            try:
             def run_rpc_comp():
              global rpc
              rpc = Presence(bot_ID)
              rpc.connect()
              rpc.update(
               details=title_rpc,
               state=description_rpc,
               activity_type=ActivityType.COMPETING,
              )
             rpc_thread = threading.Thread(target=run_rpc_comp, daemon=True)
             rpc_thread.start()
             stop_rpc()
            except Exception:
             time.sleep(0.05)
             print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Failed to run RPC{Style.RESET_ALL}")
             main()
         else:
           print("")
           print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Invalid Input{Style.RESET_ALL}")
           time.sleep(2)
           custom_rpc()

    except Exception as e:
        print(f"{bracketopen}{Fore.WHITE}!{Style.RESET_ALL}{bracketclosed} {Fore.MAGENTA}Failed to run RPC{Style.RESET_ALL}")
        main()
 if command == 1:
    custom_rpc()
 elif command == 2:
    sys.exit()
 else:
   main()
 
main()
