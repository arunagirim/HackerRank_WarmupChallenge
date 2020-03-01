# Complete the countingValleys function below.
def countingValleys(n, s):
    h=0
    v=0
    for i in s:
        if i=='U':
            h=h+1
        else:
            h=h-1
        if h==0 and i=='U':
            v=v+1
    return v
