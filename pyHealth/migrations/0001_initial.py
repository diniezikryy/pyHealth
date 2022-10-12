# Generated by Django 4.1.2 on 2022-10-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Age', models.PositiveIntegerField()),
                ('Attrition', models.CharField(max_length=30)),
                ('BusinessTravel', models.CharField(max_length=30)),
                ('DailyRate', models.IntegerField(max_length=30)),
                ('Department', models.CharField(max_length=30)),
                ('DistanceFromHome', models.IntegerField(max_length=30)),
                ('Education', models.IntegerField(max_length=30)),
                ('EducationField', models.CharField(default='', max_length=30)),
                ('EmployeeCount', models.IntegerField(max_length=30)),
                ('EnvironmentSatisfaction', models.IntegerField(max_length=1)),
                ('Gender', models.CharField(max_length=10)),
                ('HourlyRate', models.IntegerField(max_length=30)),
                ('JobInvolvement', models.IntegerField(max_length=1)),
                ('JobLevel', models.IntegerField(max_length=1)),
                ('JobRole', models.CharField(default='', max_length=99)),
                ('JobSatisfaction', models.IntegerField(max_length=1)),
                ('MaritalStatus', models.CharField(max_length=30)),
                ('MonthlyIncome', models.IntegerField(max_length=30)),
                ('MonthlyRate', models.IntegerField(max_length=30)),
                ('NumCompaniesWorked', models.IntegerField(max_length=30)),
                ('Over18', models.CharField(max_length=1)),
                ('OverTime', models.CharField(max_length=30)),
                ('PercentSalaryHike', models.IntegerField(max_length=3)),
                ('PerformanceRating', models.IntegerField(max_length=1)),
                ('RelationshipSatisfaction', models.IntegerField(max_length=1)),
                ('StandardHours', models.IntegerField(max_length=4)),
                ('Shift', models.CharField(default='', max_length=1)),
                ('TotalWorkingYears', models.IntegerField(max_length=2)),
                ('TrainingTimesLastYear', models.IntegerField(max_length=2)),
                ('WorkLifeBalance', models.IntegerField(max_length=1)),
                ('YearsAtCompany', models.IntegerField(max_length=2)),
                ('YearsInCurrentRole', models.IntegerField(default=0, max_length=2)),
                ('YearsSinceLastPromotion', models.IntegerField(max_length=2)),
                ('YearsWithCurrManager', models.IntegerField(max_length=2)),
            ],
        ),
    ]