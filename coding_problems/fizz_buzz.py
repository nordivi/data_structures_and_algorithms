# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizz_buzz(n):
    res = []
    for i in range(1, n+1):
        string = ''
        if not i % 3:
            string += 'Fizz'
        if not i % 5:
            string += 'Buzz'
        if string:
            res.append(string)
        else:
            res.append(str(i))
    return res