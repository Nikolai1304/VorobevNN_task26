x = int(input('Введите число: '))
y = int(input('Введите показатель степени: '))

def nums_degree(a, n):
    
    if n == 0:
        return 1
    # elif n == 1:
    #     return a
      
    return a* nums_degree(a,n-1) 
print(nums_degree(x,y))

# работает