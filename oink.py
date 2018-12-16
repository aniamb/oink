input = raw_input("Enter a word: ")
type(input)

first = input[1:]

second = input[0:1]

third = "ay"

pigLatin = first+second+third
print "Pig Latin Translation: " + pigLatin
