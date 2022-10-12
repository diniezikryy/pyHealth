from pyHealth.models import Employee
import csv

def run():
    with open('/Users/diniezikry/Desktop/tiara project/pyHealth/scripts/data.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Employee.objects.all().delete()

        for row in reader:
            employee = Employee(
                EmployeeId=int(row[0]),
                Age=int(row[1]),
                Attrition = row[2],
                BusinessTravel = row[3],
                DailyRate = int(row[4]),
                Department = row[5],
                DistanceFromHome = row[6],
                Education = int(row[7]),
                EducationField = row[8],
                EmployeeCount = int(row[9]),
                EnvironmentSatisfaction = int(row[10]),
                Gender = row[11],
                HourlyRate = int(row[12]),
                JobInvolvement = int(row[13]),
                JobLevel = int(row[14]),
                JobRole = row[15],
                JobSatisfaction = int(row[16]),
                MaritalStatus = row[17],
                MonthlyIncome = int(row[18]),
                MonthlyRate = int(row[19]),
                NumCompaniesWorked = int(row[20]),
                Over18 = row[21],
                OverTime = row[22],
                PercentSalaryHike = int(row[23]),
                PerformanceRating = int(row[24]),
                RelationshipSatisfaction = int(row[25]),
                StandardHours = int(row[26]),
                Shift = row[27],
                TotalWorkingYears = int(row[28]),
                TrainingTimesLastYear = int(row[29]),
                WorkLifeBalance = int(row[30]),
                YearsAtCompany = int(row[31]),
                YearsInCurrentRole = int(row[32]),
                YearsSinceLastPromotion = int(row[33]),
                YearsWithCurrManager = int(row[34]),
            )

            employee.save()

            