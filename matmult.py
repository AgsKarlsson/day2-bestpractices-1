# Program to multiply two matrices using nested loops
import random

def generate_matrix(N):
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return (X, Y)

def empty_results():
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

def insert_results():
    
    #insert_results is by far the slowest part of the script,
    #this is where I would focus the optimization if possible
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            #for k in range(len(Y)):
             #   result[i][j] += X[i][k] * Y[k][j]
            result[i][j]=X[i][:]*Y[:][j]
              
def show_results():
    for r in result:
        print(r)

N = 10
(X, Y) = generate_matrix(N)
result=empty_results()
insert_results()
show_results()

