
def fizz_buzz(n):

     for num in range(1, (n + 1)):
        print(num)

        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')

fizz_buzz(int(input("n = ")))

# Это не работает как показано в примере, но как сделать не могу додуматься! Fizz Buzz FizzBuzz
# печатается после числа, а не вместо! Подскажите, пожалуйста, как сделать.
# Могу вывести # только простой список.у вывести только простой список

def fizz_buzz(n):

    for n in range(1, (n + 1)):
        print(n)

fizz_buzz(int(input("n = ")))