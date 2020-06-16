import numpy as np

random_array = np.linspace(1,20,20,dtype=int)
print(random_array)

b = random_array.reshape(4,5)
print('Reshaped array: \n{}'.format(b))

b[np.where(b==np.max(b,axis=1,keepdims=True))] = 0
print('Replaced array: \n{}'.format(b))
