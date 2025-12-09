class Job:
    def __init__(self, name, category, rate, date, hours):
        self.name = name
        self.category = category
        if rate > 0:
            self.rate = rate
        else:
            Exception('rate must be positive')
        self.date = date
        if 0 < hours <= 6:
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

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f'Job: {self.name}, {self.category}, {self.rate}, {self.date}, {self.hours}'

    def __repr__(self):
        return f'Job({self.name}, {self.category}, {self.rate}, {self.date}, {self.hours})'

