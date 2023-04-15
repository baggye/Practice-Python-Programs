
"""return true if s is a pangram, return false if not"""
def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s:
            return False
    return True
is_pangram(input())