'''import numpy as np'''

'''a=np.array([10,20,30])
print(a)'''
#---------------------------------------
'''X= np.array([[1, 2, 3], [4, 5, 6]])
print(X.shape)
print(X.ndim)    
print(X.size)'''
#--------------------------------------
'''x=np.array([[10,20,30],[40,50,60]]
           )
print(x[0,1])
print(x[:,1])
print(x[1,:])'''
#-----------------------------------------------
'''x=np.array([10,20,30,40,50])
print(np.mean(x))
print(np.median(x))
print(np.var(x))
print(np.std(x))
print(np.max(x))
print(np.min(x))
print(np.sum(x))'''
#------------------------------------------
'''print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.arrange(0,10,5))
print(np.linspace(1,2,3))'''
#----------------------------------------------
'''a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a+b)
print(a*b)
print(a-b)'''
#-------------------------------------------------
import numpy as np
import time
# Python list
size = 1_000_000
list1 = list(range(size))
list2 = list(range(size))
start = time.time()
result = [x + y for x, y in zip(list1, list2)]
end = time.time()
print("Python list addition time:", end - start)
# NumPy array
arr1 = np.array(list1)
arr2 = np.array(list2)
start = time.time()
result = arr1 + arr2  # Vectorized operation
end = time.time()
print("NumPy array addition time:", end - start)
