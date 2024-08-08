import random as R
import string

coding = input("Enter what you want to do:\n A. coding \n B. Decoding \n").lower()

if coding == "a":
    st = input("Enter The word to code :\n")
    words = st.split()
    new_words = []
    for word in words:
        if len(word) >= 3:
            r1 = ''.join(R.choices(string.ascii_letters, k=4))  # Generate random 4-letter prefix
            r2 = ''.join(R.choices(string.ascii_letters, k=4))  # Generate random 4-letter suffix
            stword = r1 + word[1:] + word[0] + r2  # Encode: move first letter to end
            new_words.append(stword)
        else:
            new_words.append(word[::-1])  # Reverse words with fewer than 3 letters
    print(" ".join(new_words))
else:
    st = input("Enter the Word to Decode :\n")
    words = st.split()
    new_words = []
    for word in words:
        if len(word) >= 3:
            stword = word[4:-4]  # Remove 4-letter prefix and suffix
            stword = stword[-1] + stword[:-1]  # Decode: move last letter to start
            new_words.append(stword)
        else:
            new_words.append(word[::-1])  # Reverse words with fewer than 3 letters
    print(" ".join(new_words))
#Author:-
print("Author:-")
print('''\n\nMade by Ishant Yadav
    with ❤️  in
      India ''')
