class Student:
    
    school_name = 'ABC学園'
    
    def display_info(self):
        print(f"{self.school_name} : {self.name}")
        
    def set_school_name(self, name):
        self.school_name = name
        
    def set_name(self, name):
        self.name = name
        
        
student_1 = Student()
student_2 = Student()
Student.school_name =  'DEF学園'

# student_1.set_school_name('GHI学園')
# student_1.set_name('三郎')
# print(student_1.display_school_name(), student_2.display_school_name())

student_1.set_name('太郎')
student_2.set_name('次郎')
student_1.display_info()
student_2.display_info()