#REGULAR EXPRESS IN PYTHON

import re

pattern = r"sspam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")


