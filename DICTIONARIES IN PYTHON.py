
>>> #key should be immutable and unique
>>> data={1:'rahul', 2:'anchal', 3: 'bhaiya'}
>>> data
{1: 'rahul', 2: 'anchal', 3: 'bhaiya'}
>>> data[4]

>>> data[3]
'bhaiya'
>>> data[2]
'anchal'
>>> data[1]
'rahul'
>>> data.get(1)
'rahul'
>>> data.get(1,'not found')
'rahul'
>>> data.get(5,'not found')
'not found'
>>>

>>> keys=['navin','kiran','harsh']
>>> values=['python','java','javascript']
>>> data=zip(keys,values)
>>> 
>>> data
<zip object at 0x03992D48>
>>> data=dict(zip(keys,values))
>>> data
{'navin': 'python', 'kiran': 'java', 'harsh': 'javascript'}
>>> data['navin']
'python'
>>> data['kiran']
'java'
>>>
>>> data['harsh']
'javascript'
>>>
>>> data['rahul']='react'
>>> data
{'navin': 'python', 'kiran': 'java', 'harsh': 'javascript', 'rahul': 'react'}
>>> del data['navin']
>>> data
{'kiran': 'java', 'harsh': 'javascript', 'rahul': 'react'}
>>>
>>> prog={'js':'atom','cs':'vs','python':['pycharm','vscode'],'java':{'jse':'netbeans','jee':'eclips'}}
>>> prog
{'js': 'atom', 'cs': 'vs', 'python': ['pycharm', 'vscode'], 'java': {'jse': 'netbeans', 'jee': 'eclips'}}
>>> prog['js]
>>> prog['js']
'atom'
>>> prog['python']
['pycharm', 'vscode']
>>> prog['java']
{'jse': 'netbeans', 'jee': 'eclips'}
>>> 
