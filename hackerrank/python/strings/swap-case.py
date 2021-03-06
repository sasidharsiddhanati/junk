# # -*- coding: utf-8 -*-
# You are given a string SS. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format

# A single line containing a string SS.

# Constraints

# 0<len(S)≤10000<len(S)≤1000
# Output Format

# Print the modified string SS.

# Sample Input

# HackerRank.com presents "Pythonist 2".
# Sample Output

# hACKERrANK.COM PRESENTS "pYTHONIST 2".

s=input()
print(s.swapcase())