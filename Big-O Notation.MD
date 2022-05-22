Big-O Notation is a way of expressing an upper bound on the execution time or space requirements of an algorithm.

PRACTICE
-------------------------------------
1. O(n+100) -> O(n) #Kep the highest term (linear time)
2. O(100*n) -> O(n) # Constant multiples are ignores
3. O(50) -> O(1) Reduces to 1 (constants time)
4. O(n^2 + n^3) -> Pick the highest term
5. O(n+n+n+n+n) -> O(n) Throw away constants (linear time) 