
choice = input("For English to Pig Latin, Enter 1. For Pig Latin to English, Press 2: \n")
type(choice)

if choice == 1:
    input = raw_input("Enter English: ")
    type(input)

    words = input.split(" ")

    print "Pig Latin Translation: "

    for x in words:
        first = x[1:]
        second = x[0:1]
        third = "ay"

        pigLatin = first+second+third

        print pigLatin
elif choice == 2:
    pInput = raw_input("Enter Pig Latin: ")
    type(pInput)

    pWords = pInput.split(" ")
    print pInput
    print pInput[:-2]
else:
    print("Invalid input")
