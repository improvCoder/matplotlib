import torch
import matplotlib.pyplot as mt

X=torch.rand(100)*10
y=torch.rand(100)*10
print(X)
print(y)
mt.scatter(X,y,marker='o')
mt.show()


