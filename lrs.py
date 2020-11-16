# lrs.py Source Code
# Written by @SPFck

from everything import *

#############################
# LOGIN AND REGISTER SYSTEM #
#############################

curr_usr = input("Insert the username: ")
curr_pwd = input("Insert the password: ")

if Path("db.txt").exists():
  login = open("db.txt", "r").read().replace("\n", "").split(":")
  if curr_usr == login[0] and curr_pwd == login[1]:
    banner()
    cmds()
    while True:
      curr_cmd = input(f"{login[0]}@root> ")
      if curr_cmd == "exit":
        cya()
      elif curr_cmd == "say":
        args = input("@> ")
        print(args)
      elif curr_cmd == "cmds":
        cmds()

  else:
    print("Nome ou senha Incorretos!")
else:
  with open("db.txt", "w") as fx:
    fx.write(f"{curr_usr}:{curr_pwd}")
    fx.close()
  input(f"Registered with success!!\n\n{curr_usr}@root> ")
