from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)

class Class(models.Model):
    class_name = models.CharField(max_length=255)

class AssessmentArea(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    fullname = models.CharField(max_length=255)

class Answers(models.Model):
    answers = models.CharField(max_length=255)
    
class Awards(models.Model):
    name = models.CharField(max_length=255)

class Subject(models.Model):
    subject = models.CharField(max_length=255)
    subject_score = models.IntegerField(null=True)

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.IntegerField()
    sydney_percentile = models.IntegerField()
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.CharField(max_length=255)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.CharField(max_length=255)
    student_score = models.FloatField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField(default=None, null=True, blank=True)
    year_level_name = models.CharField(max_length=255)
    answer_id = models.IntegerField(default=None, null=True, blank=True)
    correct_answer_id = models.IntegerField(default=None, null=True, blank=True)
    
    



