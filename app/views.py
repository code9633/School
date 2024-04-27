from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answers, Summary, Awards, Subject

def visualizeData(request):
    
    schools = School.objects.all()
    classes = Class.objects.all()
    assessmentAreas = AssessmentArea.objects.all()
    students = Student.objects.all()
    answers  = Answers.objects.all()
    summaries = Summary.objects.all()
    awards = Awards.objects.all()
    subjects = Subject.objects.all()

    return  render(request, "index.html", {
        'schools' : schools,
        'classes' : classes,
        'assessmentAreas' : assessmentAreas,
        'students' : students,
        'answers' : answers,
        'summaries' : summaries,
        'awards':awards,
        'subjects' : subjects
    })