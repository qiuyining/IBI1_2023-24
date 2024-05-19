# Define a class to show student's information
class Student:
     # Initialize a new instance of Student
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score
        
    # print the student's information
    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")

# example 
student = Student("A", "BMI", 100, 100, 100)
student.print_details()
