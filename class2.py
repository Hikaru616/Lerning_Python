class Student:
    
    school_name = 'ABC学園'
    student_name = '太郎'
    
    def display_school_name(self):
        print(f"{self.school_name} : {self.student_name}")
        
    def set_school_name(self, name):
        self.school_name = name
        
    def set_name(self, student_name):
        self.student_name = student_name
        
        
student_1 = Student()
student_2 = Student()
Student.school_name =  'DEF学園'

student_1.set_school_name('GHI学園')
student_1.set_name('三郎')
print(student_1.display_school_name(), student_2.display_school_name())
