import pytest
from job import Job
class TestJob:
    """
        Class to test the Job class using pytest
    """
    def test_job_constructor_valid(self):
        """
            Tests valid inputs for the constructor
            Should pass the test
        """
        job = Job("John Brown", "Technical", 13.45, "21/10/2026", 4)
        assert isinstance(job, Job)

    """
        Parametrises dictionaries with wrong data types to test typeerror 
        Should pass the test
        parameter: dictionary
        error: typeerror 
    """
    @pytest.mark.parametrize("parameter, error", [
        (dict(name = 123, category = "Technical", rate = 13.45, date = "21/10/2026", hours = 4), TypeError),
        (dict(name = "John Brown", category = 1, rate = 13.45, date = "21/10/2026", hours = 4), TypeError),
        (dict(name = "John Brown", category = "Technical", rate = "13.45", date = "21/10/2026", hours = 4), TypeError),
        (dict(name = "John Brown", category = "Technical", rate = 13.45, date = 21/10/2026,hours = 4), TypeError),
        (dict(name= "John Brown", category = "Technical", rate = 13.45, date = "21/10/2026", hours = "4"), TypeError),
    ])

    def test_job_constructor_type_error(self, parameter, error):
        """
            Inserts parameters to the job class and checks if the error is raised
        """
        with pytest.raises(error):
            Job(**parameter) # Extracts parameters from the dictionary

    def test_job_constructor_negative_rate(self):
        """
            Tests if raises exception when rate is negative
            Should pass the test if so
        """
        with pytest.raises(Exception):
           Job("John Brown", "Technical", -4.10, "21/10/2026", 4)

    def test_job_constructor_zero_rate(self):
        """
            Tests if raises exception when rate is zero
            Should pass the test if so
        """
        with pytest.raises(Exception):
            Job("John Brown", "Technical", 0, "21/10/2026", 4)

    @pytest.mark.parametrize("p", [
        dict(name = "John Brown", category = "Technical", rate = 13.45, date = "21/10/2026", hours = 1), # Boundary testing
        dict(name = "John Brown", category = "Technical", rate = 13.45, date = "21/10/2026", hours = 4), # Normal case
        dict(name = "John Brown", category = "Technical", rate = 13.45, date = "21/10/2026", hours = 6), # Boundary case
    ])
    def test_job_constructor_valid_hours(self, p):
        job = Job(**p) # Extracts parameters from dictionary
        assert isinstance(job, Job)

    def test_job_constructor_invalid_hours(self):
        with pytest.raises(Exception):
            Job("John Brown", "Technical", 0, "21/10/2026", 12)

    def test_get_name(self):
        """Tests the get_name function to see if the name matches"""
        job = Job("John Brown", "Technical", 4.10, "21/10/2026", 4)
        assert job.get_name() == "John Brown"

    def test_get_category(self):
        """Tests the get_category function to see if the category matches"""
        job = Job("John Brown", "Technical", 4.10, "21/10/2026", 4)
        assert job.get_category() == "Technical"

    def test_get_rate(self):
        """Tests the get_rate function to see if the rate matches"""
        job = Job("John Brown", "Technical", 4.10, "21/10/2026", 4)
        assert job.get_rate() == 4.10

    def test_get_date(self):
        """Tests the get_date function to see if the date matches"""
        job = Job("John Brown", "Technical", 4.10, "21/10/2026", 4)
        assert job.get_date() == "21/10/2026"

    def test_get_hours(self):
        """Tests the get_hours function to see if the hours matches"""
        job = Job("John Brown", "Technical", 4.10, "21/10/2026", 4)
        assert job.get_hours() == 4
