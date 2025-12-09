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
        suitable_jobs = []
        for job in self.jobs:
            if job.getrate() == rate:
                suitable_jobs.append(job)
        return suitable_jobs

    def search_by_name_and_date(self, name, date):
        suitable_jobs = []
        for job in self.jobs:
            if job.getname() == name and job.getdate() == date:
                suitable_jobs.append(job)
        return suitable_jobs

    def get_total_cost_per_name(self, names):
        name_cost_dict = {}
        for job in self.jobs:
            if job.getname() in names:
                if job.getname() not in name_cost_dict:
                    name_cost_dict[job.getname()] = job.get_rate() * job.get_hours()
                else:
                    name_cost_dict[job.getname()] += job.get_rate() * job.get_hours()
        return name_cost_dict

    def get_category_count_per_name(self):
        cat_c_n_dict = {}
        for job in self.jobs:
            if job.name not in cat_c_n_dict:
                cat = 0
                cat_j_dict = {}
                for category in job.categories:
                    if job.category == category:
                        cat = cat + 1
                cat_j_dict[job.category] = cat
                cat_c_n_dict[job.category] = cat_j_dict[job.category]
        return cat_c_n_dict

    def load_from_file(self, file_name):
        pass

    def save_to_file(self, file_name):
        pass
