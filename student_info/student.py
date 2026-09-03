class Student:
    def __init__(self, name, roll_no, class_name, mobile_no):
        self.name = name
        self.roll_no = roll_no
        self.class_name = class_name
        self.mobile_no = mobile_no

    def display_student_info(self):
        print("\n--- Student Information ---")
        print("Name      :", self.name)
        print("Roll No   :", self.roll_no)
        print("Class     :", self.class_name)
        print("Mobile No :", self.mobile_no)

