def isPalindrome(s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]
# print(isPalindrome('racecar'))


def isPalindromeTwoPointer(s: str) -> bool:
    l, r = 0, len(s)-1 #set left to index 0 and right to length of the string - 1 (which will give last index of array string)

    while l < r:
         #these two while loops advance the pointers if they are not alphanumeric (white space, symbols)
         while l < r and not alphaNum(s[l]):
            l += 1
         while r > l and not alphaNum(s[r]):
              r -= 1
         
         if s[l].lower() != s[r].lower():
              return False
         l, r = l + 1, r - 1
    return True
        
def alphaNum(c): # helper function
    (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

print(isPalindromeTwoPointer('racecar'))

