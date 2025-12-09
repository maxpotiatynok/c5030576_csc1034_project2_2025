class JobManager:

    def __init__(self, jobs=None):
        if jobs is None:
            self.jobs = []
        else:
            self.jobs = jobs

    def get_jobs(self):
        return self.jobs

    def __str__(self):
        return f"Job manager: {self.jobs}"

    def __repr__(self):
        return f"Job manager({self.jobs})"

    def add_job(self, job):
        if job not in self.jobs:
            workers_hours = 0
            for j in self.jobs:
                if j.getname() == job.getname():
                    workers_hours += j.get_hours()
        else:
            Exception('Job already exists')

    def remove_job(self, job):
        if job in self.jobs:
            self.jobs.remove(job)
        else:
            Exception('Job does not exist')

    def edit_job(self, old_job, new_job):
        if old_job in self.jobs:
            self.jobs.remove_job(old_job)
            self.jobs.add_job(new_job)

    def search_by_category(self, category):
        suitable_jobs = []
        for job in self.jobs:
            if job.getcategory() == category:
                suitable_jobs.append(job)
        return suitable_jobs

    def search_by_rate(self, rate):
        pass

    def search_by_name_and_date(self, name, date):
        pass

    def get_total_cost_per_name(self, names):
        pass

    def get_category_count_per_name(self):
        pass

    def load_from_file(self, file_name):
        pass

    def save_to_file(self, file_name):
        pass
