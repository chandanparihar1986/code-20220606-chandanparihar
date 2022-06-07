"""
Author: Chandan Parihar
Date: 06-June-2022
Description: Just a demo file to show a basic functionality of this program.
Date                Name                 Description
06-06-2022           CP                  Demo project
"""

from BMICalculator import BMICalculator
from logger import lLogger
"""
    Assuming there would be high volume of data to be processed where the data comes in from the source system at 1 MM/sec rate, we can build the solution
    using two approaches
        1. Extend this solution and build a PySpark application using the same classes as used here
        2. Extend this solution and build a multithreaded application using the same classes as used here
"""


if __name__ == '__main__':
    print("Log file can be found at /tmp/bmicalculator.log")
    # Problem statment 1- Calculate the BMI using the given Table 1 and add three new columns
    persons =  [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
                { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
                { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
                { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
                {"Gender": "Male", "HeightCm": 167, "WeightKg": 82}]

    personsBMICalculator=[BMICalculator(person.get("Gender"), person.get("HeightCm"), person.get("WeightKg")) for person in persons]
    count_overweight = filter(lambda p:p.bmi_category=="Overweight",personsBMICalculator)
    lLogger.info("======================Start iterating over the filtered object===============================")
    for p in count_overweight:
        lLogger.info("Gender: {}, Weight :{}, BMI: {}, Category: {}, Risk: {}".format( p.gender, p.weight, p.bmi, p.bmi_category, p.health_risk))
    lLogger.info("======================End of the iteration over the filtered object===============================")
    lLogger.info("Number of overweight people is {}".format(len(list(count_overweight))))
