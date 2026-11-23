# Python 学生信息管理系统

一个基于 Python 面向对象编程实现的命令行学生信息管理系统，支持学生信息管理、成绩统计以及 JSON 文件持久化存储。

## 一、项目功能

- 添加学生：录入学生姓名、年龄、学号和成绩。
- 删除学生：根据学号删除学生信息。
- 查询学生：根据学号查找学生。
- 显示学生：展示所有学生信息。
- 成绩统计：计算所有学生的平均成绩。
- 数据持久化：通过 JSON 文件保存和加载学生数据。
- 数据校验：对学生信息、成绩和 JSON 数据进行合法性检查。
- 异常处理：使用自定义异常处理不合法的年龄输入。

## 二、技术栈

- Python
- 面向对象编程（OOP）
- JSON 数据序列化与反序列化
- pathlib 文件路径管理
- 自定义异常与异常处理
- Python 模块化开发

## 三、项目结构

```text
python-student-management-system/
│
├── README.md
│
└── python-student-management-system/
    │
    ├── main.py
    │
    ├── managers/
    │   ├── __init__.py
    │   └── student_manager.py
    │
    ├── models/
    │   ├── __init__.py
    │   └── student.py
    │
    └── utils/
        ├── __init__.py
        ├── menu.py
        └── exceptions.py
```

## 四、运行方法

1. 确保本地已安装 Python 3。
2. 克隆项目：

```bash
git clone https://github.com/2004zlll/python-student-management-system.git
```

3. 进入项目代码目录：

```bash
cd python-student-management-system/python-student-management-system
```

4. 运行程序：

```bash
python main.py
```

## 五、项目学习内容

通过本项目实践了以下 Python 知识：

- 类与对象、构造方法、实例属性和实例方法
- 模块拆分与跨模块导入
- 列表、字典及循环操作
- 文件读写与 JSON 数据处理
- 异常处理与自定义异常
- 数据合法性校验
- pathlib 路径管理
- Git 与 GitHub 版本管理

## 六、后续改进方向

- 增加学生信息修改功能
- 增加单个学生的成绩统计与查询
- 增加自动化单元测试
- 后续考虑接入 MySQL 数据库

