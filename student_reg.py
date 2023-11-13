import random
import datetime
#@ function for performing 5 different operations

## path of different file 
student_file = 'C:\\Users\\ASUS\\Desktop\\Sudip_assignment\\code\\students.txt'
course_file = 'C:\\Users\\ASUS\\Desktop\\Sudip_assignment\\code\\courses.txt'
pass_file = 'C:\\Users\\ASUS\\Desktop\\Sudip_assignment\\code\\passed.txt'
# adding student
def add_student():
    print("Names should contain only letters and start with capital letters.")
    first_name = input("Enter the first name of the student\n")
    last_name = input("Enter the last name of the student\n")
    bool = (first_name.isalpha() & last_name.isalpha() & first_name[0].isupper() & last_name[0].isupper() )
    if bool != True:
         add_student()
    while True:
     major = str(input("Select the student's major:\n\tCE: Computation Engineering\n\tEE: Electrical Engineering\n\tME: Mechanical Engineering\n\tSE: Software Engineering\nWhat is your selection?\n"))
     if major in ['CE','EE','ET','ME','SE']:
         break
     else:
         continue
    email_add = f'{first_name}.{last_name}@lut.fi'
    year = datetime.datetime.now().year
    # Function to check if a number is unique in the file
    def is_unique_number(number, filename):
        with open(filename, 'r') as file:
            for line in file:
                if str(number) == line.strip():
                    return False
        return True
    while True:  
        study_num = random.randint(10000,99999) 
        if is_unique_number(study_num, student_file):
            break
    with open(student_file,'a') as file:
         student_data = f'{study_num},{first_name},{last_name},{year},{email_add}'
         print(student_data)
         file.write(student_data + '\n')
         print("Student added successfully!")

         
# searching student
def search_student():
    matched = []
    while(1):
        student_input = input("Give at least 3 characters of students first or last name :\n")
        length = len(student_input)
        if length < 3:
            continue
        else:
            break
    with open(student_file, 'r') as file:
        for line in file:
            if line == None:
                break
            list = line.strip().split(',')
            if len(list) > 3:
                if list[1][:3].lower() == student_input.lower():
                    print("Matching Students:")
                    data = f"ID: {list[0]}, First name: {list[1]}, Last name: {list[2]}\n"
                    matched.append(data)
    for data in matched:
        print(data)
    return matched    

# searching course
def search_course():
    infos = []
    search_ele = input("Give at least 3 characters of the course or the teacher:")
    while True:
        if len(search_ele) < 3:
            continue
        else:
            break
    with open(course_file, 'r') as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) > 3 :
                course_data = data[1]
                teacher_data = data[3]
                if course_data.lower().find(search_ele.lower()) != -1 or teacher_data.lower().find(search_ele.lower() ) != -1:
                    info = f"ID: {data[0]}, Name: {data[1]}, Teacher(s): {data[3]}"
                    infos.append(info)
        for item in infos:
            print(item)
             
    print("course searched")

# adding course complettion
import datetime
import re
pass_file = 'C:\\Users\\ASUS\\Desktop\\Sudip_assignment\\code\\passed.txt'
def add_course():
    # checks and take input untill correct pattern is met
    while True:
        course_id = input("Give the course id: ")
        pattern = re.compile(r'^[A-Z]\d{4}$')
        if pattern.match(course_id):
            break
        else:
            continue
    student_id = input("Enter the student id : \n")
    # checks if grade is out of range or not
    while True:
        grade_up = int(input("Give the grade: "))
        if  grade_up > 5 or grade_up < 1 :
            print("Grade is not a correct grade")
            continue
        else:
            break
    # check if the date is under 30 days or not
    while True:
        current_date_input = input("Enter a date (DD/MM/YYYY):")
        try:
            current_date = datetime.datetime.strptime(current_date_input, '%d/%m/%Y')
        except ValueError:
            print("Invalid date format. Use DD/MM/YYYY. Try again!")
            continue
        today_date = datetime.datetime.now()
        if current_date > today_date:
             print("Input date is later than today. Try again!")
             continue
        else:
            break
    with open(pass_file, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        for line in lines:
            data = line.strip().split(',')
            data_cid = data[0].strip()
            data_sid = data[1].strip()
            data_date = data[2].strip()
            data_gpa = int(data[3].strip())
            previous_date = datetime.datetime.strptime(data_date, '%d/%m/%Y')
            days_gap = (current_date - previous_date).days
            current_student = bool(data_sid == student_id  )
            print(current_student)
            if current_student:
                if days_gap < 30:
                    date = current_date_input
                    if data_gpa < grade_up:
                        print(f"{course_id},{data_sid},{grade_up},{date}\n")
                        old_data = f"{course_id},{data_sid},{previous_date},{data_gpa}\n"
                        new_data = f"{course_id},{data_sid},{date},{grade_up}\n"
                        linee = line.replace(old_data,new_data)
                        print("Updated")
                    else:
                        print(f"Student has already passed the grade with {data_gpa}")
                else:
                    print('Input date is older than 30 days. Contact "opinto".')        
            else:
                 print("no matching student")
         # Write the modified lines back to the file
            file.write(line)
        print('Success')

# show student's record
def display_record():
    count = 0
    total_grade =0 
    total_credit =0
    student_id_input = int(input("Enter Your student ID: \n"))
    with open(student_file,'r') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            student_id = data[0]
            if student_id_input == student_id:
                student_name = data[1]
                starting_year = data[2]
                major = data[3]
                email = data[4]
        with open(pass_file,'r') as pass_files, open(course_file,'r') as course_files:
            pass_file_line = pass_files.readlines()
            course_file_line = course_files.readlines()

            data_packed = []     # because there will be multiple course passed by the student

            # sub_name = ""
            # course_id = ""
            # pass_date = ""
            # credit_hr = 0
            # teacher_name = ""
            # grade = 0
            # student_name = ""
            for pass_line in pass_file_line:
                pass_data = pass_line.strip().split(',')
                
                student_id = pass_data[1]
                if student_id_input == student_id:
                    course_id = pass_data[0]          
                    pass_date = pass_data[2]
                    grade = int(pass_data[3])
                    total_grade = total_grade+grade
                    count = count+1
                    for course_line in course_file_line:
                        course_data = course_line.strip().split(',')
                        course_id_here = course_data[0]
                        if course_id == course_id_here:
                            sub_name = course_data[1]
                            credit_hr = int(course_data[2])
                            total_credit = credit_hr + total_credit
                            teacher_name = course_data[3]
                        data_pack = f'Course ID: {course_id}, Name: {sub_name}, Credits: {credit_hr}, \nDate: {pass_date}, Teacher(s): {teacher_name}, grade: {grade}'
                        data_packed.append(data_pack)
                        print(f"Student ID: {student_id}, \nName: {student_name}\nStarting_year: {starting_year}\nMajor: {major}\nEmail: {email}\nPassed courses:\n")
    for datas in data_packed:
        print(datas)

#@  menu driven system 
is_on =  True
while is_on:
    arguments = int(input("You may select one of the following:\n\t1) Add student\n\t2) Search student\n\t3) Search course\n\t4) Add course completion\n\t5) Show student's record\n\t0) Exit\nWhat is your selection?"))
    match arguments:
                case 0:
                    is_on=False
                case 1:
                    add_student()
                case 2:
                    search_student()
                case 3:
                    search_course()
                case 4:
                    add_course()
                case 5:
                    display_record()
                case _:
                    print("Invalid Input")