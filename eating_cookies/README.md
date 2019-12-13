# Eating Cookies

Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

Thus, `eating_cookies(3)` should return an answer of 4.

## Testing

For this problem, there's a test that tests your implementation with small inputs (n <= 10). There's also a separate test that tests your implementation with large inputs (n >= 50). 

You'll find that without implementing performance optimizations into your solution, your solution will likely hang on the large input test. 

To run the tests separately, run `python test_eating_cookies.py -k small` in order to run just the small input test. Run `python test_eating_cookies.py -k large` to execute just the large input test. If you want to run both tests, just run `python test_eating_cookies.py`.

You can also test your implementation manually by executing `python eating_cookies.py [n]`.

## Hints

 * Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
 * Think about base cases that we would want our recursive function to stop recursing on. How many ways are there to eat 0 cookies? What about a negative number of cookies? 
 * Once we've established some base cases, how can we recursively call our function such that we move towards one or more of these base cases?
 * As far as performance optimizations go, caching/memoization might be one avenue we could go down? How should we make a cache available to our recursive function through multiple recursive calls?

# example of a fibcache
fibcache = {}
def  sum_fibonacci(n):
    """Compute the nth Fibonacci number.

    >>> sum_fibonacci(35)
    9227465
    >>> sum_fibonacci(10)
    55
    >>> sum_fibonacci(0)
    0
    >>> sum_fibonacci(1)
    1
    >>> sum_fibonacci(5)
    5
    """
    if n == 0:
        fibcache[n] = 0
        return fibcache[n]
    elif n == 1:
        fibcache[n] = 1
        return fibcache[n]
    else:
        sum_left = 0
        sum_right = 0
        if n-2 in fibcache.keys():
            sum_left += fibcache[n-2]
        else:
            sum_left += sum_fibonacci(n-2)
            fibcache[n-2] = sum_left
        if n-1 in fibcache.keys():
            sum_right += fibcache[n-1]
        else:
            sum_right += sum_fibonacci(n-1)
            fibcache[n-1] = sum_right
        return sum_left + sum_right