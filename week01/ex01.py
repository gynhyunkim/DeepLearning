import numpy as np

nums = [np.random.randint(1, 100) for _ in range(16)]
aa = [nums[0:8], nums[8:16]]
A = np.array(aa)

print(A.shape)
print(A.shape[0])
print(A.shape[1])
print(A)

sub_max = [0] * A.shape[0]
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if sub_max[i] < A[i][j]:
            sub_max[i] = A[i][j]
        
print("All Max: ", max(sub_max))
for i in range(A.shape[0]):
    print("SubMax ", i, ": ", sub_max[i])
        
B = np.reshape(A, (2, 2, 4))
print(B.shape)
print(B)
C = np.arange(16).reshape(2, 2, 4)
C[:, :, 2:4] = B[:, :, :2]
C[:, :, :2] = B[:, :, 2:4]
print(C)
