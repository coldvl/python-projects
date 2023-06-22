employees = {"Іванов", "Петров", "Сидоров", "Ігнатенко", "Коваленко"}

filtered_employees = [employee for employee in employees if employee.startswith("І")]

print(filtered_employees)