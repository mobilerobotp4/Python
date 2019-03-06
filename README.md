# Python
Python code
Problem:Combine Two Strings
We are given 3 strings: str1, str2, and str3. Str3 is said to be a shuffle of str1 and str2 if it can be formed by interleaving 
the characters of str1 and str2 in a way that maintains the left to right ordering of the characters from each string. For example,
given str1=”abc” and str2=”def”, str3=”dabecf” is a valid shuffle since it preserves the character ordering of the two strings.
So, given these 3 strings write a function that detects whether str3 is a valid shuffle of str1 and str2.

Solution:
We will use recursion to solve the problem, but first we check whether the length of str1 plus str2 equals to the length of str3. 
If not, then str3 can’t be a valid shuffle since it contains extra characters, so we return false immediately. Recursion happens as
follows. If the first characters of str1 and str3 are the same, then we’ll recurse with new str1 and str3 being all but first 
characters of the strings, and str2 will stay the same. If first characters of str2 and str3 are the same, then we’ll do the same 
thing with new str2 and str3 being all but first characters, and str1 the same. Now this is the same problem with shorter strings,
so it’s very suitable for recursion. If neither str1’s nor str2’s first character equals str3’s first character, we return false.
The base case of the recursion is, if any of the strings is empty then the concatenation of str1 and str2 should be equal to str3.


