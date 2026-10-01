grade_counter = 1
approved_count = 0
failed_count = 0
approved_average = 0
failed_average = 0
total_average = 0

total_grades = int(input("Ingrese la cantidad de notas:"))

while grade_counter <= total_grades:
    current_grade = int(input(f"Ingrese la nota número {grade_counter}: "))
    if current_grade < 70:
        failed_count = failed_count + 1
        failed_average = failed_average + current_grade
    else:
        approved_count = approved_count + 1
        approved_average = approved_average + current_grade
    total_average = total_average + (current_grade / total_grades)
    grade_counter = grade_counter + 1

if failed_count > 0:
    failed_average = failed_average / failed_count
else:
    failed_average = 0

if approved_count > 0:
    approved_average = approved_average / approved_count
else:
    approved_average = 0

print (f"El estudiante tiene esta cantidad de notas aprobadas: {approved_count}")
print (f"Este es el promedio de notas aprobadas: {approved_average}")
print (f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_count}")
print (f"Este es el promedio de notas desaprobadas: {failed_average}")
print (f"Este es el promedio total de notas: {total_average}")
