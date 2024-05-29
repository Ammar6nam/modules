import json

jsonString='{"name":"Paul","surname":"Polish","number":1234,"list":[1,2,3,4]}'
dict=json.loads(jsonString)
print(dict['list'][3])

myDict={'name':'Ammar',
        'surname':'Nammour'}
jsonConent=json.dumps(myDict)
print('mydict:',myDict)
print(type(myDict))
print('jsonConent',jsonConent)
print(type(jsonConent))