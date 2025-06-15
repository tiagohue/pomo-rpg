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
  |.|
  |.|
  |:|     __
,_|:|_,  /  )
  (Do   / _I_
   +\ \ || __|
     \ \||___|_
      \ \/.:.\/\
       \|.:::/-----\
        |___|::oOo::|
        /   |:(III):|
       |_____\ ºOº /
        | |  \ \:/
        |_|   |_|
        \ /   \ /__
        / |   |____\
        `-'""")

def draw_time_progress_bar(progress, progress_max):
  # Retorna (colunas, linhas) do terminal
  columns, lines = shutil.get_terminal_size()

  width = columns - 11

  filled = int((progress / progress_max) * width)
  bar = '#' * filled + '-' * (width - filled)
  print(f"\r⏳ [{bar}] {progress // 60:02}/{progress_max // 60:02}", end="")

def display_stresses():
  data = load_data()
  print(f"Physical Stress: {data["stress"]["physical"][0]}/{data["stress"]["physical"][1]}")
  print(f"Mental Stress: {data["stress"]["mental"][0]}/{data["stress"]["mental"][1]}")
  print()