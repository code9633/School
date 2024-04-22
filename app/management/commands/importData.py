import csv
from django.core.management.base import BaseCommand
from app.models import School, Class, AssessmentArea, Student, Answers, Summary, Awards, Subject

class Command(BaseCommand):
    help = 'Import data from CSV files'

    def handle(self, *args, **options):
        # CSV file paths
        csv_files = [
            'csv/Ganison_dataset_1.csv',
            'csv/Ganison_dataset_2.csv',
            'csv/ganison_dataset_3.csv',
            'csv/ganison_dataset_4.csv',
            'csv/ganison_dataset_5.csv',
            'csv/ganison_dataset_6.csv'
        ]
        

        for csv_file in csv_files:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Extract data from the row
                    school_name = row['school_name']
                    year = row['year']
                    student_id = row['StudentID']
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    # Extract other fields...

                    # Create School object
                    school, _ = School.objects.get_or_create(name=school_name)

                    # Create Class object
                    class_name = row['Class']
                    class_obj, _ = Class.objects.get_or_create(class_name=class_name)

                    # Create AssessmentArea object
                    assessment_area_name = row['Assessment Areas']
                    assessment_area, _ = AssessmentArea.objects.get_or_create(name=assessment_area_name)

                    # Create Student object
                    student, _ = Student.objects.get_or_create(fullname=first_name + ' ' + last_name)

                    # Create Answers object
                    answers = row['Answers']
                    answers_obj, _ = Answers.objects.get_or_create(answers=answers)

                    # Create Awards object
                    award_name = row['award']
                    award, _ = Awards.objects.get_or_create(name=award_name)

                    # Create Subject object
                    subject_name = row['Subject']
                    subject_score = row.get('subject_score', None)
                    subject, _ = Subject.objects.get_or_create(subject=subject_name, subject_score=subject_score)

                    # Create Summary object
                    # Create Summary object
                    summary = Summary(
                        school=school,
                        sydney_participant=row['sydney_participants'],
                        sydney_percentile=row['sydney_percentile'],
                        assessment_area=assessment_area,
                        award=award,
                        class_id=class_obj,
                        correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],
                        correct_answer=row.get('correct_answer', ''),
                        student=student,
                        participant=row['participant'],
                        student_score=row['student_score'],
                        subject_id=subject,
                        category_id = row.get('category_id', None),
                        year_level_name=row.get('year_level_name', ''),
                        answer_id=row.get('answer_id', '') if row.get('answer_id', '') else None,
                        correct_answer_id=row.get('correct_answer_id', '') if row.get('correct_answer_id', '') else None,
                    )

                    summary.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
        

