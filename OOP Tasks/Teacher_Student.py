# Create Student and Teacher classes
# Student
# learn() -> prints: the student is actually learning
# question(teacher) -> calls the teacher's giveAnswer() method
# Teacher
# teach(student) -> calls the student's learn() method
# giveAnswer() -> prints: the teacher is answering a question
# Instantiate a Student and Teacher object
# Call the student's question() method and the teacher's teach() method

class Student():
    def __init__(self, name):
        self.name=name
      
    
    def question():
        print("I have a question")
    
    def learn():
        print("I am actually learning")
    
class Teacher(Student):
    def __init__(self,name, input):
        self.name=name
        self.input=input

    def giveAnswer():
        print ("The teacher is answering a question")
    
    def teach():
        pass
     

        

student=Student
teacher=Teacher


student.question()
# teacher.giveAnswer()

teacher.teach()