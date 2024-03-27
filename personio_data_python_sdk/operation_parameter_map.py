operation_parameter_map = {
    '/company/time-offs-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'time_off_type_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'half_day_start'
            },
            {
                'name': 'half_day_end'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'skip_approval'
            },
        ]
    },
    '/company/absence-periods-POST': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'time_off_type_id'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'half_day_start'
            },
            {
                'name': 'half_day_end'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'skip_approval'
            },
        ]
    },
    '/company/time-offs/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/absence-periods/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/time-offs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/time-offs-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'updated_from'
            },
            {
                'name': 'updated_to'
            },
            {
                'name': 'employees[]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/company/absence-periods-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'updated_from'
            },
            {
                'name': 'updated_to'
            },
            {
                'name': 'employees[]'
            },
            {
                'name': 'absence_types[]'
            },
            {
                'name': 'absence_periods[]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/company/time-off-types-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/company/attendances-POST': {
        'parameters': [
            {
                'name': 'attendances'
            },
            {
                'name': 'skip_approval'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/attendances/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'skip_approval'
            },
        ]
    },
    '/company/attendances-GET': {
        'parameters': [
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'updated_from'
            },
            {
                'name': 'updated_to'
            },
            {
                'name': 'includePending'
            },
            {
                'name': 'employees[]'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/company/attendances/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'date'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'break'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'skip_approval'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/custom-reports/columns-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'report_id'
            },
        ]
    },
    '/company/custom-reports/reports/{report_id}-GET': {
        'parameters': [
            {
                'name': 'report_id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/company/custom-reports/reports-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'report_ids'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/company/document-categories-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/documents-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'category_id'
            },
            {
                'name': 'file'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'date'
            },
        ]
    },
    '/company/employees-POST': {
        'parameters': [
            {
                'name': 'employee'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees/{employee_id}/absences/balance-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees/custom-attributes-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'email'
            },
            {
                'name': 'attributes[]'
            },
            {
                'name': 'updated_since'
            },
        ]
    },
    '/company/employees/attributes-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees/{employee_id}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees/{employee_id}/profile-picture/{width}-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'width'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/employees/{employee_id}-PATCH': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'employee'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/attendances/projects-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'active'
            },
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/attendances/projects/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/company/attendances/projects-GET': {
        'parameters': [
            {
                'name': 'X-Personio-Partner-ID'
            },
            {
                'name': 'X-Personio-App-ID'
            },
        ]
    },
    '/company/attendances/projects/{id}-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'active'
            },
        ]
    },
};