# coding: utf-8

"""
    Personnel Data

    API for reading and writing personnel data including data about attendances, absences, documents, etc

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import personio_data_python_sdk
from personio_data_python_sdk.paths.company_employees_employee_id_absences_balance import get
from personio_data_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCompanyEmployeesEmployeeIdAbsencesBalance(ApiTestMixin, unittest.TestCase):
    """
    CompanyEmployeesEmployeeIdAbsencesBalance unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
