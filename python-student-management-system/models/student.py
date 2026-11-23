class Student:
    def __init__(self, name, age, student_id, scores):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.scores = scores
    def cal_avg(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)
    def is_passed(self):
        avg=self.cal_avg()
        return avg is not None and avg >= 60
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 学号: {self.student_id}, 成绩: {self.scores}"
