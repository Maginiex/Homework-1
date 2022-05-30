print('Введите два числа!')
num_one=int(input())
num_two=int(input())
print('Выберите операцию \n 1 - Умножение \n 2 - Деление \n 3 - Сложение \n 4 - Вычетание \n')
task=int(input())
if task == 1:
    result=num_one*num_two
    print('ваше вычесление '+str(num_one)+'*'+str(num_two)+'='+str(result))
if task == 2:
    result=num_one/num_two
    print('ваше вычесление '+str(num_one)+'/'+str(num_two)+'='+str(result))
if task == 3:
    result=num_one+num_two
    print('ваше вычесление '+str(num_one)+'+'+str(num_two)+'='+str(result))
if task == 4:
    result=num_one-num_two
    print('ваше вычесление '+str(num_one)+'-'+str(num_two)+'='+str(result))