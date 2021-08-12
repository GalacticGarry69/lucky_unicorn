show_instructions = input("Have you played this game before?")

# if they say yes, cutput 'program continues'
if show_instructions == "yes" or show_instructions == "y":
    show_instructions = "yes"
    print("program continues")
# if they say no, output 'display instructions'
elif show_instructions == "no"or show_instructions == "n":
    show_instructions = "no"
    print("display instructions")
else:
    print("Please answer yes / no")
