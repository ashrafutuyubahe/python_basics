studentFilePath = "C:\\Users\\pc\\Downloads\\Compressed\\io\\students_scores.txt"  # Ensure the file extension is included
lowest_mark = float('inf')  # Set to infinity to ensure any mark will be lower initially

with open(studentFilePath, 'r') as studentFile:
    for student in studentFile:
        each_student = student.strip()  # Remove leading/trailing whitespace/newline characters
        student_mark = int(each_student.split(":")[1].strip())  # Convert the mark to an integer

        # Check if the current student's mark is lower than the lowest_mark
        if student_mark < lowest_mark:
            lowest_mark = student_mark

# Check if lowest_mark was updated
if lowest_mark == float('inf'):
    print("No marks found.")
else:
    print('The lowest mark is {}'.format(lowest_mark))
