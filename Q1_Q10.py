def generate_prime_factors (number):
    #generate a list contains the prime factors of number
    n = 2
    prime_factors = []
    while (n <= number):
        while (number % n == 0):
            prime_factors.append (n)
            number /= n
        n += 1
    return prime_factors
    
#http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


'''
Question 1: 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum (number1, number2):
    # calculate the sum of arithmetic sequence
    n = (number2 - 1) / number1
    return n * number1 + (n * (n - 1) * number1) / 2

result = sum(3,1000) + sum(5, 1000) - sum(15, 1000)
print ("Q1 result = " + str(result))


'''
Question 2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

def fib (number):
	'''
	Formula:
		F(2n-1) = F(n)^2+F(n-1)^2
		F(2n) = F(n) * (2F(n-1) + F(n))
	'''
    if number <= 2:
        return 1
    else:
        if (number % 2):
            return (fib(number/2) * fib(number/2) + fib(number/2 + 1) * fib(number/2 + 1))
        else:
            return (fib(number/2) * ( 2 * fib(number/2 + 1) - fib(number/2)))
	
fibn, sum, i = 0, 0, 0
while fibn <= 4000000:
    if (fibn % 2 == 0):
        sum += fibn
    i += 1
    fibn = fib (i)
print ("Q2 result = " + str (sum))


'''
Question 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
n = 2
prime_factors = []
number = 600851475143

prime_factors_list = generate_prime_factors (number)
print prime_factors_list
print max(prime_factors_list)


'''
Question 4:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def palindromic (number):
	# determine whether a number is palindromic
    number_list = []
    while number > 10:
        number_list.append (number % 10)
        number /= 10
    number_list.append (number)
    number_length = len (number_list)
    for i in range (0, number_length/2):
        if number_list[i] != number_list[number_length-1-i]:
            return None
    return True


palindromic_dict = {}
for i in range (999, 100, -1):
    for j in range (999, 100, -1):
        if palindromic (i*j):
           palindromic_dict.update ({i*j: [i, j]})
           
maximum = max(palindromic_dict)
print maximum, palindromic_dict[maximum]


'''
Question 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
i = 20
while (i % 3 or i % 4 or i % 5 or i % 6 or i %  7 or i % 8 or i % 9 or i % 11 or i % 12\
        or i % 13 or i % 14 or i % 15 or i % 16 or i % 17 or i % 18 or i % 19 or i % 20):
    i += 20
print i


'''
Question 6:
The sum of the squares of the first ten natural numbers is,
	1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
# method 1
# (a+b+c)^2 = a^2 + b^2 + c^2 +2ab + 2bc + 2ac
sum = 0
for i in range (1, 101):
    for j in range (i+1, 101):
        if i != j:
            sum += 2 * i * j
print sum

# method 2
# (a+b+c)^2 = a^2 + b^2 + c^2 +2ab + 2bc + 2ac = a^2 + b^2 + c^2 +2a(b + c) + 2bc
sum = 0
for i in range (1, 101):
    sum += (100-i) * (i+101) * i
print sum


'''
Question 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
number = 3
i = 1
prime_list = [2]
while (i < 10001):
    for n in prime_list:
        if (number % n == 0):
            break
    else:
        prime_list.append (number)
        i += 1
    number += 1

print prime_list, prime_list[-1]

'''
Question 8:
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
'''

numbers =  '73167176531330624919225119674426574742355349194934\
            96983520312774506326239578318016984801869478851843\
            85861560789112949495459501737958331952853208805511\
            12540698747158523863050715693290963295227443043557\
            66896648950445244523161731856403098711121722383113\
            62229893423380308135336276614282806444486645238749\
            30358907296290491560440772390713810515859307960866\
            70172427121883998797908792274921901699720888093776\
            65727333001053367881220235421809751254540594752243\
            52584907711670556013604839586446706324415722155397\
            53697817977846174064955149290862569321978468622482\
            83972241375657056057490261407972968652414535100474\
            82166370484403199890008895243450658541227588666881\
            16427171479924442928230863465674813919123162824586\
            17866458359124566529476545682848912883142607690042\
            24219022671055626321111109370544217506941658960408\
            07198403850962455444362981230987879927244284909188\
            84580156166097919133875499200524063689912560717606\
            05886116467109405077541002256983155200055935729725\
            71636269561882670428252483600823257530420752963450'
            
            
list = [int(i) for i in numbers if i is not ' ']

t1 = time.time()
max_value = -1

for index in xrange (988):
    result = 1
    for _ in range(13):
        result *= list [index + _]
    max_value = max (result, max_value)
    
print max_value

'''
Question 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
for a in range (1, 501):
	for b in range (1, 501):
		if (2000*a + 2000*b - 2*a*b == 1000*1000):
			print (a, b, 1000-a-b)
			print a*b*(1000-a-b)


'''
Question 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
# https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False
    
def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1
        
# 9 sec
def solve_number_10():
    # She *is* working on Project Euler #10, I knew it!
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return


