from data.repository import load_data
import os
import platform
import shutil

def clear_terminal():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def display_status():
  data = load_data()

  print("=== POMO RPG ===")
  print(f"Name: {data["name"]}")
  print(f"Level: {data["level"]}  |  XP: {data["xp"]}/{data["level"]+1}  |  Pomos: {data["pomos"]}\n")

def display_character():
  print("Character:")
  print(r"""  / \
  | |
  |.|
  |.|
  |:|      __
,_|:|_,   /  )
  (Oo    / _I_
   +\ \  || __|
      \ \||___|
        \ /.:.\-\
         |.:. /-----\
         |___|::oOo::|
         /   |:<_T_>:|
        |_____\ ::: /
         | |  \ \:/
         | |   | |
         \ /   | \___
         / |   \_____\
         `-'""")

def draw_time_progress_bar(progress, progress_max):
  # Retorna (colunas, linhas) do terminal
  columns, lines = shutil.get_terminal_size()

  width = columns - 11

  filled = int((progress / progress_max) * width)
  bar = '#' * filled + '-' * (width - filled)
  print(f"\r⏳ [{bar}] {progress // 60:02}/{progress_max // 60:02}", end="")
