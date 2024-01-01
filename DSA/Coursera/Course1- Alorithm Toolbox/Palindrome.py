from testing import stressTest



def palindromeFinder(string: str) -> bool:
    string = string.lower()
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return palindromeFinder(string[1:-1])
    else:
        return False


string1 = "rotoR"
string2 = "rater"
print(string1[1:-1])
print(palindromeFinder(string1))
