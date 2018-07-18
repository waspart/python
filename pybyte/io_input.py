def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")

t = (',', ' ')
for s in t:
    something = something.replace(s, '')

if is_palindrome(something):
    print('Yes!')
else:
    print('No!')
