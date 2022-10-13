# Refactored FizzBuzz to use function - thus make it reusable
# Not using classes and objects

def fizz_buzz():

    for i in range(1, 101):
        if i % 15 == 0: # i % 5 == 0 & i % 3 == 0 also viable
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
    return i

print(fizz_buzz())