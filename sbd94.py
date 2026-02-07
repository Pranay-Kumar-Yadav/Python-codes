#accept string ending with alphanumeric character
import re
text = "hello123"
pattern = r".*[A-za-z0-9]$"

if re.fullmatch(pattern,text):
    print("Accept")
else:
    print("Discard")    