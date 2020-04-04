from datetime import datetime

class DateParser:
    def __init__(self, date_str):
        self.date_str = date_str

    def parse(self):
        '''
        This method must return a datetime python object parsed
        from the input string.

        example usage of this class and method.

        parser = DateParser("2020-04-11")
        parsed_date = parser.parse()

        The following check is equivalent
        parsed_date == datetime.datetime(2020, 04, 11, 0 0)
        '''
        pass
        
