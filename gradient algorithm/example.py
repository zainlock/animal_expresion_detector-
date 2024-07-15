import numpy as np 
#gardient Descent for Linear Regression
# yhat=wx+b
#loss=(y-yhat)**2/n

#initialization some parameters
x=np.random.randn(10,1)
y=2*x+np.random.rand()

#parameters
w=0.0
b=0.0

#hyperparameter
learning_rate=0.01

#create gardient descent function
def gradient_descent(x,y,w,b,learning_rate):
    dldw=0.0
    dlbd=0.0
    n=x.shape[0]
    
    #loss = ((y-(wx+b))**2)
    for xi,yi in zip(x,y):
        dldw+= -2*xi*(yi*(w*xi*b))
        dlbd+= -2*(yi*(w*xi+b))
        
        #make update
        w=w-learning_rate*(1/n)*dldw
        b=b-learning_rate*(1/n)*dlbd
        
        return w,b
for epoch in range(400):
    w,b=gradient_descent(x,y,w,b,learning_rate)
    yhat=w*x+b
    loss=np.divide(np.sum([y-yhat]**2,axis=0),x.shape[0])
    print(f"{epoch} loss is {loss},parameters W:{w}, B:{b}")