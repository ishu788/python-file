import re
pattern = r"[a-z A-Z]+ \d+"
matches=re.findall(pattern,"MXV2014,XYZ 2015,FUX 2019,MARUTI SUZUKI")
for match in matches:
    print(match,end="")
