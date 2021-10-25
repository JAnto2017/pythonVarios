#Function re.search finds a match of a pattern anywhere in the string
#re.findall returns a list of all substrings that match a pattterc

import re

pattern = r"spam"

if re.match(pattern,"eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern,"eggspamsausagespam"):
    print ("Match")
else:
    print("No match")

print(re.findall(pattern,"eggspamsausagespam"))
