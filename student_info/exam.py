class Exam:
    def __init__(self, marks):
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_result(self):
        if self.calculate_average() >= 40:
            return "PASS"
        else:
            return "FAIL"

    def display_exam_info(self):
        print("\n--- Examination Information ---")

        for i, mark in enumerate(self.marks, start=1):
            print("Semester", i, "Marks:", mark)

        print("Cumulative Average :", self.calculate_average())
        print("Result              :", self.calculate_result())
