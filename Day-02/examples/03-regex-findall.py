####regular expression for finding word for sentence
import re
demo ="this line will be remember for long time"
developer="remember"

search=re.search(developer,demo)
if search:
    print("we have find",{search.group()}) ##curly brace are optional
else:
    print("OOPs! not found")
