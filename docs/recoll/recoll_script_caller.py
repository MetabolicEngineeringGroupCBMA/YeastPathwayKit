#!/usr/bin/python3
import re
import subprocess
from pathlib import Path

cmd = "./recollscript.py filename:pYPKa_E_*.gb"
folder = "/home/bjorn/Desktop/YeastPathwayKit/sequences"
p = subprocess.run(cmd,
                   stdout=subprocess.PIPE,
                   encoding='utf-8',
                   shell=True)
result = p.stdout.strip()

result = result.replace("-checkpoint", "")
result = result.replace("tp.gb", ".gb")
found = re.findall("pYPKa_E_.+\.gb", result)

collected = sorted(set(p.name for p in Path(folder).glob("pYPKa_E_*.gb")))

diff = set(found).difference(set(collected))


