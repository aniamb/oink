continuation = 1
while (continuation == 1):
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

        keepGoing = raw_input("Would you like to translate another word? Enter Y or N: \n")
        type(keepGoing)

        if keepGoing == "Y":
            continuation = 1
        else:
            continuation = 2

    elif choice == 2:
        pInput = raw_input("Enter Pig Latin: ")
        type(pInput)

        print "Pig Latin Translation: "
        pWords = pInput.split(" ")
        for y in pWords:
            sansAY = y[:-2]
            firstLetter = sansAY[-1:]
            secondHalf = sansAY[:-1]
            print firstLetter+secondHalf

        keepGoing = raw_input("Would you like to translate another word? Enter Y or N: \n")
        type(keepGoing)

        if keepGoing == "Y":
            continuation = 1
        else:
            continuation = 2
    else:
        print("Invalid input")
