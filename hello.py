def get_cubed(lst):
  '''
  INPUT: LIST (containing numeric elements)
  OUTPUT: LIST (cubed value of each even number in originals list)
  return a list containing each element cubed
  '''
  return [x*x*x for x in list]


A = [1,2,3]

get_cubed(A)
