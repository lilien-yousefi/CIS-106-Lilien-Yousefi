# comment - Lilien Yousefi

def compbattingavg(hits, atbats):
    battingavg = hits / atbats

    if atbats == 0:
        return 0.0

    return battingavg

def main():
    playercount = 0

    while True:
        r = input("Do you want to enter player data? (Yes or No): ")
        if r == "yes":
            lastname = input("Enter player's last name: ")
            hits = int(input("Enter number of hits: "))
            atbats = int(input("Enter number of at-bats: "))

        battingavg = compbattingavg(hits, atbats)
        playercount += 1

        print("Player's Last Name is: ", lastname)
        print("Player's Batting Average is: ", battingavg)
        print("Total Number of Players: ", playercount)

main()