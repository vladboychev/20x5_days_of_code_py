print("Welcome to the secret auction!")
auction_dict = {}


def auction():
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    auction_dict[name] = bid

    def end_auction():
        highest_bid = 0
        bidder = ''
        for key in auction_dict:
            if auction_dict[key] > highest_bid:
                highest_bid = auction_dict[key]
                bidder = key

        print(f"The winner is {bidder} with a bid of ${highest_bid}.")

    bidders = True
    while bidders:
        game = input("Are there any other bidders? Y or N: ").lower()
        if game == "y":
            auction()
        bidders = False
        end_auction()


auction()
