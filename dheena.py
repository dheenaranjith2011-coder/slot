import re

s='dheena 9342357445 santhosh 8072481818'
ans= re.findall('/d{10}',s)
print(ans)
