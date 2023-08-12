# -- CHANGE THIS VALUE TO ADJUST GAMMA --
POW_VALUE = 1.00
# --

result = ""

with open("vgct.cal", "r") as fd:
    line = fd.readline()
    while line.replace(" ", "").replace("\n", "") != "BEGIN_DATA":
        result += line
        line = fd.readline()

    result += line
    line = fd.readline()

    while not line.startswith("END_DATA"):
        rgba = list(map(lambda x: str(pow(float(x), POW_VALUE)), line.split(" ")))
        result += " ".join(rgba) + "\n"
        line = fd.readline()
    
    result += line

with open("result.cal", "w") as fd:
    fd.write(result)

import os
os.system(f"iccvcgt -i /usr/share/DisplayCAL/presets/sRGB.icc result.cal sRGB-{POW_VALUE}G.icc")
