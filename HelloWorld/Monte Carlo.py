__author__ = 'alihooke'
def coinFlipTrial(M, N):
    """ Performs one sequence of N coin flips and determines if greater than or equal to M
    """


    for i in range(N):
        if (random.random() < M):
            return False
        else:
            return True


