#! /usr/bin/python/  python3
# coding: utf-8
import logging as lg

from itertools import permutations

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



    def simpleArraySum(arr):
        """
        Given an array of integers, find the sum of its elements.

        :return: Print the sum of the array's elements as a single integer.
        :rtype: int
        
        :Example:
        >>> a = [1,2,3,4,10,11]
        >>> simpleArraySum(a)
        >>> 31
        """   
        somme = 0
        for i in list(range(len(arr))):
            somme += arr[i]
        return somme

    def compareTriplets(a, b):
        """
        Given a and b, determine their respective comparison points. The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

            - If a[i] > b[i], then Alice is awarded 1 point.
            - If a[i] < b[i], then Bob is awarded 1 point.
            - If a[i] = b[i], then neither person receives a point.

        Comparison points is the total points a person earned.

        :return: a's score is in the first position, and b's score is in the second.
        :rtype: array[int]

        :Example:
        >>> a = [1, 2, 3]
        >>> b = [3, 2, 1]
        >>> compareTriplets(a, b)
        >>> [1, 1]       
        """   
        queries = [[1,0] if a[i] > b[i]  else  [0,1] if a[i] < b[i] else [0,0]  for i in range(len(a))]
        val_a = 0
        val_b = 0
        for i in list(range(len(a))):
            val_a += queries[i][0]
            val_b += queries[i][1]
        return [val_a,val_b]    
    

    def diagonalDifference(arr):
        """
        Given a square matrix, calculate the absolute difference between the sums of its diagonals.

        :return: the absolute difference between the sums of the matrix's two diagonals as a single integer.
        :rtype: int
        
        :Example:
        >>> a = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
        >>> diagonalDifference(a)
        >>> 15  
        """  
        n= len(arr)
        left_diag = sum(arr[i][-i-1] for i in range(n))
        rigth_diag = sum(arr[i][i] for i in range(n))
        return abs(rigth_diag-left_diag)


    def rotate(l, n):
        return l[n:] + l[:n]


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




    def arrayManipulation(n, queries):
        """
        Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive.
        Once all operations have been performed, return the maximum value in your array.

        :return:  max of array
        :rtype:  int

        For example, the length of your array of zeros n = 10. Your list of queries is as follows:

            a b k
            1 5 3
            4 8 7
            6 9 1

        Add the values of k between the indices a and b inclusive:

        index->  1 2 3  4  5 6 7 8 9 10
                [0,0,0, 0, 0,0,0,0,0, 0]
                [3,3,3, 3, 3,0,0,0,0, 0]
                [3,3,3,10,10,7,7,7,0, 0]
                [3,3,3,10,10,8,8,8,1, 0]

        The largest value is 10  after all operations are performed.        

        
        :Example:
        >>> queries = [[1,2,100],[2,5,100],[3,4,100]]
        >>> a = 5
        >>> arrayManipulationNumpy(5,a1) 
        >>> 200
        """
       
        array = [0] * (n + 1)
        
        for query in queries: 
            a = query[0] - 1
            b = query[1]
            k = query[2]
            array[a] += k
            array[b] -= k
            
        max_value = 0
        running_count = 0
        for i in array:
            running_count += i
            if running_count > max_value:
                max_value = running_count
                
        return max_value




    
    def arrayManipulationNumpy(d,self):
        """
        Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive.
        Once all operations have been performed, return the maximum value in your array.

        :return:  max of array
        :rtype:  int

        For example, the length of your array of zeros n = 10. Your list of queries is as follows:

            a b k
            1 5 3
            4 8 7
            6 9 1

        Add the values of k between the indices a and b inclusive:

        index->  1 2 3  4  5 6 7 8 9 10
                [0,0,0, 0, 0,0,0,0,0, 0]
                [3,3,3, 3, 3,0,0,0,0, 0]
                [3,3,3,10,10,7,7,7,0, 0]
                [3,3,3,10,10,8,8,8,1, 0]

        The largest value is 10  after all operations are performed.        

        
        :Example:
        >>> queries = [[1,2,100],[2,5,100],[3,4,100]]
        >>> a = 5
        >>> arrayManipulationNumpy(5,a1) 
        >>> 200
        """
        queries = self.queries
        a = np.array([0]*d)
        k = len(self.queries)
        for i in range(0,k): 
            a[int(self.queries[i][0])-1:int(self.queries[i][1])] += int(self.queries[i][2]) 
        return max(a)





    def SkyscrapersJim(arr):
        queries = [s for s in [[j,[i for i, x in enumerate(arr) if x == j]] for j in set(arr)] if len(s[1]) > 1]
        res = [[queries[i][0],queries[i][1][k+1],[1 if  j>queries[i][0] else 0 for j in arr[queries[i][1][k]:queries[i][1][k+1]]]] for i in range(len(queries))  for k in list(range(len(queries[i][1]) - 1))]
        step2 = [tuple for x in [j for j in set(arr)]  for tuple in res if tuple[0] == x] 
        k = len(step2)
        running_add= [0]*k
        for i in range(k): 
            if  step2[i][0] == step2[i-1][0]    and 1 not in step2[i][2] :             
                running_add[i] = running_add[i-1] + 1
            elif step2[i][0] == step2[i-1][0]   and 1 not in step2[i][2] :             
                running_add[i] = 1
            elif 1 not in step2[i][2] and step2[i][1] != step2[i-1][1]:                     
                running_add[i] = 1    
            else :
                running_add[i] = 0
               
        return 2*sum(running_add)


    def JimSkyscrapers(arr):
        arr.append(2**64)
        idx, routes = 0, 0
        stack, m = [], {}
        while idx < len(arr):
            if stack == [] or arr[idx] <= stack[-1]:
                stack.append(arr[idx])
                if arr[idx] in m:
                    m[arr[idx]] += 1
                else:
                    m[arr[idx]] = 1
                idx += 1
            else:
                top = stack.pop()
                if top in m and top < arr[idx]:
                    routes += m[top] * (m[top] - 1) 
                    del m[top]
        return(routes)



    def timeConversion(str1):
        """
        Given a time in -hour AM/PM format, convert it to military (24-hour) time.
        Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

        :return:  a string representing time in  24-hour format
        :rtype:  String
        
        :Example:
        >>> time_string = 07:05:45PM
        >>> timeConversion(time_string) 
        >>> 19:05:45
        """
        if str1[-2:] == "AM" and str1[:2] == "12": 
            return "00" + str1[2:-2]     
        elif str1[-2:] == "AM": 
            return str1[:-2] 

        elif str1[-2:] == "PM" and str1[:2] == "12": 
            return str1[:-2]        
        else: 
            return str(int(str1[:2]) + 12) + str1[2:8]        




    def kangaroo(x1, v1, x2, v2):
        """
        Function to figure out a way to get two kangaroos at the same location at the same time .
            x1, v1: integers, starting position and jump distance for kangaroo 1
            x2, v2: integers, starting position and jump distance for kangaroo 2

        :return:  a string YES or NO
        :rtype:  String
        
        :Example:
        >>> kangaroo(0,2,5,3)
        >>> 'NO'
        >>> kangaroo(0,3,4,2)
        >>> 'YES'
        >>> kangaroo(0,2,5,3)
        >>> 'NO'
        """

        num = x2 - x1
        den = v1 - v2
        if den == 0 and  num != 0:
            return 'NO'
        elif num / den >=1 and  (num / den).is_integer():
            return 'YES'
        else:
            return 'NO'

    def formingMagicSquare(s):
        """
        We define a magic square to be an n x n matrix of distinct positive integers from 1 to n2 where the sum of any row, column, or diagonal of length n is always equal to the same number: the magic constant.

        You will be given a 3 x 3 matrix s of integers in the inclusive range [1, 9]. 
        We can convert any digit a to any other digit b in the range [1, 9] at cost of [a - b]. Given s, convert it into a magic square at minimal cost. Print this cost on a new line.
        :return:  the minimal total cost of converting the input square to a magic square
        :rtype:  Int
        
        :Example:
        >>> s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

            
        The matrix looks like this:
        5 3 4
        1 5 8
        6 4 2

        We can convert it to the following magic square:

        8 3 4
        1 5 9
        6 7 2

 
        This took three replacements at a cost of |5 - 8|+ |8 - 9| + |4 - 7|= 7

        >>> formingMagicSquare(s)
        >>> 7
        """
       def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield list(lst[i:i + n])

        seq = list(range(1,10))
        perm = permutations(seq)
        perm_list = [list(chunks(P,3)) for P in perm if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15)]
        perm_list_square = [lst for lst in perm_list]
        return min([sum([abs(s[i][j] - b[i][j])  for i in list(range(0,3)) for j in list(range(0,3))]) for b in perm_list])






    def extraLongFactorials(n):
        """
        To compute the factoriel of n 
            n! = n x (n-1) x (n-2) x ... x 2 x 1

        :return:  The facoriel of n
        :rtype:  Int
        
        :Example:
        >>> extraLongFactorials(2)
        >>> 2
        >>> extraLongFactorials(25)
        >>> 15511210043330985984000000           
        """       
        if(n==0):
            result = 1
        else:
            result = n*extraLongFactorials(n-1)
        return result




    def getTotalX(a, b):
         """
        You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

            1- The elements of the first array are all factors of the integer being considered
            2- The integer being considered is a factor of all elements of the second array

        :return:   the number of integers that are considered to be between a and b.
        :rtype:  INTEGER
        
        :Example:
        >>> a= [2, 4]
        >>> b= [16, 32 ,96]
        >>> getTotalX(a, b)

        >>> a= [3 ,4]
        >>> b= [24, 48]
        >>> getTotalX(a, b)         
        """        
        max_a = max(a)
        min_b = min(b)+1
        Z = list(range(max_a,min_b))  
        W = [x for x in Z for i in list(range(len(a))) if x%a[i] ==0]
        Q = list(set([y for y in W if len([x for x in W if x == y]) == len(a)]))
        D = [s for s in  Q  for i in list(range(len(b))) if b[i]%s ==0]
        return len([a for a in Q if len([x for x in D if x == a]) == len(b)]) 




