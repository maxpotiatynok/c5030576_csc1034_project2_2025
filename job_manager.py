class JobManager:

    # Constructor
    def __init__(self, jobs=None):
        # jobs is an optional parameter
        # meaning it can be null
        # if so, the list of jobs will be empty
        if jobs is None:
            self.__jobs = []
        else:
            self.__jobs = jobs

    # Get the list of jobs
    def get_jobs(self):
        return self.__jobs

    # String representation
    def __str__(self): #
        return f"Job manager: {self.__jobs}"

    # Formal string representation for developers
    def __repr__(self):
        return f"Job manager({self.__jobs})"

    # Add a new job to the list
    def add_job(self, job):
        if job not in self.__jobs: # Check if a similar job already exists in the list
            workers_hours = 0
            for j in self.__jobs:
                # Check if such job already exists
                if j.getname() == job.getname():
                    workers_hours += j.get_hours()
        else:
            Exception('Job already exists') # Throw an exception if the conditions above aren't met

    # Remove a job from the list
    def remove_job(self, job):
        if job in self.__jobs:
            self.__jobs.remove(job)
        else:
            Exception('Job does not exist')

    # Replace old job with the new one
    def edit_job(self, old_job, new_job):
        if old_job in self.__jobs:
            self.__jobs.remove_job(old_job)
            self.__jobs.add_job(new_job)

    # Search jobs by a category
    def search_by_category(self, category):
        suitable_jobs = []
        for job in self.__jobs:
            if job.getcategory() == category:
                suitable_jobs.append(job)
        return suitable_jobs # Returns all matching jobs


    # Search jobs by rate
    def search_by_rate(self, rate):
        suitable_jobs = []
        for job in self.__jobs:
            if job.getrate() == rate:
                suitable_jobs.append(job)
        return suitable_jobs

    # Search jobs by name and date
    def search_by_name_and_date(self, name, date):
        suitable_jobs = []
        for job in self.__jobs:
            if job.getname() == name and job.getdate() == date: # Search jobs that exactly match name and date requirements
                suitable_jobs.append(job)
        return suitable_jobs

    # Return a dictionary that maps each name to the total cost of all jobs under this name
    def get_total_cost_per_name(self, names):
        name_cost_dict = {}
        for job in self.__jobs:
            if job.getname() in names:
                if job.getname() not in name_cost_dict:
                    # Check if name is in the dictionary
                    # if not - create a new key-value pair
                    name_cost_dict[job.getname()] = job.get_rate() * job.get_hours()
                else:
                    #if the pair exists, add job cost to the total cost
                    name_cost_dict[job.getname()] += job.get_rate() * job.get_hours()
        return name_cost_dict

    # Return a dictionary that maps name to dictionary that maps each category to the number of jobs of that category
    def get_category_count_per_name(self):
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

    # Read a file and add jobs from the file to the jobs list
    def load_from_file(self, file_name):
        pass

    # Write jobs from the jobs list to a file
    def save_to_file(self, file_name):
        pass
