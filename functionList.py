#! /usr/bin/python/  python3
# coding: utf-8
import logging as lg

class listTransformation:
    """
    A class used to represent a list as input

    ...

    Attributes
    ----------
    queries : array[str]
        an array of query strings
    strings : array[str]
       an array of strings to search

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

	
    def __init__(self, inputList):
        """
        a constructor to initialize the attributes of the class setStringToCompare.

        : queries : array[str]  an array of query strings
        : strings : array[str]  an array of strings to search
        """
        self.inputList = inputList



    def reverseArray(a):
        """
        Given an array, A, of N integers, print each element in reverse order as a single line of space-separated integers.

        :return: reverse order as a single line of space-separated integers.
        :rtype: array[int]
        
        :Example:
        >>> a = [1,2,100,3]
        >>> reverseArray(a)
        >>> [3, 100, 2, 1]  
        """        
        n = len(a)
        return [a[n-1-i] for  i in range(0,n)]


    
    def left_rotation(d,self):
        """
        Given an array of n integers and a number, d, perform  left rotations on the array
        A left rotation operation on an array of size n shifts each of the array's elements  1 unit to the left. 
        For example, if  2-left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

        :return: shifted array
        :rtype: array[int]
        
        :Example:
        >>> n = 5
        >>> d = 4
        >>> a = [i for i in range(1,n+1)]   
        >>> left_rotation(4,a)
        >>> [5, 1, 2, 3, 4]
        """

        n = len(self.inputList)
        k = n - d
        b = []
        for i in range(0,n):
            b.append(l[i-k])      
        return b


    
    def arrayManipulation(d,self):
        """
        Given an array of n integers and a number, d, perform  left rotations on the array
        A left rotation operation on an array of size n shifts each of the array's elements  1 unit to the left. 
        For example, if  2-left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

        :return: shifted array
        :rtype: array[int]
        
        :Example:
        >>> n = 5
        >>> d = 4
        >>> a = [i for i in range(1,n+1)]   
        >>> left_rotation(4,a)
        >>> [5, 1, 2, 3, 4]
        """
        queries = self.queries
        a = np.array([0]*d)
        k = len(self.queries)
        for i in range(0,k): 
            a[int(self.queries[i][0])-1:int(self.queries[i][1])] += int(self.queries[i][2]) 
        return max(a)





    def decryptPassword(self):
        """
        Given an array of n integers and a number, d, perform  left rotations on the array
        A left rotation operation on an array of size n shifts each of the array's elements  1 unit to the left. 
        For example, if  2-left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

        :return: shifted array
        :rtype: array[int]
        
        :Example:
        >>> s = 'hAck3rr4nk'
        >>> decryptPassword(s)
        >>>
        >>> s = 'poTaTo' 
        >>> decryptPassword(s)
        >>> ['p', 'T', 'o', '*', 'T', 'a', '*', 'o']
        """
        l = [char for char in self]
        m = len([letter for letter in l if letter.isupper()])
        k = len(l)
        w = []
        b = []
        for i in list(range(k)):        
            if i< k -2 and l[i].islower() and l[i+1].isupper():
               w.append(l[i+1]) 
               w.append(l[i])           
            elif l[i].isupper() and l[i-1].islower():
               w.append('*')          
            elif l[i].isnumeric():
               w.append(0)
               b.append(l[i]) 
            else:
               w.append(l[i])      
        b.reverse() 
        d = b + w
        return d


    def hourglassSum(self):
        """
        Given a 6 x 6  2D Array, "arr":
        We define an hourglass in A to be a subset of values with indices falling in this pattern in "arr"'s graphical representation:
        For example, 

        a b c
          d
        e f g

        There are 16 hourglasses in "arr", and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in "arr", 
        then print the maximum hourglass sum.

        For example, given the 2D array:
        -9 -9 -9  1 1 1 
         0 -9  0  4 3 2
        -9 -9 -9  1 2 3
         0  0  8  6 6 0
         0  0  0 -2 0 0
         0  0  1  2 4 0

        We calculate the following  hourglass values:

        -63, -34, -9, 12, -10, 0, 28, 23, -27, -11, -2, 10, 9, 17, 25, 18

        Our highest hourglass value is 28 from the hourglass:

        0 4 3
          1
        8 6 6

        
        :return: the maximum hourglass sum.
        :rtype: int
        
        :Example:
        >>> T = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]
        >>> hourglassSum(T)
        >>> 28
        """


        a = []
        for  c in list(range(0,4)):
            for  l in list(range(0,4)):
                Matrix = [[self[i][j] for  j in range(c,c+3)]   for i in range(l,l+3)] 
                print(Matrix)
                a.append(sum(sum(Matrix,[])) -  Matrix[1][0] -  Matrix[1][2])
        return max(a)















