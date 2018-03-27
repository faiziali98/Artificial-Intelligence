word=raw_input("Enter the word: ")
revword = ""
for i in reversed(word):
    revword += i
if (revword==word):
    print("Palindrome")
else :
    print("Not a palindrome")