class Job:
def __init__(self, name, category, rate, date, hours):
    self.name = name
    self.category = category
    self.rate = rate
    self.date = date
    self.hours = hours
pass
def get_name(self):
    return self.name
pass
def get_category(self):
    return self.category
pass
def get_rate(self):
    return self.rate
pass
def get_date(self):
    return self.date
pass
def get_hours(self):
    return self.hours
pass
def __eq__(self, other):
    if self.name == other.name:
        return True
    else:
        return False
pass
def __hash__(self):
    return hash(self.name)
pass
def __str__(self):
    print(f"{self.name} {self.category} {self.rate} {self.date} {self.hours}")
pass
def __repr__(self):
    print(self.name, self.category, self.rate, self.date, self.hours)
pass
