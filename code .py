num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
dict={}
for key in sorted(num):
   dict[key]=sorted(num[key])
print(dict)