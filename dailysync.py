#!/usr/bin/env python3

from multiprocessing import Pool
import subprocess
import os

src = "/data/prod/"
dest = "/data/prod_backup/"
events = []


def copy_event(event):
  #print(list(event))
  subprocess.call(list(event))


def main():
  src_path = os.path.expanduser('~') + src
  dest_path = os.path.expanduser('~') + dest

  print(src_path, dest_path)
  for root, dirs, files in os.walk(src_path, topdown=True):
    for name in dirs:
      if name:
        _src = os.path.join(root, name)
        _dest = _src.replace(src, dest)
        events.append( ("rsync", "-arnv", _src, dest_path) )

  print(events)
  with Pool() as p:
    p.map(copy_event, events)


if __name__ == "__main__":
  main()



