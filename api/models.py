from django.db import models
from uuid import uuid4


class Student(models.Model):
    class StudentLevels(models.TextChoices):
        FM = "Freshman", "Freshman"
        JR = "Junior", "Junior"
        SN = "Senior", "Senior"

    id = models.UUIDField(default=uuid4, primary_key=True)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=10)
    level = models.CharField(
        max_length=10, choices=StudentLevels.choices, default=StudentLevels.FM, null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"


class SubjectGrade(models.Model):
    class Subjects(models.TextChoices):
        MATH = "Math", "Math"
        SCIENCE = "Science", "Science"
        HISTORY = "History", "History"

    id = models.UUIDField(primary_key=True, default=uuid4)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='stud_grades')
    subject = models.CharField(max_length=10, choices=Subjects.choices)
    grade = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.f_name}'s {self.subject} Grade: {self.grade}"