def climbingLeaderboard(ranked, player):
    """
    An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
        - The player with the highest score is ranked number 1 on the leaderboard.
        - Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

    :input:   
        - The existing leaderboard, "ranked" , is in descending order.
        - The player's scores, "player", are in ascending order.

    :return:  List of the updates ranking

    :rtype:  Liste of INTEGER

    :Example:
    >>> ranked= [100, 100, 50, 40, 40, 20, 10]
    >>> player= [5,25, 50, 120]
    >>> climbingLeaderboard(ranked, player)
    >>> [6, 4, 2, 1]
    >>> ranked= [100, 90, 90, 80, 75, 60]
    >>> player= [50, 65, 77, 90, 102]
    >>> climbingLeaderboard(ranked, player)
    >>> [6, 5, 4, 2, 1]
    """  
    listA = sorted(list(set(ranked)), reverse=True)
    res = []
    for k in player: 
        while len(listA) > 0 and listA[-1] <= k:
            del listA[-1]           
        res.append(len(listA) + 1)          
    return res



def circularArrayRotation(a, k, queries):
    """
    For each array, perform a number of right circular rotations and return the value of the element at a given index.

     :input:     
        a: an array of integers to rotate
        k: an integer, the rotation count
        queries: an array of integers, the indices to report

    :return:   For each query, print the value of the element at index  of the rotated array on a new line.
    :rtype:  Liste of INTEGER

    :Example:
    >>> a= [3,4,5,4]
    >>> k= 2
    >>> queries= [0,1,2,3]
    >>> circularArrayRotation(a, k, queries)
    >>> [5, 4, 3, 4]
    """ 
    n = len(a)
    rot = [l for l in {l: v for l, v in sorted({(a[i],i):(i+k)%n for i in list(range(n))}.items(), key=lambda item: item[1])}]
    return([rot[i][0] for i in queries])


