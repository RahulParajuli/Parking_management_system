
import re
import logging
from typing import Tuple
from datetime import datetime
from ParkingManagement.configurations import month_abbreviations

def saturate_date(input_date:str="") -> Tuple[str,datetime]:
    """A utility function to parse the input date into the system flexible format.

    Args:
        input_date (str): _description_. Defaults to "".

    Returns:
        _type_: Tuple containing the string type and datetime type parse result of the respective input date.
    """
    def _map_month_by_num(month:str="") -> int:
        for month_id , month_values in month_abbreviations.items():
            if month.strip() in month_values:
                return month_id
        return 00
    try :    
        year,month, date = 0000, 00 , 00
        if re.search(r"([\d]{4}\-?[\d]{2}\-[\d]{2})", input_date):
            date_as_str = input_date
            date_as_datetime = datetime.strptime(date_as_str, "%Y-%m-%d")
            return date_as_str, date_as_datetime

        # Searching month 
        month_list = [_month[0] for k,_month in month_abbreviations.items()]
        month_list.extend([_abb[1] for k, _abb in month_abbreviations.items()])
        match_month = "|".join(month_list)
        if month_match := re.search(match_month, input_date, flags= re.I):
            month = _map_month_by_num(month_match.group())
            
            # Any thing before the month is the date and post it the year 
            if date_match := re.search(r"[\d]+", input_date[:month_match.span()[0]]):
                date = date_match.group()
                if len(date) == 1 :
                    date = "0" + date 
                    
            if year_match := re.search(r"[\d]+", input_date[month_match.span()[1]:]):
                year = year_match.group()

        date_as_str = "-".join([year,month,date])
        if ( len(month) !=2 or len(date) != 2 ) or (len(year) != 4):
            logging.error("Invalid Date Format : ".format(date_as_str))
            return (date_as_str,"")
        
        datetime_object = datetime.strptime(date_as_str, '%Y-%m-%d')
        return (date_as_str,datetime_object)
    except Exception as e:
        logging.error("Error parsing of Input Date" + e)
        return ("", None)  
    
    
if __name__ == '__main__':
    print(saturate_date("3rd June 2022"))
    print(saturate_date("24th Dec 2024"))
    print(saturate_date("1 March 2022"))


    

