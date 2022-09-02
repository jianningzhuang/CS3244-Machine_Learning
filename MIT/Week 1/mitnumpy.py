import numpy as np

### create a new matrix
A = np.array([[0,1], [2,3], [4,5], [6,7]]) # 4x2 matrix

### transpose function
def tp(A):
    return np.transpose(A)

### return shape in form (row, col) or (length,) if 1D array
print(A.shape)

### 2D array slicing
#A = A[a:b , c:d] #from rows a to b (not inclusive), slice from col c to d

#A = A[a , c:d] #from row a, slice elements c to d => 1D array

#A = A[a:b, c] #from rows a to b, return cth element => 1D array
print(A)
print(A.shape)

### turn list of numbers into 2D numpy row vector
def rv(value_list):
    return np.array([value_list])

### turn list of numbers into 2D numpy column vector
def cv(value_list):
    return np.transpose(rv(value_list))

B = np.array([[3], [4]])
### euclidean length of column vector
def length(col_v):
   return np.sum(col_v * col_v)**0.5
   #return np.asscalar(np.dot(np.transpose(col_v), col_v))**0.5

### unit vector
def normalize(col_v):
    return col_v/length(col_v)

### returns the final column as a two dimensional array
def index_final_col(A):
    return A[: , -1:] #for all rows, slice last element to keep 2D array

data = np.array([[150, 5.8], [130, 5.5], [120, 5.3]])

print(data.shape[0])
print(np.dot(np.array([[1,1,1]]), data))

def transform1(data):
    accum = np.array([[1]*(data.shape[0])])
    return np.transpose(np.dot(accum, data))

### column vector of sum of elements in each row
def transform(data):
    return (np.dot(data, np.array([[1], [1]])))




### signed distance from point to hyperplane = projection of vector from point to hyperplane (theta*x + theta_0) onto normal

# 1) origin to hyperplane
# dot((0-x), theta)/norm(theta) = theta_0/norm(theta)

# 2) general point to hyperplane
# dot((p-x), theta)/norm(theta) = (dot(p, theta) + theta_0 )/norm(theta) by distributive property of dot product


def signed_dist(p, th, th0):
    return (np.dot(np.transpose(p), th) + th0)/length(th)


### 1 if on positive side of hyperplane, 0 if on hyperplane, -1 if on negative side
def positive(x, th, th0):
    return np.sign(np.dot(np.transpose(th), x) + th0)


data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
labels = rv([-1, -1, +1, +1, +1])

#A = positive(data, th, th0) #A should be a 1 by 5 array of values, either +1, 0 or -1, indicating, for each point in data, whether it is on the positive side of the hyperplane defined by th, th0
#A = positive(data, th, th0) == labels #A should be a 1 by 5 array of boolean values, either True or False, indicating for each point in data and corresponding label in labels whether it is correctly classified by hyperplane


### returns the number of points for which the label is equal to the output of the positive function on the point.
def score(data, labels, th, th0):
    return np.sum(positive(data, th, th0) == labels)

# data is dimension d by n
# labels is dimension 1 by n
# ths is dimension d by m
# th0s is dimension 1 by m
# return matrix of integers indicating number of data points correct for
# each separator:  dimension m x 1
def score_mat(data, labels, ths, th0s):
   pos = np.sign(np.dot(np.transpose(ths), data) + np.transpose(th0s))
   return np.sum(pos == labels, axis = 1, keepdims = True)
def best_separator(data, labels, ths, th0s):
   best_index = np.argmax(score_mat(data, labels, ths, th0s))
   return cv(ths[:,best_index]), th0s[:,best_index:best_index+1]


