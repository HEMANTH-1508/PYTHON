#EMPLOYEE SALARY INCREMENT


salary = int(input("Enter the employee's salary: "))
grade = input("Enter the employee's grade (A or B): ")

if salary < 10000:
    bonus = 0.07 * salary
else:
    if grade == 'A':
        bonus = 0.05 * salary
    elif grade == 'B':
        bonus = 0.1 * salary
    else:
        print("Invalid grade entered.")
        exit()
        
salary_with_bonus = salary + bonus
print("Bonus: $", bonus)
print("Salary with bonus: $", salary_with_bonus)
