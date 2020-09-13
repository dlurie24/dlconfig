import sys
import subprocess
import os
from github_token import GITHUB_TOKEN

args = []
l = len(sys.argv)
if args is not None:
  for i in range(l):
    arg = sys.argv[i]
    args.append(arg)

zsh_bin = "/bin/zsh"
cd_dev = "cd ~/development/"

DEFAULT_UI = "antd"
ui = ""

if l == 1:
  #commands = cd_dev
  commands = cd_dev
else:
  for i in range(len(args)):
    if i == 0:
      continue
    elif i == 1:
      project = args[i] # DEFAULT FIRST ARGUMENT
    else:
      arg = args[i]
      if arg in ["-u", "-ui"]:
        ui = arg
      if arg in ["-n", "-name"]:
        project = arg

  exists = os.path.exists(cd_dev+project)
  react_dir = "~/development/"+project+"/"+project+"-react/"
  if exists:
    commands = ""
  else:
    commands = (
      "mkdir ~/development/" + project + ";" +
      "\n"+ cd_dev + project + ";" +
      "\n"+"conda create -n " + project + "env " + "python=3.8" + " -y" + ";" +  
      "\n"+"conda activate " + project + "env" + ";" +
      "\n"+"npx create-react-app " + project + "-react" + ";" +
      "\n"+"rm " + react_dir + "src/App.js" + ";" +
      "\n"+"rm " + react_dir + "src/App.css" + ";" +
      "\n"+"rm " + react_dir + "src/App.test.js" + ";" +
      "\n"+"cp ~/development/react_config/components/Router.js " + react_dir + "src/" + ";" +
      "\n"+"cp ~/development/react_config/components/index.js " + react_dir + "src/" + ";" +
      "\n"+"yarn add react-router-dom" + ";"
      )

    if ui == "":
      ui_cmd = "\n"+"yarn add " + DEFAULT_UI + ";"
    else:
      ui_cmd = "\n"+"yarn add " + ui + ";"
    commands += ui_cmd

    commands += (
      "\n"+"cd " + react_dir + ";" + 
      "\n"+"rm -rf .git" + ";" + 
      "\n"+"cd .." + ";" +

      "\n"+"curl -H \"Authorization: token " + GITHUB_TOKEN +
      "\" https://api.github.com/user/repos -d '{\"name\": \"" + project + "\"}'" + ";" +
      "\n"+"git init" + ";" +
      "\n"+"echo node_modules > .gitignore"
      "\n"+"git add ." + ";" +
      "\n"+"git commit -m \"Created repository\"" + ";" + 
      "\n"+"git remote add origin https://github.com/dlurie24/" + project + ";" + 
      "\n"+"git remote -v" + ";" +
      "\n"+"git push origin master" + ";" +
      "\n"+"cd " + react_dir + ";" + 
      "\n"+"yarn start" + ";"
    )
  
  commands += (
    "\n"+"open -a Terminal " + react_dir + 
    "\n"+"open -a Terminal " + "~/development/" + project
  )

subprocess.run(commands, shell=True, executable=zsh_bin)




# if [$1 == ""]; then
# 130                   dev
# 131                 elif [! -a !/development/$1]; then
# 132                   mkdir ~/development/$1
# 133                   cd ~/development/$1
# 134                   conda create -n $1env
# 135                   conda activative $1env
# 136                 fi
# 137                 open -a Terminal ~/development/$1
# 138                 open -a Terminal ~/development/$1