
def fizz_buzz(n):

    for num in range(1, (n + 1)):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizz_buzz(int(input("n = ")))