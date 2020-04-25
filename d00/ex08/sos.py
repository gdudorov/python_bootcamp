import sys

morze = {' ': '/','A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.'
        }

def print_morze(text):
    i = 0
    for word in text:
        if i != 0:
                print(end="/ ")
        i+=1
        for char in word:
                if char != " ":
                        print (morze[char.upper()], end=" ")
                else:
                        print(end="/ ")

if len(sys.argv) < 1:
       quit(print(end=""))
elif sum(1 for w in sys.argv[1:] for c in w if not c.upper() in morze) > 0:  #sum(1 for w in sys.argv[1:] for c in w if c == "/") != 0:
        quit(print("ERROR", end=""))
print_morze ((sys.argv[1:]))