def breakingRecords(scores):
    """
    Given the scores for a season, find the number of times He breaks her records for most and least points scored during the season.

     :input:     
        scores: contains n space-separated integers describing the respective values of scores(0), scores(1), scores(2), ..., scores(n)

    :return:   Numbers of times the best (highest) score increased and the worst (lowest) score decreased.
    :rtype:  Liste of INTEGER (two space-seperated integers)

    :Example:
    >>> scores = [3,4,21,36,10,28,35,5,24,42]
    >>> breakingRecords(scores)
    >>> [4, 0]
    >>>  
    >>> scores = [10, 5, 20, 20, 4, 5 ,2 ,25 ,1]
    >>> breakingRecords(score2)
    >>> [2, 4]
    """ 
    n = len(scores)
    def highestRecords(a,n):
        highest = [a[i] for i in  list(range(n))]
        for i in list(range(1,n)): 
            while highest[i] < highest[i-1] and i < n:
                highest[i] = highest[i-1]
                break 
        return highest
    def LowestRecords(a,n):
        Lowest = [a[i] for i in  list(range(n))]
        for i in list(range(1,n)): 
            while Lowest[i] > Lowest[i-1] and i < n:
                Lowest[i] = Lowest[i-1]
                break 
        return Lowest
    a_1 = highestRecords(scores,n)
    brokeHighest = 0
    for i in list(range(n)): 
        while a_1[i] > a_1[i-1] and i < n:
            brokeHighest += 1
            break
    b_1 = LowestRecords(scores,n)
    brokeLowest = 0
    for i in list(range(n)): 
        while b_1[i] < b_1[i-1] and i < n:
            brokeLowest += 1
            break
    return [brokeHighest, brokeLowest]







