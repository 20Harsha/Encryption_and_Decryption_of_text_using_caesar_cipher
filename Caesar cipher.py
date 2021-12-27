w='''
 _______    _______    _______    _______    _______    _______          _______   _________   _______               _______    _______ 
(  ____ \  (  ___  )  (  ____ \  (  ____ \  (  ___  )  (  ____ )        (  ____ \  \__   __/  (  ____ )  |\     /|  (  ____ \  (  ____ )
| (    \/  | (   ) |  | (    \/  | (    \/  | (   ) |  | (    )|        | (    \/     ) (     | (    )|  | )   ( |  | (    \/  | (    )|
| |        | (___) |  | (__      | (_____   | (___) |  | (____)|        | |           | |     | (____)|  | (___) |  | (__      | (____)|
| |        |  ___  |  |  __)     (_____  )  |  ___  |  |     __)        | |           | |     |  _____)  |  ___  |  |  __)     |     __)
| |        | (   ) |  | (              ) |  | (   ) |  | (\ (           | |           | |     | (        | (   ) |  | (        | (\ (   
| (____/\  | )   ( |  | (____/\  /\____) |  | )   ( |  | ) \ \__        | (____/\  ___) (___  | )        | )   ( |  | (____/\  | ) \ \__
(_______/  |/     \|  (_______/  \_______)  |/     \|  |/   \__/        (_______/  \_______/  |/         |/     \|  (_______/  |/   \__/
                                                                                                                                        
                                                                                                                                                                                                                                  
'''
print(w)
global shift
while True:
    '''In the variable alphabet twice the alphabets are their because when shift gets added to index and if it exceeds 26 that is z so
    it can again start from 'a' so twice alphabets are taken for example if z is the letter and we have shift plus 2 so next 2 characters
    are not their if we use just 26 letters so to avoid the error we used it twice so when z is their its next 2 charaters are a and b
    so that problem is solved.'''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print(len(alphabet))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrpyt:\n")
    text = input("Type your message:\n").lower()

    '''Shift is the global variable assigned it using global keyword outside the loop.
    if the shift is greater then 52 we take mode otherwise no changes has been done on the shift value'''
    shift = int(input("Type the shift number:\n"))
    if shift >=52:
        shift = shift % 26

    def caesar(text, shift, direction):

        s1 = []  # to find index of that letter in alphabet
        for i in text:
            if i not in alphabet:  # this if is used because their might be other special chracters or spaces might be their
                s1.append(i)
            else:
                o = alphabet.index(i)
                s1.append(o)  # that index is stored in list

        def encode():
            s = []  # takes text and store all in s as list
            for i in range(0, len(text)):
                s.append(text[i])
            print(s)
            for i in range(0, len(s)):
                if s[i] not in alphabet:
                    s[i]=s[i]
                else:
                    '''S1 contains the index of that value so we add shift to its index
                     fetch the particular index value from alphabet'''
                    s[i] = alphabet[s1[i] + shift]

            z = ""
            z = z.join(s) #using join to combine the text
            print(f"The encoded text is {z}")

        def decode():
            s = []  # takes text and store all in s as list
            for i in range(0, len(text)):
                s.append(text[i])
            print(s)
            for i in range(0, len(s)):
                if s[i] not in alphabet:
                    s[i]=s[i]
                else:
                    '''S1 contains the index of that value so we subtract shift to its index
                    fetch the particular index value from alphabet'''
                    s[i] = alphabet[s1[i] - shift]  # adding to index
            z = ""
            z = z.join(s) #using join to combine the text
            print(f"The decoded text is {z}")

        if direction == "encode":
            encode()
        elif direction == "decode":
            decode()
        else:
            print("invalid")


    caesar(text, shift, direction)  #calling the function
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    n = input()
    if n=='yes':
        continue #Continue statement is used to continue the loop
    else:
        print("Goodbye")
        break #Break statement is used to exit the loop