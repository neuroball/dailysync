#!/usr/bin/env python3

from multiprocessing import Pool
import subprocess
import os

src = "/data/prod/"
dest = "/data/prod_backup/"
events = []


def copy_event(event):
  print(list(event))
  pass
  subprocess.call(list(event))


def main():
  src_path = os.getcwd() + src

  for root, dirs, files in os.walk(src_path, topdown=False):
    for name in files:
      _src = os.path.join(root, name)
      _dest = _src.replace(src, dest)
      events.append( ("rsync", "-arq", _src, _dest) )

  print(events)
  with Pool() as p:
    p.map(copy_event, events)


if __name__ == "__main__":
  main()

