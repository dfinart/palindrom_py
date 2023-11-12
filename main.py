def isPalindrome(s): 
          
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return print("Палиндром")
    return print("Не палиндром")

s = input("Введите слово:")
isPalindrome(s) 