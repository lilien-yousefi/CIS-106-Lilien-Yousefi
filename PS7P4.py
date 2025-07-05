# comment - Lilien Yousefi


def compute_pay(job_code, hours):
    job_code = job_code.upper()

    if job_code == 'L':
        rate = 25.0
    elif job_code == 'A':
        rate = 30.0
    elif job_code == 'J':
        rate = 50.0

    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate

    return rate, gross_pay


def main():
    total_gross_pay = 0.0

    while True:
        response = input("Do you want to enter employee data? (Yes or No): ")
        if response != 'yes':
            break

        last_name = input("Enter employee's last name: ")
        job_code = input("Enter job code (L, A, or J): ")
        hours_worked = float(input("Enter hours worked: "))

        rate, gross = compute_pay(job_code, hours_worked)

        total_gross_pay += gross

        print("Employee's Last Name is: ", last_name)
        print("Hours Worked: ", hours_worked)
        print("Pay Rate: $", rate)
        print("Gross Pay: $", gross)


    print("Total Gross Pay for all employees: $", total_gross_pay)

main()
