import re

"""
s = "Chaled adosado en venta en Carrer de Joan"
m = re.match("^((?!en).)*",s)
if m:
    print (m.group(0))
"""

s = "Cala Murada (Manacor)"
m = re.match("([^()]+) \(([^()]+)\)",s)
if m:
    print(m.groups())