from enum import Enum

class FeedbackAdminUpdateRequest_type(str, Enum):
    Bug = "bug",
    Confusing = "confusing",
    Feature_request = "feature_request",
    Missing_capability = "missing_capability",
    Other = "other",

