# CHALLENGE ONE
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# CHALLENGE TWO
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

# CHALLENGE THREE
# f = open("file1.txt", "r")
# result = [int(n) for n in f if n in open("file2.txt", "r")]
# print(result)

# CHALLENGE FOUR
# HINT -> passed_students = {student:score for (student, score) in students_scores.items() if score > 70}
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# CHALLENGE FIVE
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
