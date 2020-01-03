

def translate(phrase):
    TranslateFinal = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                TranslateFinal = TranslateFinal + "G"
            else :
                TranslateFinal = TranslateFinal + "g"
        else:
            TranslateFinal = TranslateFinal + letter
    return TranslateFinal


print(translate(input("Enter a word: ")))










