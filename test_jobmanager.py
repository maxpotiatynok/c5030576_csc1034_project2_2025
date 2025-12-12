import csv

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

    # Normal Case
    def test_category_count_per_name_valid(self):
        """Tests the category_count_per_name function"""
        j1 = Job("Vladimir Kuznetsov", "Human Resources", 14.10, "24/10/2026", 6)
        j2 = Job("Vladimir Kuznetsov", "Technical", 14.10, "24/10/2026", 5)
        j3 = Job("John Brown", "Technical", 13.45, "21/10/2026", 3)
        job_list = [j1, j2, j3]
        job_manager = JobManager(job_list)
        assert job_manager.get_category_count_per_name() == {"Vladimir Kuznetsov": {"Human Resources": 1, "Technical":2}, "John Brown": {"Technical": 2}}

    # Exceptional Case
    def test_category_count_per_name_empty(self):
        """Tests the category_count_per_name function where there are no matching jobs"""
        job_manager = JobManager()
        assert job_manager.get_category_count_per_name() == {}

    # Normal case
    def test_load_from_file_valid(self):
        """Tests the load_from_file function"""
        job_manager = JobManager()
        job_manager.load_from_file("sample_data.csv")
        sample_jobs = [
            Job("Aiden Clarke", "Technical", 14.32, "03/08/2024", 3),
            Job("Maya Bennett", "Administration", 12.84, "12/07/2024", 5),
            Job("Elias Turner", "Research Activities", 17.45, "28/07/2024", 2),
            Job("Sophie Hall", "Marketing", 15.67, "09/08/2024", 4),
            Job("Noah Patel", "Operational", 11.98, "21/07/2024", 6),
            Job("Ruby Dawson", "Customer Service", 13.74, "04/08/2024", 1),
            Job("Leo Marsh", "Senior Invigilation", 19.12, "18/07/2024", 3),
            Job("Chloe Grant", "Technical", 16.53, "06/08/2024", 2),
            Job("Oscar Webb", "Teaching and Learning Activities", 11.44, "01/08/2024", 5),
            Job("Isla Kerr", "Research Activities", 18.27, "25/07/2024", 4),
            Job("Finn Collins", "Administration", 10.95, "29/07/2024", 6),
            Job("Zara Hughes", "Marketing", 17.63, "03/07/2024", 1),
            Job("Arlo Spence", "Operational", 12.14, "11/08/2024", 5),
            Job("Freya Morton", "Technical", 14.89, "30/07/2024", 2),
            Job("Hugo Bishop", "Customer Service", 13.05, "07/08/2024", 6),
            Job("Ivy Lambert", "Research Activities", 18.92, "15/07/2024", 3),
            Job("Jude Harris", "Administration", 10.78, "19/07/2024", 4),
            Job("Luna Reeves", "Senior Invigilation", 16.34, "26/07/2024", 1),
            Job("Caleb Foster", "Operational", 12.67, "05/08/2024", 3),
            Job("Nina Watts", "Teaching and Learning Activities", 15.21, "02/08/2024", 5)
        ]
        assert job_manager.get_jobs() == sample_jobs

    def test_load_from_file_invalid(self):
        """Tests the load_from_file function with invalid input"""
        job_manager = JobManager()
        sample_jobs = [
            Job("Aiden Clarke", "Technical", 14.32, "03/08/2024", 3),
            Job("Maya Bennett", "Administration", 12.84, "12/07/2024", 5),
            Job("Elias Turner", "Research Activities", 17.45, "28/07/2024", 2),
            Job("Sophie Hall", "Marketing", 15.67, "09/08/2024", 4),
            Job("Noah Patel", "Operational", 11.98, "21/07/2024", 6),
            Job("Ruby Dawson", "Customer Service", 13.74, "04/08/2024", 1),
            Job("Leo Marsh", "Senior Invigilation", 19.12, "18/07/2024", 3),
            Job("Chloe Grant", "Technical", 16.53, "06/08/2024", 2),
            Job("Oscar Webb", "Teaching and Learning Activities", 11.44, "01/08/2024", 5),
            Job("Isla Kerr", "Research Activities", 18.27, "25/07/2024", 4),
            Job("Finn Collins", "Administration", 10.95, "29/07/2024", 6),
            Job("Zara Hughes", "Marketing", 17.63, "03/07/2024", 1),
            Job("Arlo Spence", "Operational", 12.14, "11/08/2024", 5),
            Job("Freya Morton", "Technical", 14.89, "30/07/2024", 2),
            Job("Hugo Bishop", "Customer Service", 13.05, "07/08/2024", 6),
            Job("Ivy Lambert", "Research Activities", 18.92, "15/07/2024", 3),
            Job("Jude Harris", "Administration", 10.78, "19/07/2024", 4),
            Job("Luna Reeves", "Senior Invigilation", 16.34, "26/07/2024", 1),
            Job("Caleb Foster", "Operational", 12.67, "05/08/2024", 3),
            Job("Nina Watts", "Teaching and Learning Activities", 15.21, "02/08/2024", 5)
        ]
        with pytest.raises(Exception):
            job_manager.load_from_file("bad_data.csv")

    def test_save_to_file(self):
            """Tests the save_to_file function with valid input"""
            sample_jobs = [
                Job("Aiden Clarke", "Technical", 14.32, "03/08/2024", 3),
                Job("Maya Bennett", "Administration", 12.84, "12/07/2024", 5),
                Job("Elias Turner", "Research Activities", 17.45, "28/07/2024", 2),
                Job("Sophie Hall", "Marketing", 15.67, "09/08/2024", 4),
                Job("Noah Patel", "Operational", 11.98, "21/07/2024", 6),
                Job("Ruby Dawson", "Customer Service", 13.74, "04/08/2024", 1),
                Job("Leo Marsh", "Senior Invigilation", 19.12, "18/07/2024", 3),
                Job("Chloe Grant", "Technical", 16.53, "06/08/2024", 2),
                Job("Oscar Webb", "Teaching and Learning Activities", 11.44, "01/08/2024", 5),
                Job("Isla Kerr", "Research Activities", 18.27, "25/07/2024", 4),
                Job("Finn Collins", "Administration", 10.95, "29/07/2024", 6),
                Job("Zara Hughes", "Marketing", 17.63, "03/07/2024", 1),
                Job("Arlo Spence", "Operational", 12.14, "11/08/2024", 5),
                Job("Freya Morton", "Technical", 14.89, "30/07/2024", 2),
                Job("Hugo Bishop", "Customer Service", 13.05, "07/08/2024", 6),
                Job("Ivy Lambert", "Research Activities", 18.92, "15/07/2024", 3),
                Job("Jude Harris", "Administration", 10.78, "19/07/2024", 4),
                Job("Luna Reeves", "Senior Invigilation", 16.34, "26/07/2024", 1),
                Job("Caleb Foster", "Operational", 12.67, "05/08/2024", 3),
                Job("Nina Watts", "Teaching and Learning Activities", 15.21, "02/08/2024", 5)
                ]
            sample_new_jobs = [
                Job("Liam Foster", "Technical", 14.75, "05/03/2027", 4),
                Job("Emily Hart", "Administration", 12.40, "12/04/2027", 5),
                Job("Jackson Reed", "Marketing", 16.80, "19/02/2027", 3),
                Job("Ava Mitchell", "Customer Service", 11.95, "22/03/2027", 2),
                Job("Lucas Rivera", "Operational", 13.10, "07/05/2027", 6),
                Job("Mila Stone", "Research Activities", 17.55, "14/04/2027", 4),
                Job("Henry Cole", "Teaching and Learning Activities", 15.20, "28/02/2027", 3),
                Job("Ella James", "Technical", 18.35, "10/05/2027", 1),
                Job("Caleb Norris", "Senior Invigilation", 19.40, "03/03/2027", 2),
                Job("Grace Wood", "Administration", 10.90, "17/04/2027", 6),
                Job("Ethan Russell", "Marketing", 13.85, "26/03/2027", 4),
                Job("Aria Wells", "Research Activities", 14.60, "09/05/2027", 5),
                Job("Logan Price", "Operational", 11.70, "02/04/2027", 3),
                Job("Sienna Blake", "Customer Service", 12.95, "21/02/2027", 4),
                Job("Owen Carter", "Technical", 17.25, "11/03/2027", 2),
                Job("Harper Lane", "Teaching and Learning Activities", 14.30, "06/05/2027", 5),
                Job("Wyatt Brooks", "Senior Invigilation", 18.90, "24/04/2027", 3),
                Job("Zoe Harrington", "Research Activities", 16.10, "15/03/2027", 2),
                Job("Leo Hammond", "Operational", 12.60, "30/05/2027", 6),
                Job("Nora Stephenson", "Administration", 11.50, "08/05/2027", 1)
            ]
            """Puts sample data into the file"""
            filler = JobManager(sample_jobs)
            filler.save_to_file("sample_data.csv")

            """loading new data to the file"""
            job_manager = JobManager(sample_new_jobs)
            job_manager.save_to_file("sample_data.csv")

            """downloading new data from the file"""
            file_manager = JobManager()
            file_manager.load_from_file("sample_data.csv")
            """comparing them"""
            assert sample_jobs == file_manager.get_jobs()








