import os
from enum import Enum


class PagesURLs(Enum):
    BASE = os.getenv("BASE_URL")
    CAREERS = "/careers"
