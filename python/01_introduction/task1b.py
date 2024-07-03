def isVowel(str):

    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if str in vowel:

        #print ("It is a vowel")
        print(f"'{str}' is a vowel")
    else:
        print(f"'{str}' is not a vowel")
isVowel('a')
isVowel('d')