import unittest
from tests.Employee import *

class EmployeeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Daniel", 50, "Reading Department", 10)

    def test_that_we_can_calculate_emp_salary(self, hourly_rate, numbers_of_hours_worked):
        self.employee.emp_salary =