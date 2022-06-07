"""
Author: Chandan Parihar
Date: 06-June-2022
Description: Provides the functionality for the BMI calculator.
Date                Name                 Description
06-06-2022           CP                  Demo project
"""

import random
from logger import lLogger

class BMICalculator:
    def __init__(self, gender, height, weight):
        #super().__init__()
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = None
        self.bmi_category = None
        self.health_risk = None
        self.__setvalues()


    """
    private method to BMICalculator to set BMI, BMI Category & Health Risk
    this is added just for the demonstration. Ideally this should be part of the database table
    and a view can be created to get these values. This would also be ideal for big data workloads where 
    such small expension to the dataset can be done at the database level and a relatively bigger dataset gets passed to  
    big data system.
    Ultimately we strive to perform computation of big data workloads on big data systems 
    and avoid performing computation of small datasets on big data plateforms as much as we should/can 
    """
    def __setvalues(self):
        #Added just for logging random object
        rnd = random.randint(1,10000000)

        lLogger.info("Begin setting BMI values for object")
        self.bmi = self.weight/(self.height/100)**2
        if self.bmi<=18.4:
            self.bmi_category="Underweight"
            self.health_risk ="Malnutrition risk"
        elif self.bmi>=18.5 and self.bmi<=24.9 :
            self.bmi_category="Normal weight"
            self.health_risk ="Low risk"
        elif self.bmi>=25 and self.bmi<=29.9 :
            self.bmi_category="Overweight"
            self.health_risk ="Enhanced risk"
        elif self.bmi>=30 and self.bmi<=34.9 :
            self.bmi_category="Moderately Obese"
            self.health_risk ="Midium risk"
        elif self.bmi>=35 and self.bmi<=39.9 :
            self.bmi_category="Severely Obese"
            self.health_risk ="High risk"
        elif self.bmi>=40 :
            self.bmi_category="Very severely Obese"
            self.health_risk ="Very high risk"
        lLogger.info("Setting of BMI values is completed for object")
