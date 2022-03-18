def isPalindrome(self, s: str) -> bool:
    if len(s) <= 1:
        return True

    abc = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
    lower = s.lower()
    string = []

    i = 0
    while i < len(lower):
        if lower[i] in abc:
            string.append(lower[i])
        i+=1

    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True
