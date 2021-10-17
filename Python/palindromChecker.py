word = input("Enter any word:")
originalWord = word.lower()
reverseWord = word[ : :-1].lower()

if originalWord==reverseWord :
    print(word+" is PALINDROME")
else:
    print(word+" is not PALINDROME")