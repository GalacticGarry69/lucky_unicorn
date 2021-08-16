import random

# main routine goes here
tokens = ("unicorn", "horse", "zebra", "donkey")
balance = 60

# testing loop to generate 20 tokens
for iterm in range(0,20):
    chosen = random.choice(tokens)

    # adjust balance
    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

    # output
    print("Tokens: {} , Balance: ${}".format(chosen, balance))
