def palindrom_check():
    n=input("Enter the Word:")
    if n==n[::-1]:
        print("The word is a palindrome")
    else:
        print("Naaaah!!!. that's not a palidrome")

palindrom_check()