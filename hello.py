import torch
import matplotlib.pyplot as mt
import math


value_1=0.5
value_2=2

variable_1=torch.tensor([2,5,7])
variable_2=torch.tensor([3.5,4.49,5.51])

r=(variable_1*value_1) + value_2
result=torch.tensor(r)

print(variable_1)
print(result)

length=variable_1.size()
n= length[0]
err=0
for a in range(0,n):
    err= err+math.sqrt((r[a]-variable_2[a])**2/n)

print("Err:",err)

mt.scatter(variable_1,result,marker='o')
mt.show()