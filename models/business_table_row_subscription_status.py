from enum import Enum

class BusinessTableRow_subscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Overdue = "Overdue",
    Canceled = "Canceled",

