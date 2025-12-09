class Job:
    def __init__(self, name, category, rate, date, hours):
        self.name = name
        self.category = category
        if rate > 0: # Should be positive
            self.rate = rate
        else:
            Exception('rate must be positive')
        self.date = date
        if 0 < hours <= 6: # Should be positive and no more than 6
            self.hours = hours
        else:
            Exception('hours must be between 0 and 6')

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_rate(self):
        return self.rate

    def get_date(self):
        return self.date

    def get_hours(self):
        return self.hours

    # Method to check if two objects of Job class are equal
    # Returns a boolean value(either True or False)
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    # Returns an object's has value(integer)
    def __hash__(self):
        return hash(self.name)

    # String representation
    def __str__(self):
        return f'Job: {self.name}, {self.category}, {self.rate}, {self.date}, {self.hours}'

    # Formal string representation for developers
    def __repr__(self):
        return f'Job({self.name}, {self.category}, {self.rate}, {self.date}, {self.hours})'

