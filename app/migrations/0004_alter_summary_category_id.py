# Generated by Django 5.0.4 on 2024-04-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_subject_subject_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='category_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
