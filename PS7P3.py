# comment - Lilien Yousefi


def compute_mpg_and_cost(miles, gallons):
    if gallons == 0:
        mpg = 0.0
    else:
        mpg = miles / gallons
    cost = gallons * 3.00
    return mpg, cost

def main():
    trip_count = 0
    total_miles = 0
    total_gas_cost = 0.0

    while True:
        response = input("Do you want to enter trip data? (Yes or No): ")
        if response != 'yes':
            break

        city = input("Enter destination city: ")
        miles = float(input("Enter miles traveled: "))
        gallons = float(input("Enter gallons used: "))


        mpg, cost = compute_mpg_and_cost(miles, gallons)


        trip_count += 1
        total_miles += miles
        total_gas_cost += cost


        print("Trip to :", city)
        print("Miles traveled: ", miles)
        print("Miles per gallon: ", mpg)
        print("Gas cost: $", cost)


    print("Total trips: ", trip_count)
    print("Total miles traveled: ", total_miles)
    print("Total gas cost: $", total_gas_cost)

main()
