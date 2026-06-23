from enum import Enum

class LeadProfile_employmentType(str, Enum):
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

