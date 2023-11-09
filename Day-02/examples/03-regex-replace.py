#######for replacing word from sentence
import re
mytext="cloudblitz has lots of money"
text="lots"
replace123="less"
#sub is keyword
demo=re.sub(text,replace123,mytext) ##text konsa change krna #replace123 new wala #mytext kisme edit krna

print("latest changes",demo)
