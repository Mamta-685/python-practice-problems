#My approach*********************

def is_palindrome(sent):
    length = len(sent)

    if length == 0:  # edge case
        return False

    if length % 2 == 0:
        left = sent[:length // 2]
        right = sent[length // 2:]
    else:
        left = sent[:length // 2]
        right = sent[length // 2 + 1:]

    return left == right[::-1]


#optimal solution*************************

def is_palindrome2(sentence):
    sentence = sentence.lower().replace(" ", "")
    return sentence == sentence[::-1]

print(is_palindrome("eye"))
print(is_palindrome("racecar"))

print(is_palindrome2("Harry"))
print(is_palindrome2("racecar"))
