import sys, subprocess, os

args = []
l = len(sys.argv)
if args is not None:
  for i in range(l):
    arg = sys.argv[i]
    args.append(arg)

zsh_bin = "/bin/zsh"
cd_dev = "cd ~/development/"
frameworks = ["react"]

if l == 1:
  commands = cd_dev
else:
  frame = args[1]
  if frame not in frameworks:
    print("ERROR: framework \"" + frame + "\" not recognized")
    exit()
  if l == 3:
    project = args[2]
  else:
    project = ""
  if frame == 'react':
    commands = ("python3 ~/development/scripts/launch_"+frame+".py " + project)

print(commands)
subprocess.run(commands + ";", shell=True, executable=zsh_bin)