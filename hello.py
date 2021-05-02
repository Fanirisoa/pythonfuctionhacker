import sys
import numpy as np

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
 print(vector_int)
   
    split_vec = [vector_int[i:i + n] for i in range(0, len(vector_int), n)] 
 print(split_vec)

    return  matrix(split_vec)    



print("Output question 6: ", get_vector_sum(1,21))










