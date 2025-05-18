"""
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.shape)
#representa el tipo de dato de los elementos de array
print(arr.dtype)
#ver la version de numpy
print(np.__version__)
#te permite verificar que el objeto creado es realmente un arreglo de NumPy (ndarray) y no una lista común de Python.
print(type(arr))
#conta las dimensiones de los bloques de datos
print(arr.ndim)
#numero de dimensiones
print('number of dimensions :', arr.ndim)
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3])
"""
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])
print("2nd element on 2nd row:", arr[1, 1])
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
"""


