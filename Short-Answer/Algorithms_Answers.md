#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) runtime is O(n), since it takes the n times before breaking the while loop.


b) the first loop is n, and the second loop is adding j^2. So the time complexity should be O(n + sqrt(n)).


c) it is O(n) because it runs n -1 times recursively.

## Exercise II

I would pick the middle floor (n/2) to start the test. Then if the egg doesn't break, I will recursively keep applying the same (n/2) reasoning until finding the floor where the egg breaks. Whenever that happens, by applying the same methodology, I would test whether the egg breaks or not when throwing it from 1 floor below the "breaking floor". That is the floor that will be returned by my function. The runtime complexity is the square root of n since it keeps cutting in half the number of trials on the "floor looking process".


