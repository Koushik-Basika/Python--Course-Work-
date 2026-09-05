import re 
pattern=r"[0-9]"
text="codegnan"
res=re.match(pattern,text)
print(res.group() if res else "pattern not found")

import re 
pattern=r"[0-9]"
text="codegnan2026"
res=re.search(pattern,text)
print(res.group() if res else "pattern not found")

import re 
pattern=r"[0-9]"
text="codegnan 2026 python version 3.14"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"[0-9]"
text="codegnan 2026 python version 3.14"
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

import re 
pattern=r"[0-9]{8}"
text="45678901"
res=re.fullmatch(pattern,text)
print(res.group() if res else "pattern not found")


import re 
pattern=r"[,(*]"
text="java,python(mysql*css"
res=re.split(pattern,text)
print(res)

import re 
pattern=r"[a-z]"
text="python version 3.14,batch-063"
res=re.sub(pattern,"*",text)
print(res)

#meta characters

import re 
pattern=r"t.u"
text="thu tiu tku tou tipu yoioup"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"^(91)"
text="919032998114"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"14$"
text="919032998114"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"to*"
text="to t too tooo toooo"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"ab+"
text="ab abbb a abbbbbb abbbb"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"91|0"
text="05678"
res=re.findall(pattern,text)
print(res)

import re 
pattern=r"[aeiouAEIOU]"
text="Codegnan Programming"
res=re.findall(pattern,text)
print(res)











