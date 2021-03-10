import sys
import os
import shutil
import subprocess
from datetime import date

def config():
  f = open("./folder.txt", "r")
  return f.read()

def criarPasta():
  folder = config()
  atual = date.today().strftime('%d-%m-%Y')
  pasta = (folder + '/' + atual)
  if(os.path.isdir(pasta) == False):
    os.makedirs(folder + '/' + atual)
  return pasta

def deletar(file):
  if(os.path.exists(file)):
    os.remove(file)

params = sys.argv
if(len(params) > 1):
  params = params[1:]
  folder = config()
  for param in params:
    if(os.path.exists(param)):
      nome = criarPasta()
      base = os.path.basename(param)
      dest = nome + '/' + base
      if(os.path.exists(dest) == False):
        shutil.move(param, dest)
else:
  subprocess.call("explorer " + config(), shell=True)
