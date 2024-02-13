import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):
    """
    * Create a new test method called test_apply_extension
    * Inside test_apply_extension, store the current end_date in a variable called old_end_date
    * Call a method named apply_extension that will take a number of days as an argument on the student instance to update the end_date
    * Assert whether the instance's end_date is equal to the old_end_date plus the days argument that was pass in using timedelta
    * Run the tests to confirm the the new method is failing
    * In the Student class, create a new method called apply_extension that has a parameter called days
    * Use the timedelta method from datetime to update the end_date property
    * Run the tests to confirm they are working
    """

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student("John", "Doe")
    
    def tearDown(self):
        print('tearDown')
        pass

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, "John Doe")


    def test_email(self):
        print('test_email')
        student = Student("John", "Doe")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
        """
        The method below is also great! But keep in mind that it will
        only be correct if a student has received 1 extenstion. If 
        they receive a second - it would return false

        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
        """
    
    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request!")

if __name__ == "__main__":
    unittest.main()