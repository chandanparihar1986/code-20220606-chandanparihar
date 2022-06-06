

import unittest
from BMICalculator import BMICalculator
from logger import lLogger

"""
Author: Chandan Parihar
Date: 06-June-2022
Description: This class covers all test cases with respect to the BMI calculator including covering edge cases
Date                Name                 Description
06-06-2022           CP                  Demo project
"""

class BMICalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        lLogger.info("Setting up an mocked json object that acts as a defualt test object")
        self.persons = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                        {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                        {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                        {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                        {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                        {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

    def testAddBMIColumns(self):
        personsBMICalculator = [BMICalculator(person.get("Gender"), person.get("HeightCm"), person.get("WeightKg"))
                                for person in self.persons]
        for person in personsBMICalculator:
           self.assertEqual(person.bmi !=None and person.bmi_category != None and person.health_risk !=None, True, "Error adding new columns")

        lLogger.info("Successfully tested addition of 3 columns")

    # Check the number of default people in the default object
    def testOverweightcase1(self):
        personsBMICalculator = [BMICalculator(person.get("Gender"), person.get("HeightCm"), person.get("WeightKg"))
                                for person in self.persons]
        count_overweight = filter(lambda p: p.bmi_category == "Overweight", personsBMICalculator)
        self.assertEqual(len(list(count_overweight)),1, "Unexpected number of overweight people")
        lLogger.info("Successfully tested overweight case 1")

    # Add one more overweight entry to the default object and test the increased count
    def testOverweightcase2(self):
        persons = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
                   {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
                   {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
                   {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
                   {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                   {"Gender": "Female", "HeightCm": 167, "WeightKg": 82},
                   {"Gender": "Male", "HeightCm": 167, "WeightKg": 82}]

        personsBMICalculator = [BMICalculator(person.get("Gender"), person.get("HeightCm"), person.get("WeightKg")) for
                                person in persons]
        count_overweight = filter(lambda p: p.bmi_category == "Overweight", personsBMICalculator)
        self.assertEqual(len(list(count_overweight)),2, "Unexpected number of overweight people")
        lLogger.info("Successfully tested overweight case 2")


    # Check if JSON object is empty
    def testOverweightcase3(self):
        persons = []
        personsBMICalculator = [BMICalculator(person.get("Gender"), person.get("HeightCm"), person.get("WeightKg")) for
                                person in persons]
        count_overweight = filter(lambda p: p.bmi_category == "Overweight", personsBMICalculator)
        self.assertEqual(len(list(count_overweight)),0, "Unexpected number of overweight people")
        lLogger.info("Successfully tested overweight case 3")

