def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input("How much would you like to play with?"))

            # if the amount is to low / too high give
            if 0 < response <= 10:
                print("You have asked to play with ${}".format(response))

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here...
how_much = num_check("how much would you like to play with? ",1,10)


