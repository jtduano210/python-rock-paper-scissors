# simple rock paper scissors shell game
# by Jeffrey Duano

import datetime, os, platform
from time import sleep

def rps_ai():
  t = datetime.datetime.now()
  x = t.isoformat(timespec='milliseconds')
  x = int(x[-1])
  if x == 1 or x == 4 or x == 7 or x == 0: # 0 here because rock is most thrown in rps
    return "r"
  elif x == 2 or x == 5 or x == 8:
    return "p"
  elif x == 3 or x == 6 or x == 9:
    return "s"
  else:
    return -1

def rps_check(in_var, opp_var):  # case 0: tie, case 1: loss, case 2: win!
  if in_var == opp_var:
    return 0
  elif in_var == "r" and opp_var == "p":
    return 1
  elif in_var == "r" and opp_var == "s":
    return 2
  elif in_var == "p" and opp_var == "r":
    return 2
  elif in_var == "p" and opp_var == "s":
    return 1
  elif in_var == "s" and opp_var == "r":
    return 1
  elif in_var == "s" and opp_var == "p":
    return 2
  else:
    return -1

def main():
  wins = 0
  losses = 0
  while True:
    if platform.system() == "Windows":
      os.system("cls")
    else:
      os.system("clear")
    print("ROCK PAPER SCISSORS\n\nCURRENT RECORD:\nW = {}\nL = {}\n\nr = rock\np = paper\ns = scissors\n".format(wins, losses))
    in_var = input("Enter a character: ")
    if in_var != "r" and in_var != "p" and in_var != "s":
      print("\nInvalid selection.\n")
      sleep(2)
      continue
    opp_var = rps_ai()
    print("Computer's character: {}".format(opp_var))
    check = rps_check(in_var, opp_var)
    if check == 0:
      print("\nYou tied!")
    elif check == 1:
      print("\nYou lost!")
      losses += 1
    elif check == 2:
      print("\nYou won!")
      wins += 1
    sleep(2)

main()