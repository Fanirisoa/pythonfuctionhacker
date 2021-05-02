import sys


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
	string_split = [char for char in string]
	string_distinct = list(set(string_split))
	return  {string_distinct[i]: string_split.count(string_distinct[i]) for i in range(len(string_distinct))}


print("Output question 4: ", count_characters('abbcccddddeeeeeffffffggggggghhhhhhhh'))

