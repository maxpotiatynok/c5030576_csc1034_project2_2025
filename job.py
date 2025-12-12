class Job:
    # Constructor
    def __init__(self, name, category, rate, date, hours):
        if isinstance(name, str): # Check if name is a string
            self.__name = name
        else:
            raise TypeError("Name must be a string")
        if isinstance(category, str): # Check if category is a string
            self.__category = category
        else:
            raise TypeError("Category must be a string")
        if isinstance(rate, float): # Check if rate is a float
            if rate > 0: # Should be positive
                self.__rate = rate
            else:
                raise TypeError("Rate must be positive")
        else:
            raise TypeError("Rate must be a float")
        if isinstance(date, str): # Check if date is a string
            self.__date = date
        else:
            raise TypeError("Date must be a string")
        if isinstance(hours, int): # Check if hours is an integer
            if 0 < hours <= 6: # Should be positive and no more than 6
                self.__hours = hours
            else:
                raise Exception('hours must be between 0 and 6') # Throw an exception if the number of hours is more than 6
        else :
            raise TypeError("Hours must be an integer")

    # Get name
    def get_name(self):
        return self.__name

    # Get category
    def get_category(self):
        return self.__category

    # Get rate
    def get_rate(self):
        return self.__rate

    # Get date
    def get_date(self):
        return self.__date

    # Get hours
    def get_hours(self):
        return self.__hours

    # Method to check if two objects of Job class are equal
    # Returns a boolean value(either True or False)
    def __eq__(self, other):
        if self.__name == other.name:
            return True
        else:
            return False

    # Returns an object's has value(integer)
    def __hash__(self):
        return hash(self.__name)

    # String representation
    def __str__(self):
        return f'Job: {self.__name}, {self.__category}, {self.__rate}, {self.__date}, {self.__hours}'

    # Formal string representation for developers
    def __repr__(self):
        return f'Job({self.__name}, {self.__category}, {self.__rate}, {self.__date}, {self.__hours})'

