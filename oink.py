
input = raw_input("Enter a word: ")
type(input)

words = input.split(" ")

print "Pig Latin Translation: "

for x in words:
    first = x[1:]
    second = x[0:1]
    third = "ay"

    pigLatin = first+second+third

    print pigLatin
