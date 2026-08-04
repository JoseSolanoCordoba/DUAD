
number_of_approved = 0
number_of_unapproved = 0
total = 0
approved_sum = 0
unapproved_sum = 0
approved_average = 0
unapproved_average = 0

number_of_notes = int(input("Ingrese cuántas notas quieres revisar:\n"))

for _ in range(0,number_of_notes):
    grade = int(input("Ingrese la nota:\n"))
    total = total + grade
    if grade<70:
        unapproved_sum += grade
        number_of_unapproved += 1
    else:
        approved_sum += grade
        number_of_approved += 1

total_average = total/number_of_notes
if number_of_approved!=0: 
    approved_average = approved_sum/number_of_approved
if number_of_unapproved!=0:
    unapproved_average = unapproved_sum/number_of_unapproved

print("El número de notas aprobadas es:", number_of_approved,"\n")
print("El número de notas desaprobadas es:", number_of_unapproved,"\n")
print("El promedio de todas es:", total_average,"\n")
print("El promedio de las aprobadas es:", approved_average,"\n")
print("El promedio de las desaprobadas es:", unapproved_average,"\n")