def birthday(s, d, m):
    """
    Given the scores for a season, find the number of times He breaks her records for most and least points scored during the season.

     :input:     
        s: an array of integers, the numbers on each of the squares of chocolate
        d: an integer, Ron's birth day
        m: an integer, Ron's birth month

    :return:   an integer denoting the number of ways Lily can divide the chocolate bar.
    :rtype: INTEGER 

    :Example:
    >>> Q =[1, 2 ,1 ,3 ,2] 
    >>> birthday(Q, 3, 2)
    >>> 2
    """ 
    l = m
    k = d
    n = len(s)
    if(n==1):
        result = 1
    else:
        b = [sum(S) for S in [s[i:i+l] for i in  list(range(n-2))]] 
        nb = 0
        for i in list(range(len(b))): 
            while b[i] == k:
                nb += 1
                break
        result = nb
    return result


def absolutePermutation(n, k):
    if k == 0:
        return [i+1 for i in range(n)]
    elif n % (2*k) != 0 or 2*k > n: 
        return [-1]
    return [(i+1)+(1 if (i//k)%2==0 else -1)*k for i in range(n)]





def saveThePrisoner(n, m, s):
    return ((s - 1 + m - 1) % n) + 1


def nonDivisibleSubset(k, s):
    d = [c for c in [[sorted([j for j in s if  (j+i)%k == 0 and j != i]),i,len([j for j in s if  (j+i)%k == 0 and j != i])] for i in s ] if len(c[0]) > 1] 
    rankDel = sorted([[c[1], len(c[0])] for c in d], key=lambda valRank: valRank[1], reverse=True)
    
    for l in rankDel:
        c = [n for n in s if n != l[0]]
        print(l[0])
        while len([w for w in [(c[i] + c[j])%k  for i in list(range(len(c)))  for j in list(range(len(c))) if i != j and i > j] if w == 0]) >= 1:
            print(len([w for w in [(c[i] + c[j])%k  for i in list(range(len(c)))  for j in list(range(len(c))) if i != j and i > j] if w == 0]))
            s.remove(l[0])
            break   
    return len(s)



