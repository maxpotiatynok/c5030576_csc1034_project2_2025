import pytest
from job_manager import JobManager
from job import Job
class TestJobManager:
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
        assert job_manager.get_jobs() ==[job1, job2]