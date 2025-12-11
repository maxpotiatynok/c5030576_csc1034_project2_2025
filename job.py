class Job:
    # Constructor
    def __init__(self, name, category, rate, date, hours):
        self.__name = name
        self.__category = category
        if rate > 0: # Should be positive
            self.__rate = rate
        else:
            Exception('rate must be positive') # Throw an exception if the rate is negative or zero
        self.__date = date
        if 0 < hours <= 6: # Should be positive and no more than 6
            self.__hours = hours
        else:
            Exception('hours must be between 0 and 6') # Throw an exception if the number of hours is more than 6

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

