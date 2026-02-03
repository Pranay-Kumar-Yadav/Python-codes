#json
import json
d={'name':'kkkkk','age':22,'ismarried':False,'insurance':None}
name="kkkkk"
age="22"
data=["kkkkk",22,False,None]
data1=("kkkkk",22,False,None)
var=None

print(json.dumps(d))

print(type(json.dumps(d)))