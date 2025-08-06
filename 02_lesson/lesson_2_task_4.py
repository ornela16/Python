
def fizz_buzz(n):

    for num in range(1, (n + 1)):

        if (num % 3 == 0 and num % 5 == 0):
            print('FizzBuzz')
        else:

            if (num % 3 == 0):
                print('Fizz')
            else:

                if (num % 5 == 0):
                    print('Buzz')
                else:
                    print(num)

fizz_buzz(int(input("n = ")))

# fizz_buzz(18)

# простой список

# def fizz_buzz(n):
#
#     for n in range(1, (n + 1)):
#         print(n)
#
# fizz_buzz(int(input("n = ")))