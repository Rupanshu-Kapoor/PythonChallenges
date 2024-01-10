from testing import stressTest

def palindrome(str, i , j):
    if i >= j:
        return True
    if str[i] != str[j]:
        return False
    return palindrome(str, i+1, j-1)



def palindromeFinder(string: str) -> bool:
    string = string.lower()
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return palindromeFinder(string[1:-1])
    else:
        return False


string1 = "rotor"
string2 = "rater"
print(palindromeFinder(string1))
print(palindrome(string1,0,len(string1)-1))
