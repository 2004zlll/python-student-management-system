from managers.student_manager import StudentManager
from utils.menu import show
from models.student import Student
from utils.exceptions import AgeError
def main():
    manager=StudentManager()
    while(True):
        show()
        choice = input("请输入操作编号: ")
        if choice == '1':
            name = input("请输入学生姓名: ").strip()
            if not name:
                print("姓名不能为空")
                continue
            try:
                age = int(input("请输入学生年龄: "))
                if age<1 or age>150:
                    raise AgeError("年龄不合法")
            except AgeError as e:
                print(e)
                continue
            except ValueError:
                 print("年龄必须输入整数")
                 continue
            student_id = input("请输入学生学号: ").strip()
            if not student_id:
                print('学号不能为空')
                continue
            scores = []
            for num in input("请输入学生成绩：").split(','):
                try:
                    score=int(num.strip())
                except ValueError:
                    print("请输入有效整数数字")
                    continue
                if 0<=score<=100:
                    scores.append(score)
                else:
                    print("成绩范围为0-100")
            
            student = Student(name, age, student_id, scores)
            manager.add_student(student)
        elif choice == '2':
            student_id = input("请输入要删除的学生学号: ").strip()
            manager.remove_student(student_id)
        elif choice == '3':
            student_id = input("请输入要查找的学生学号: ").strip()
            student = manager.find_student(student_id)
            if student:
                print(student)
            else:
                print("未找到该学生。")
        elif choice == '4':
            manager.show_all()
        elif choice == '5':
            avg_score = manager.get_average()
            if avg_score is not None:
                print(f"所有学生的平均成绩为: {avg_score:.2f}")
            else:
                print("当前没有可以统计的数字")
        elif choice == '0':
            break
        else:
            print("无效的操作编号，请重新输入。")

if __name__=='__main__':
    main()