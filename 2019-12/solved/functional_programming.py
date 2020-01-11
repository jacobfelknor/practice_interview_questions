# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element
#  of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(f):
    def left(a, b):
        return a

    return f(left)


def cdr(f):
    def right(a, b):
        return b

    return f(right)


if __name__ == "__main__":

    """ So here's how this works....

        1. First, cons is evaluated with arguments a,b.
        
        2. Cons returns the pair function, which takes a 
           function as its argument and evals that function
           with the original a and b arguments
        
        3. Then, either cdr or car is called. These functions
           take a function (in this case, the pair func) as 
           an argument. It will then call the function given
           as an argument (again, the pair func in this case)
           with the argument right or left, where right & left
           are also functions.

        4. Finally, it will call pair(right) or pair(left).
           pair will evaluate the given function with args
           a and b, set earlier. So the resulting func calls
           are right(a,b) and left(a,b) printing the results

    """
    print(car(cons(3, 4)))  # prints 3
    print(cdr(cons(3, 4)))  # prints 4

