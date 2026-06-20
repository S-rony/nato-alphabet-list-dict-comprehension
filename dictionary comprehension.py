name = ["Alex","Beth","Carolina","Dave", "Elanor","Freddie"]
#over 60 add new item to the passed_students dictionary
import random
student_scores = {student:random.randint(1,100) for student in name }
passed_student = {student:score for student,score in student_scores.items() if score>=60}
print(passed_student)