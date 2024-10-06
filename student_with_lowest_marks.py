
# Define the file path
studentFilePath = "C:\\Users\\pc\\Downloads\\Compressed\\io\\students_scores.txt"  # Make sure the file path is correct

lowest_mark = float('inf')  # Set initial lowest mark to infinity
students_with_lowest_score = []  # List to store names of students with the lowest score

# Read the file and process the scores
with open(studentFilePath, 'r') as studentFile:
    for student in studentFile:
        each_student = student.strip()  # Remove any leading/trailing whitespace/newline characters
        name, mark_str = each_student.split(":")  # Split the line into name and mark
        student_mark = int(mark_str.strip())  # Convert the mark to an integer

        # Determine if the current mark is lower than the current lowest mark
        if student_mark < lowest_mark:
            lowest_mark = student_mark  # Update the lowest mark
            students_with_lowest_score = [name]  # Reset the list with the current student's name
        elif student_mark == lowest_mark:
            students_with_lowest_score.append(name)  # Add the current student's name to the list

# Output the results
if students_with_lowest_score:
    print(f'The lowest score is {lowest_mark}, and the following students received this score:')
    for student in students_with_lowest_score:
        print(student)
    print(f'Total number of students with the lowest score: {len(students_with_lowest_score)}')
else:
    print('No students found in the file.')
