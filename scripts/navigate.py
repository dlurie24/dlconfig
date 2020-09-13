import sys, subprocess

args = []
for i, arg in enumerate(sys.argv):
  args = args.append(arg)

if args is None:
  subprocess.run("dev", shell=True, executable="/bin/zsh")

