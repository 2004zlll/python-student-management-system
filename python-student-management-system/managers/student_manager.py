import json
from models.student import Student
from pathlib import Path
DATA_FILE = Path(__file__).resolve().parent.parent / "students.json"
class StudentManager:
    def __init__(self):
        self.students=[]
        self.load_from_file()

    def add_student(self, student):
        if not isinstance(student, Student):
            print("只能添加Student对象。")
            return
        if not student.scores:
            print("至少需要一门有效成绩")
            return
        for stu in self.students:
            if stu.student_id == student.student_id:
                print("当前学号已存在")
                return

        self.students.append(student)
        self.save_to_file()
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_to_file()
                return
        print("学生学号有误")
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    def show_all(self):
        for student in self.students:
            print(student)
    def get_average(self):
        total=0
        count=0
        for student in self.students:
            total+=sum(student.scores)
            count+=len(student.scores)
        if count:
            return total/count
        else:
            return None
    def save_to_file(self):
        students_data=[]
        for student in self.students:
            data={'name':student.name,
                  'age':student.age,
                  'student_id':student.student_id,
                  'scores':student.scores}
            students_data.append(data)
        print("开始保存 JSON 文件...")
        with open(DATA_FILE,'w',encoding='utf-8') as f:
            json.dump(students_data,f,ensure_ascii=False,indent=4)

        
    def load_from_file(self):
        try:
            with open(DATA_FILE,'r',encoding='utf-8') as f:
                data=json.load(f)
            if not isinstance(data,list):
                return
            required_fields = ['name', 'age', 'student_id', 'scores']


            for item in data:
                if not isinstance(item, dict):
                    continue

                if not all(key in item for key in required_fields):
                    continue
                if not isinstance(item['name'], str) or not item['name'].strip():
                    continue

                if type(item['age']) is not int:
                    continue

                if not 1 <= item['age'] <= 150:
                    continue

                if not isinstance(item['student_id'], str) or not item['student_id'].strip():
                    continue
                scores = item['scores']

                if not isinstance(scores, list) or not scores:
                    continue

                valid_scores = True

                for score in scores:
                    if type(score) is not int or not 0 <= score <= 100:
                        valid_scores = False
                        break

                if not valid_scores:
                    continue
                student=Student(item['name'],
                                item['age'],
                                item['student_id'],
                                item['scores'])
                self.students.append(student)

        except FileNotFoundError:
            return
        except json.JSONDecodeError as e:
            print("JSON 文件格式错误：", e)