# 6.00 Problem Set 7 

# This problem set is designed to help you solidify your understanding of some
# material that we have covered in lecture, but not emphasized on the programming
# problems. You should do it, but do NOT hand it in.

# 1) What is the computational complexity of fact0? Explain your answer.
def fact0(i):
    assert type(i) == int and i >= 0
    if i == 0 or i == 1:
        return 1
    return i * fact0(i-1)
# T(i) = 2 + 3 + 2 + T(i-1) = 7 + T(i-1)
# T(i-1)= 7 + 7 + T(i-2)
# T(i) = 7k + T(i-k)    -->  i-k=1 -> k=i-1
# T(i) = 7(i-1) + T(1) = 7i -7 + 5 = 7i - 2
# O(n) -> Linear


# 2) What is the computational complexity of fact1? Explain your answer.
def fact1(i):
    assert type(i) == int and i >= 0
    res = 1
    while i > 1:
        res = res * i
        i -= 1
    return res
# T(i) = 3 + (1 + 1 + 1)i = 3 + 3i
# O(n) -> Linear


# 3) What is the computational complexity of makeSet? Explain your answer.
def makeSet(s):
    assert type(s) == str
    res = ''
    for c in s:
        if not c in res:
            res = res + c
    return res
# T(s) = 1 + (1+1)s = 1 + 2(len(s))
# O(n) -> Linear


# 4) What is the computational complexity of intersect? Explain your answer.
def intersect(s1, s2):
    assert type(s1) == str and type(s2) == str
    s1 = makeSet(s1)
    s2 = makeSet(s2)
    res = ''
    for e in s1:
        if e in s2:
            res = res + e
    return res
# T(s1, s2) = 2 + 1+2(len(s1)) + 1 + 2(len(s2)) + (len(s1)*(len(s2))
# = 3 + 2(len(s1)) + 2(len(s2)) + len(s1)*len(s2)
# O(s1*s2) -> if s1==s2 -> O(n^2) -> Quadratic


# 5) Present a hand simulation of the code below. Describe the value to which each
# identifier is bound after each step of the computation. Note that “s1” and “s2” exist
# in more than one scope
def swap0(s1, s2):
    assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    s1 = s2[:]
    s2 = tmp
    return
s1 = [1]
s2 = [2]
swap0(s1, s2)
print(s1, s2)
# |              global                  |
# |                |      function       |
# |   s1   |   s2  |  tmp  |  s1  |  s2  |
# |   [1]  |   [2] |  [1]  | [2]  | [1]  |
# |   [1]  |   [2] |                     |

# 6) Present a hand simulation of the following code: 
def swap1(s1, s2):
    assert type(s1) == list and type(s2) == list
    return s2, s1
s1 = [1]
s2 = [2]
s1, s2 = swap1(s1, s2)
print(s1, s2)
# |              global           |
# |                |  function    |
# |   s1   |   s2  |  s1   |  s2  |
# |   [1]  |   [2] |  [1]  | [2]  |
# |   [2]  |   [1] |              |

# 7) Present a hand simulation of the following code: 
def rev(s):
    assert type(s) == list
    for i in range(int(len(s)/2)):
        tmp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp
s = [1,2,3]
rev(s)
print(s)
# |              global                                 |
# |                |      function        |             |
# |       s        |   tmp    |     s     |      s      |
# |   [1, 2, 3]    |    1     | [3, 2, 3] |  [3, 2, 3]  |
# |   [3, 2, 3]    |    1     | [3, 2, 1] |  [3, 2, 1]  |
# |   [3, 2, 1]    |                      |             |


if __name__ == "__main__":
    print("fact0")
    print(fact0(5))
    print("fact1")
    print(fact1(5))
    print("makeSet")
    print(makeSet("abcab"))
    print("intersect")
    print(intersect("abcabdef", "abcfd"))