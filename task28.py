x = int(input('Введите первое неотрицательное число: '))
y = int(input('Введите второе неотрицательное число: '))

def nums_summa(a, n):
    
    if n == 0:
        return a
    
    print("x = ", a)
    print("y = ", n)
    # elif a == 0:
    #     return n
      
    return nums_summa(a+1, n-1)

print(nums_summa(x,y))

# работает нормально