
def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
            continue
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
            continue
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())
    #updated to table

fizzBuzz(15)
