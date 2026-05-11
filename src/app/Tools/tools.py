from datetime import datetime
from langchain.tools import tool

@tool
def get_currecnt_time():
    """Returns the currect time as a string"""

    return datetime.now().strftime("%H:%M:%S")