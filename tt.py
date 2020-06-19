

n = int(input().strip())

result = n % 2

if result == 0 or range(2, 5):
     print('Not Weird')

if result == 0 and result > 20:
    print('Not Weird')

if result == 0 and range(6,20):
    print('Weird')

elif result == 1:
     print('Weird')



