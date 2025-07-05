# comment - Lilien Yousefi


def compute_tuition(credit_hours, district_code):
    district_code = district_code.upper()
    if district_code == 'I':
        rate = 250.0
    elif district_code == 'O':
        rate = 550.0

    tuition = credit_hours * rate
    return tuition

def main():
    total_tuition = 0.0

    while True:
        response = input("Do you want to enter student data? (Yes or No): ")
        if response != 'yes':
            break

        last_name = input("Enter student's last name: ")
        credit_hours = float(input("Enter number of credit hours: "))
        district_code = input("Enter district code (I or O): ")

        tuition = compute_tuition(credit_hours, district_code)

        total_tuition += tuition

        print("Student's Last Name is: ", last_name)
        print("Tuition owed: $", tuition)


    print("Total tuition owed by all students: $", total_tuition)

main()
