from enum import Enum

class LeadQualification_employmentType(str, Enum):
    Employed = "Employed",
    PartTime = "PartTime",
    SelfEmployed = "SelfEmployed",
    Contractor = "Contractor",
    Unemployed = "Unemployed",
    Retired = "Retired",
    Student = "Student",
    Military = "Military",
    Homemaker = "Homemaker",
    Disabled = "Disabled",
    Other = "Other",

