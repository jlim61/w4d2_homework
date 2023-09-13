# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function


# 'stop gninnips my sdrow' challenge:

# Write a function that takes in a string of one or more words,
# and returns the same string,
# but with all five or more letter words reversed.
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.


'''
I think will need to break the string into a list and split them separately. then target each word and reverse them.
only letter and spaces so don't need to worry about it having numbers. spaces only when more than one word present.
'''

string1 = 'stop gninnips my sdrow'
string2 = 'eno owt eerht ruof evif'
string3 = '          word     drow        test             tset'
string4 = 'This is a coding challenge'

def rev_string(astring):
    astring = astring.split()
    final_string = ""
    rev_words = []
    print(astring)
    for word in astring:
        word_reversed = word[::-1]
        print(word_reversed)
        rev_words.append(word_reversed)
        print(rev_words)
    while len(final_string) < len(rev_words):
        for word2 in rev_words:
            if word2 != rev_words[-1]:
                final_string += "".join(word2 + " ")
            else:
                final_string += "".join(word2)
    print(final_string)
    return final_string





rev_string(string1)
rev_string(string2)
rev_string(string3)
rev_string(string4)


# hether Method, forgot to account for word len of 5 in my example

def astring_edit(astring):
    empty_string = []
    for word in astring.split():
        if len(word) >= 5:
            empty_string.append(word[::-1])
        else:
            empty_string.append(word)
    return ' '.join(empty_string)

print(astring_edit(string1))
print(astring_edit(string2))
print(astring_edit(string3))
print(astring_edit(string4))

'''
O(n + m)
def astring_edit(astring):
    empty_string = [] -> O(1)
    for word in astring.split(): -> O(n) + O(n) -> O(n)
        if len(word) >= 5: -> O(1)
            empty_string.append(word[::-1]) -> O(m) -> m is average length of each word
        else:
            empty_string.append(word) -> O(1)
    return ' '.join(empty_string) -> O(n)
'''