#!/usr/bin/env python

import sys
import re

def usage():
  print('usage: {} path/to/file'.format(sys.argv[0]))

if len(sys.argv) != 2:
  usage()
  exit(1)

notes = open(sys.argv[1]).read().split('\n\n')
print('Targets\tHosts\tNVTs\tScan Duration\tResults\tErrors\tTarget load\tTarget iowait\tGSM load\tComment')

for note in notes:
  lines = note.split('\n')

  if not lines[0].startswith('Scan'):
    comment = lines[0]
    lines.pop(0)  # remove first line
  else:
    comment = ''

  targets = ''
  if comment:
    try:
      targets = re.search(r'^(\d+) Container', comment).group(1)
    except:
      pass

  hosts, nvts =  '', ''
  try:
    hosts = re.search(r'^Scan (\d+) hosts', lines[0]).group(1)
    nvts = re.search(r' (\d+) NVTs$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    pass

  try:
    duration = re.search(r'^Scan Duration ([\d:]+)h$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    duration = ''

  try:
    results = re.search(r'^Results: (\d+)$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    results = ''

  try:
    errors = re.search(r'^Errors: (\d+)$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    errors = ''

  tload, tiowait =  '', ''
  try:
    tload = re.search(r'^Target load[\w\.: ]* (\d+.?\d*)', lines[0]).group(1)
    tiowait = re.search(r' \((\d*.?\d+)% iowait\)$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    pass

  try:
    gload = re.search(r'^GSM Load: (\d+)$', lines[0]).group(1)
    lines.pop(0)  # remove first line
  except:
    gload = ''

  print('\t'.join([targets, hosts, nvts, duration, results, errors, tload, tiowait, gload, comment]))
