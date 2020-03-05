# ECOR 1051 Lab 12 File: lab12-linearRegression.py


from typing import Set, Tuple
# See Practical Programming, Chapter 8, section Type Annotations For Lists,
# and Chapter 11, first paragraph of section Creating New Type Annotations. 

def get_points() -> Set[Tuple[float, float]]:
    """Return a set of (x, y) points.
    
    >>> get_points()
    {(1.0, 5.0), (3.5, 12.5), (2.0, 8.0)}
    # The order of the points may vary, depending on how sets are implemented
    # in the version of Python you're using.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}

#exercise 3
def fit_line_to_points(points: Set[Tuple[float, float]]) -> Tuple[float, float]:
    """The function returns a tuple, which contains the slope and intercept of 
    the best-fit straight line through the points.
    >>>fit_line_to_points(get_points())
    (2.0,3.0)
    """
    sumx=0
    sumy=0
    sumxx=0
    sumxy=0
    sumyy=0
    for i in points:
        sumx+=i[0]
        sumy+=i[1]
        sumxy+=i[0]*i[1]
        sumxx+=i[0]*i[0]
        sumyy+=i[1]*i[1]
    m=(sumx*sumy-len(points)*sumxy)/(sumx*sumx-len(points)*sumxx) 
    b=(sumx*sumxy-sumxx*sumy)/(sumx*sumx-len(points)*sumxx)
    new_tuple=m,b
    return new_tuple

#exercise 4
a=fit_line_to_points(get_points())
print('the best_line is y=',a[0],'x+',a[1],sep='')

#exercise 5
def read_and_print_lines()->None:
    infile = open('lab12-data.txt','r') 
    for line in infile:   
        print(line) 
    infile.close()
read_and_print_lines()


#Exercise7 and 8
def read_point(filename: str) ->Set[Tuple[float, float]]:
    """This function takes one argument, which is the name of a text file. Each
    line in the text file will contain two real numbers, which represent the x 
    and y coordinates of one point. The function will return a set of tuples,
    with each tuple containing one (x, y) point
    >>>read_points('lab12-data.txt')
    {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}
    >>>read_points('lab12-data2.txt')
    {(3.0, 2.0), (3.1, 6.8), (1.5, 2.6), (4.0, 6.0)}
    """        
    points=open(filename,'r')
    result=set()
    for i in points:
        numbers = i.split()
        a=(float(numbers[0]), float(numbers[1]))
        result.add(a)
    return result
r7 =read_point('lab12-data.txt')
print(r7)

r8=fit_line_to_points(read_point(input()))
print('the best fit line is y =', r8[0],'x +', r8[1], sep='')
