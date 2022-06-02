import numpy as geek
  
# input array
in_arr = geek.array([[[216,0]],

 [[ 87,282]],

 [[469,20]],

 [[385,343]]])
print(in_arr.shape)
in_arr = geek.reshape(in_arr,(4,2))
in_arr = in_arr.tolist()
print(in_arr)
print ("Input unsorted array : ", in_arr) 
  
out_arr = geek.argsort(in_arr)
print ("Output sorted array indices : ", out_arr)
print("Output sorted array : ", in_arr[out_arr])