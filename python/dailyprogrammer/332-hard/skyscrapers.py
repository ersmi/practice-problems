import sys #sys.argv
import itertools #itertools.permutations

ITER_LIMIT = 1000000

def parseInput():
    ''' Initialize using cli specified file '''
    with open(sys.argv[-1], 'r') as fd:
        size = int(fd.readline())
        height_limits = map(int, fd.readline().split(' '))
    return size, height_limits

def evalLine(heights):
    ''' Take list of heights and determine number "seen" '''
    seen = 0
    tallest = 0
    for h in heights:
        if h > tallest:
            tallest = h
            seen += 1
    return seen

def checkSolution(size, height_limits, grid):
    ''' 
    Check columns and rows in `grid` satisfy the requirements in `height_limits`
    
    Each column is sorted to during the process with O(nlog(n)) complexity.
    Each row and column must be iterated through to be checked, resulting in O(n^2) complexity.
    '''
    # Clockwise rotation around the grid
    for x in range(size*4):
        if x < size: # Columns
            heights = [ y[x] for y in grid ]
        elif x < size*2: # Reversed Rows
            heights = grid[x-size][::-1]
        elif x < size*3: # Reversed Columns
            heights = [ y[(size*2)-x-1] for y in grid ][::-1]
        else: # Rows
            heights = grid[(size*3)-x-1]
        if evalLine(heights) != height_limits[x] and height_limits[x] != 0:
            return False

    # Also need to check column values are unique
    for x in range(size):
        col = [y[x] for y in grid]
        if sorted(col) != range(1,size+1):
            return False

    return True
    
# Based on DrYap's StackOverflow response on 'Variable number of loops'
# https://stackoverflow.com/questions/18165937/variable-number-of-nested-for-loops
def buildPerms(size, height_limits, grid, loop_level=0, iters=0):
    '''
    Iterate through all possible permutations of each row
    
    The else branch is recursively called `size` times to generate the grid permutations.
    The if statement is hit for each possible combination of the `size` permutations
      and checks the solution for correctness.
  
    The recursive calls result in O(2^k) time complexity where k is the time complexity
      of the if branch (in this case O(n^2))
    '''
    if loop_level == size:
        if checkSolution(size, height_limits, grid):
            return grid
        elif iters > ITER_LIMIT:
            raise Exception('Iteration limit reached: %s' % iters)
        else:
            return False
    else:
        for x in itertools.permutations(range(1,size+1)):
            iters += 1
            grid[loop_level] = x
            # Check if more recursive loops are needed, otherwise start iterating.
            if loop_level != size:
                # If we're returned a grid, we've got a valid solution
                # Otherwise we continue to iterate
                if buildPerms(size, height_limits, grid, loop_level+1, iters):
                    return grid
        # If we've fallen out of all loops, return no solution.
        if loop_level == 0:
            return 'No solution exists'
                
def exhaustiveSearch():
    ''' 
    Exhaustive search for nxn skyscraper problem solution. 
    
    Has an overall time complexity of O(2^(n^2)) and is therefore unsuitable for n >= 5
    '''
    size, height_limits = parseInput()
    return buildPerms(size, height_limits, [0]*size)

print exhaustiveSearch()