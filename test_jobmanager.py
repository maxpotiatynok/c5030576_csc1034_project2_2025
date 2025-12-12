import pytest

import job
from job_manager import JobManager
from job import Job
class TestJobManager:
    """Tests the JobManager class"""
    # Normal case
    def test_init_full(self):
        """Tests the constructor by using a list as a parameter"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert isinstance(job_manager, JobManager)

    # Exceptional case
    def test_init_empty(self):
        """Tests the constructor by not using a list as a parameter"""
        job_manager = JobManager()
        assert isinstance(job_manager, JobManager)

    # Normal case
    def test_get_job(self):
        """Tests the get_job function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert job_manager.get_jobs() == [job1, job2]

    # Normal case
    def test_str(self):
        """Tests the __str__ function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert job_manager.__str__() == "Job manager: ".join(str(j) for j in job_list) # Compares .__str__() method
        # with the list converted to the string

    # Normal case
    def test_repr(self):
        """Tests the __repr__ function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        list_str = "".join(str(j) for j in job_list)
        assert job_manager.__repr__() == f"Job manager({list_str})"

    # Normal case
    def test_add_job_valid(self):
        """Tests the add_job function"""
        job_manager = JobManager()
        job = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_manager.add_job(job)
        assert job in job_manager.get_jobs()

    # Exceptional case
    def test_add_job_invalid(self):
        """Tests the add_job function raises an error if an invalid job is provided"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_list = [j1]
        job_manager = JobManager(job_list)
        with pytest.raises(Exception):
            job_manager.add_job(j2)

    # Normal case
    def test_remove_job_valid(self):
        """Tests the remove_job function"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        jobs_list = [j1]
        job_manager = JobManager(jobs_list)
        job = job_manager.remove_job(j1)
        assert job not in job_manager.get_jobs()

    # Exceptional case
    def test_remove_job_invalid(self):
        """Tests the remove_job function raises an error if an invalid job is provided"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_manager = JobManager()
        with pytest.raises(Exception):
            job_manager.remove_job(j1)

    # Normal case
    def test_edit_job(self):
        """Tests the edit_job function"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        job_manager.edit_job(j1, j2)
        assert j2 in job_manager.get_jobs() and j1 not in job_manager.get_jobs()
        """no need to test exceptional cases as they are covered under test_remove_job_invalid and test_add_job_invalid methods"""

    # Normal Case
    def test_search_by_category_valid(self):
        """Tests the search_by_category function"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_category("Human Resources") == [j1]
    # Exceptional case
    def test_search_by_category_un(self):
        """Tests the search_by_category function where no job with such category exists"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_category("Technical") == []
    # Normal Case
    def test_search_by_rate_valid(self):
        """Tests the search_by_rate function"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_rate(14.10) == [j1]

    # Exceptional Case
    def test_search_by_rate_un(self):
        """Tests the search_by_rate function where no job with such rate exists"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_category(13.45) == []

    # Normal Case
    def test_search_by_name_and_date(self):
        """Tests the search_by_name_and_date function"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_name_and_date("John Brown", "21/10/2026") == [j1]

    @pytest.mark.parametrize("nd", [
        dict(name = "Vladimir Kuznetsov", date = "21/10/2026"),
        dict(name = "John Brown", date = "24/10/2026"),
    ])
    # Exceptional Case
    def test_search_by_name_and_date_empty(self,nd):
        """Tests the search_by_name_and_date function where there are no matching jobs"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_list = [j1]
        job_manager = JobManager(job_list)
        assert job_manager.search_by_name_and_date(**nd) == []

    # Normal Case
    def test_total_cost_valid(self):
        """Tests the total_cost function"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("John Brown", "Technical", 13.45, "21/10/2026", 3)
        job_list = [j1, j2]
        job_manager = JobManager(job_list)
        workers = ["John Brown"]
        assert job_manager.get_total_cost_per_name(workers) == {"John Brown": (13.45*4) + (13.45*3)}

    # Exceptional Case
    def test_total_cost_un(self):
        """Tests the total_cost function where no job with such name exists"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("John Brown", "Technical", 13.45, "21/10/2026", 3)
        job_list = [j1, j2]
        job_manager = JobManager(job_list)
        workers = ["Eugene O'Connor"]
        assert job_manager.get_total_cost_per_name(workers) == {"Eugene O'Connor": 0}

    def test_category_count_per_name_valid(self):
        """Tests the category_count_per_name function"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        j2 = Job("Vladimir Kuznetsov", "Technical", 14.10, "24/10/2026", 5)
        j3 = Job("John Brown", "Technical", 13.45, "21/10/2026", 3)
        job_list = [j1, j2, j3]
        job_manager = JobManager(job_list)
        assert job_manager.get_category_count_per_name() == {"Vladimir Kuznetsov": {"Human Resources": 1, "Technical":2}, "John Brown": {"Technical": 2}}


