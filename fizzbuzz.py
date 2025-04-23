for i in range(1, 18):
    if i % 3 == 0 or i % 5 == 0:
        print('fizz'*(i%3==0) + 'Buzz'*(i%5==0))
    else:
        print(f'{i}')
