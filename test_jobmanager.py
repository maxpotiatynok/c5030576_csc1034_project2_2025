import pytest

import job
from job_manager import JobManager
from job import Job
class TestJobManager:
    """Tests the JobManager class"""
    def test_init_full(self):
        """Tests the constructor by using a list as a parameter"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert isinstance(job_manager, JobManager)

    def test_init_empty(self):
        """Tests the constructor by not using a list as a parameter"""
        job_manager = JobManager()
        assert isinstance(job_manager, JobManager)

    def test_get_job(self):
        """Tests the get_job function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert job_manager.get_jobs() == [job1, job2]

    def test_str(self):
        """Tests the __str__ function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        assert job_manager.__str__() == "Job manager: ".join(str(j) for j in job_list) # Compares .__str__() method
        # with the list converted to the string

    def test_repr(self):
        """Tests the __repr__ function"""
        job1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job2 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        job_list = [job1, job2]
        job_manager = JobManager(job_list)
        list_str = "".join(str(j) for j in job_list)
        assert job_manager.__repr__() == f"Job manager({list_str})"

    def test_add_job_valid(self):
        """Tests the add_job function"""
        job_manager = JobManager()
        job = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_manager.add_job(job)
        assert job in job_manager.get_jobs()

    def test_add_job_invalid(self):
        """Tests the add_job function raises an error if an invalid job is provided"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        j2 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_list = [j1]
        job_manager = JobManager(job_list)
        with pytest.raises(Exception):
            job_manager.add_job(j2)

    def test_remove_job_valid(self):
        """Tests the remove_job function"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        jobs_list = [j1]
        job_manager = JobManager(jobs_list)
        job = job_manager.remove_job(j1)
        assert job not in job_manager.get_jobs()

    def test_remove_job_invalid(self):
        """Tests the remove_job function raises an error if an invalid job is provided"""
        j1 = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        job_manager = JobManager()
        with pytest.raises(Exception):
            job_manager.remove_job(j1)
