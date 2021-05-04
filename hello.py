import sys
import numpy as np
import scipy.stats as stats

def get_cubed(lst):
  '''
  INPUT: LIST (containing numeric elements)
  OUTPUT: LIST (cubed value of each even number in originals list)
  return a list containing each element cubed
  '''
  return [x*x*x for x in lst]


print("Output question 1: ", get_cubed([1,2,3]))


def get_squared_evens(lst):
    '''
    INPUT: LIST (containing numeric elements)
    OUTPUT: LIST (squared value of each even number in originals list)
    return squared evens in a list
    '''
    return [x*x for x in lst  if x % 2 == 0]


print("Output question 2: ", get_squared_evens([1,2,3,4,5,6,7,8]))


def make_dict(lst1,lst2):
    '''
    INPUT: LST1, LST2
    OUTPUT: DICT (LST 1 are the keys and LST2 are the values)
    Given equal length lists create a dictionary where the first list is the keys
    '''
    return {lst1[i]: lst2[i] for i in range(len(lst1))}


print("Output question 3: ", make_dict([1,2,3],['a','b','c']))



def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (with counts of each character in input string)
    Return a dictionary of character counts
    '''
    string_split=[char for char in string]
    string_distinct=sorted(list(set(string_split)), key=str.lower)
    dic_list= {string_distinct[i]: string_split.count(string_distinct[i]) for i in range(len(string_distinct))}
    dic_ord = sorted(dic_list.items(), key=lambda x: x[0])
    return  dic_ord

print("Output question 4: ", count_characters('abbcccddddeeeeeffffffggggggghhhhhhhh'))


def calculate_l1_norm(v):
    '''
    INPUT: LIST or ARRAY (containing numeric elements)
    OUTPUT: FLOAT (L1 norm of v)
    calculate and return a norm for a given vector
    '''
    return  sum([abs(x) for x in  v])

print("Output question 5: ", calculate_l1_norm([2.0, -3.5, 5.1]))


def get_vector_sum(vectorLower, vectorUpper):
    '''
    INPUT: vector lower and upper bounds
    OUTPUT: calculated value for vector sum
    (1) create a vector ranging from 1:150
    (2) transform the vector into a matrix with 10 rows and 15 columns
    (3) print the sum for the 10 rows
    '''
    n = 10
    vector_int = list(range(vectorLower, vectorUpper))  
    split_vec = [vector_int[i:i + n] for i in range(0, len(vector_int), n)] 

    matrix_used = np.matrix(split_vec)  
    list_res = np.sum(matrix_used,axis=0).tolist()

    return  list_res[0]



print("Output question 6: ", get_vector_sum(1,151))




def geometric_distribution(p,k):
    '''
    INPUT: probability of success and trials
    OUTPUT: determined probability
    '''

    return ((1-p)^(k-1))*(p)



def poisson_distribution(mu,k):
    '''
    INPUT: parameter of the poisson distribution and number of accidents
    OUTPUT: determined probability
    '''
    return np.exp(-mu) * mu**k / np.math.factorial(k)



def gaussian_distribution(loc_val, scale_val, cdf_val):
    '''
    INPUT: loc (mean of the distribution), scale (standard deviation of the distribution), and cdf values
    OUTPUT: determined probability
    '''
    return stats.norm(loc_val, scale_val).cdf(cdf_val)


print("Output question 9: ", gaussian_distribution(0,1,0))



def matrix_multiplication(A,B):
  '''
  INPUT: LIST (of length n) OF LIST (of length n) OF INTEGERS
  LIST (of length n) OF LIST (of length n) OF INTEGERS
  OUTPUT: LIST OF LIST OF INTEGERS
  (storing the product of a matrix multiplication operation)
  Return the matrix which is the product of matrix A and matrix B
  where A and B will be (a) integer valued (b) square matrices
  (c) of size n-by-n (d) encoded as lists of lists, e.g.
  A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix
  | 2 3 4 |
  | 6 4 2 |
  |-1 2 0 |
  You may not use numpy. Write your solution in straight python
  '''
  return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]


print("Output question 10: ", matrix_multiplication([[12,7,3],[4 ,5,6],[7 ,8,9]],[[5,8,1],[6,7,3],[4,5,9]]))


