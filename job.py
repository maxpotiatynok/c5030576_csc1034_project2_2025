class Job:
    def __init__(self, name, category, rate, date, hours):
        """Constructor"""
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

    def get_name(self):
        """Get name"""
        return self.__name

    def get_category(self):
        """Get category"""
        return self.__category

    def get_rate(self):
        """Get rate"""
        return self.__rate

    def get_date(self):
        """Get date"""
        return self.__date

    def get_hours(self):
        """Get hours"""
        return self.__hours

    def __eq__(self, other):
        """
            Method to check if two objects of Job class are equal
            Returns a boolean value(either True or False)
        """
        if self.__hash__() == other.__hash__():
            return True
        else:
            return False

    def __hash__(self):
        """Returns an object's has value(integer)"""
        return hash(self.__name)

    def __str__(self):
        """String representation"""
        return f'Job: {self.__name}, {self.__category}, {self.__rate}, {self.__date}, {self.__hours}'

    def __repr__(self):
        """Formal string representation for developers"""
        return f'Job({self.__name}, {self.__category}, {self.__rate}, {self.__date}, {self.__hours})'

