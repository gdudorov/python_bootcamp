import string

def text_analyzer(text = "empty"):
    if text == "empty":
        return (print("You have provided no text. Please input something", end=""))
    print("The text contains", sum(1 for c in text), "characters:")
    print("-", sum(1 for c in text if c.isupper()), "upper letters")
    print("-", sum(1 for c in text if c.islower()), "lower letters")
    count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
    print ("-", count(text, string.punctuation),"punctuation marks")
    print("-", sum(1 for c in text if c.isspace()), "spaces")

text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
