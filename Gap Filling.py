#Filling in the Gaps
import shutil, re
from pathlib import Path

p = Path(r'C:\Users\thikr\OneDrive\Documentos\Lernen\Python\Automate the Boring Stuff with Python Programming\Projects\Filling in the Gaps')

pattern = re.compile('''
^(.*?)
(00\d|0\d\d|\d{3}|\d\d|\d{3}|\d)
(.*?)$
''', re.VERBOSE)

fileP = p.glob('*')
fileS = set()
realP = 1
for file in list(fileP):
    filename = re.search(pattern, file.name)
    if filename == None:
        continue
    firstPart = filename.group(1)
    position = filename.group(2)
    finalPart = filename.group(3)
    if firstPart not in fileS:
        fileS.add(f"{firstPart}")
        realP = 1
    if int(position) == realP:
        realP += 1
        continue
    else:
        if realP < 10:
            shutil.move(Path(p/f"{firstPart}{position}{finalPart}"),Path(p/f"{firstPart}00{realP}{finalPart}"))
        elif realP < 100:
            shutil.move(Path(p/f"{firstPart}{position}{finalPart}"),Path(p/f"{firstPart}0{realP}{finalPart}" ))
        else:
            shutil.move(Path(p/f"{firstPart}{position}{finalPart}"),Path(p/f"{firstPart}{realP}{finalPart}" ))
    realP += 1
    
    
 
