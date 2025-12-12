import csv

from pygments.lexers import j

from job import Job

class JobManager:
    """Constructor"""
    def __init__(self, jobs=None):
        """jobs is an optional parameter
         meaning it can be null
        if so, the list of jobs will be empty"""
        if jobs is None:
            self.__jobs = []
        else:
            self.__jobs = jobs

    def get_jobs(self):
        """Get the list of jobs"""
        return self.__jobs

    def __str__(self):
        """String representation"""
        return "Job manager: ".join(str(j) for j in self.__jobs)

    def __repr__(self):
        """Formal string representation for developers"""
        list_str = "".join(str(j) for j in self.__jobs)
        return f"Job manager({list_str})"

    def add_job(self, job):
        """Add a job to the list of jobs"""
        if job not in self.__jobs: # Check if a similar job already exists in the list
            workers_hours = 0
            for j in self.__jobs:
                # Check if such job already exists
                if j.getname() == job.getname():
                    workers_hours += j.get_hours()
        else:
            raise Exception('Job already exists') # Throw an exception if the conditions above aren't met

    def remove_job(self, job):
        """Remove a job from the list of jobs"""
        if job in self.__jobs:
            self.__jobs.remove(job)
        else:
            raise Exception('Job does not exist')

    def edit_job(self, old_job, new_job):
        """Edit a job in the list of jobs"""
        if old_job in self.__jobs:
            self.__jobs.remove_job(old_job)
            self.__jobs.add_job(new_job)

    def search_by_category(self, category):
        """Search for jobs with the given category"""
        suitable_jobs = []
        for job in self.__jobs:
            if job.getcategory() == category:
                suitable_jobs.append(job)
        return suitable_jobs # Return all matching jobs


    def search_by_rate(self, rate):
        """Search for jobs with the given rate"""
        suitable_jobs = []
        for job in self.__jobs:
            if job.getrate() == rate:
                suitable_jobs.append(job)
        return suitable_jobs

    def search_by_name_and_date(self, name, date):
        """Search for jobs with the given name and date"""
        suitable_jobs = []
        for job in self.__jobs:
            if job.getname() == name and job.getdate() == date: # Search jobs that exactly match name and date requirements
                suitable_jobs.append(job)
        return suitable_jobs

    def get_total_cost_per_name(self, names):
        """Return a dictionary that maps each name to the total cost of all jobs under this name"""
        name_cost_dict = {}
        for job in self.__jobs:
            if job.getname() in names:
                if job.getname() not in name_cost_dict:
                    # Check if name is in the dictionary
                    # if not - create a new key-value pair
                    name_cost_dict[job.getname()] = job.get_rate() * job.get_hours()
                else:
                    # if the pair exists, add job cost to the total cost
                    name_cost_dict[job.getname()] += job.get_rate() * job.get_hours()
        return name_cost_dict

    def get_category_count_per_name(self):
        """Return a dictionary that maps name to dictionary that maps each category to the number of jobs of that category"""
        cat_c_n_dict = {}
        for job in self.__jobs:
            if job.name not in cat_c_n_dict:
                cat = 0
                cat_j_dict = {}
                for category in job.categories:
                    if job.category == category:
                        # Count the amount of jobs in the same category for the same name
                        cat = cat + 1
                cat_j_dict[job.category] = cat
                cat_c_n_dict[job.category] = cat_j_dict[job.category]
        return cat_c_n_dict

    def load_from_file(self, file_name):
        """Reads a file and adds jobs from the file to the jobs list"""
        with open(file_name, "r", newline=' ') as csv_file: # Read each row from a file
            reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONE) # Separate columns with comma and without quotation marks
            next(reader) # Skip the first row
            for row in reader:
                if row != [] and len(row) == 5: # The row should not be empty and have less than 5 columns
                    self.add_job(Job(row[0], row[1], row[2], row[3], row[4])) # create a job object with parameters from the file
                else:
                    raise Exception('Invalid row')

    def save_to_file(self, file_name):
        """Write jobs from the jobs list to a file"""
        list_count = 0 # Count each job object in the jobs list
        with open(file_name, "w", newline=' ') as csv_file: # Write each row into a file
            writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in writer:
                if not row: # Write only in empty rows
                    writer.writerow(self.__jobs[list_count]) # Add a job to a file
                    list_count += 1 # Increment the jobs list counter