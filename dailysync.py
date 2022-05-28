#!/usr/bin/env python

import multiprocessing
import subprocess
import os

src = "/data/prod/"
dest = "/data/prod_backup/"
events = []

def copy_event(event):
  subprocess.call(list(event))

for root, dirs, files in os.walk(src, topdown=False):
  for name in files:
    _src = os.path.join(root, name)
    _dest = _src.replace(src, dest)
    events.append( ("rsync", "-arq", _src, _dest) )
  for name in dirs:
    _src = os.path.join(root, name)
    _dest = _src.replace(src, dest)
    events.append( ("rsync", "-arq", _src, _dest) )

  with Pool(len(events)) as p:
    p.map(copy_event, events)