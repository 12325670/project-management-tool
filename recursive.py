# recursion problem : repeating somwthing in self siilar way
# adding two nubers
# def add (x,y):
#     tot=x
#     if y==0:
#         return x
def fact_rec(x):
    if x == 1:
        return 1
    else:
        return(x * fact_rec (x-1))
print(fact_rec())