continuation = 1
while (continuation == 1):
    choice = raw_input("For English to Pig Latin, Enter 1. For Pig Latin to English, Press 2: \n")
    actualChoice = int(choice)

    if actualChoice == 1:
        input = raw_input("Enter English: ")
        type(input)

        words = input.split(" ")

        print "Pig Latin Translation: "

        for x in words:
            first = x[1:]
            second = x[0:1]
            third = "ay"

            pigLatin = first+second+third

            print (pigLatin),

        print ""
        keepGoing = raw_input("Would you like to translate another word? Enter Y or N: \n")
        type(keepGoing)
        keepGoing.upper()

        if keepGoing == 'Y' or keepGoing == 'y':
            continuation = 1
        else:
            continuation = 2

    elif actualChoice == 2:
        pInput = raw_input("Enter Pig Latin: ")
        type(pInput)

        print "English Translation: "
        pWords = pInput.split(" ")
        for y in pWords:
            sansAY = y[:-2]
            firstLetter = sansAY[-1:]
            secondHalf = sansAY[:-1]
            print (firstLetter+secondHalf),

        print ""
        keepGoing = raw_input("Would you like to translate another word? Enter Y or N: \n")
        type(keepGoing)
        keepGoing.upper()

        if keepGoing == 'Y' or keepGoing == 'y':
            continuation = 1
        else:
            continuation = 2
    else:
        print("Invalid input")

print "Thanks for Translating."
