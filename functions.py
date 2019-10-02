import peewee

from models import *

import random
import collections

navigation_menu = [
    {
        "link": "/dashboard",
        "icon": "fas fa-fw fa-tachometer-alt",
        "title": "Dashboard"
    },
    {
        "link": "/issues",
        "icon": "fas fa-fw fa-exclamation-triangle",
        "title": "Issues"
    },
    {
        "link": "/reports",
        "icon": "fas fa-fw fa-chart-area",
        "title": "Reports"
    },
    {
        "link": "/targets",
        "icon": "fas fa-fw fa-bullseye",
        "title": "Targets"
    },
    {
        "link": "/network",
        "icon": "fas fa-fw fa-laptop",
        "title": "Network"
    }
]

page_titles = {
    "/dashboard": "Dashboard",
    "/reports": "Reports",
    "/targets": "Targets",
    "/issues": "Issues",
    "/network": "Network"
}

types = [
        {
            'type': 'danger',
            'title': 'Critical',
            'color': '#e74a3b',
            'order': 4
        },
        {
            'type': 'primary',
            'title': 'Low',
            'color': '#4e73df',
            'order': 2
        },
        {
            'type': 'warning',
            'title': 'High',
            'color': '#f6c23e',
            'order': 3
        },
        {
            'type': 'info',
            'title': 'Medium',
            'color': '#36b9cc',
            'order': 1
        }
    ]

issues = [
    {
        'type': 'info',
        'title': 'Reflected Cross-Site Scripting (XSS)',
        'issue_id': 123
    },
    {
        'type': 'primary',
        'title': 'Web Server In Use Contains Known Vulnerabilities (Apache)',
        'issue_id': 234
    },
    {
        'type': 'danger',
        'title': 'Web Server Directory Listings Expose List of Files',
        'issue_id': 345
    }
]
#
# def create_database():
#     try:
#         pg_db.drop_tables([
#             Issue_category
#         ]
#         )
#         print('Dropped.')
#     except peewee.InternalError as err:
#         print(err)
#     try:
#         pg_db.create_tables([
#             Issue_category
#         ])
#         print('Created.')
#     except peewee.InternalError as err:
#         print(err)


def test_network_data():
    res = {}
    protocols = ['tcp','ftp','sftp','ip','ssl','ssh','http','https']
    services = ['Ubuntu 13', 'Windows XP', 'MacOS', 'Android']
    result_arr = []
    for i in range(1,11):
        tmp_arr = {}
        tmp_arr['ip_address'] = str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255))
        tmp_arr['hostnames'] = ''.join(random.choice(['hello', 'apple', 'something', 'yeah', 'nope', 'lalala']) for _ in range(5))
        tmp_arr['port'] = random.randint(1,9999)
        tmp_arr['protocol'] = random.choice(protocols)
        tmp_arr['service'] = random.choice(protocols)
        tmp_arr['service_info'] = random.choice(services)
        result_arr.append(tmp_arr)
    res['recordsTotal'] = len(result_arr)
    res['recordsFiltered'] = len(result_arr)
    res['data'] = result_arr
    print(res)
    return res


def test_targets_data():
    hostnames = ['test','main','index','preview','custom']
    zones = ['ru','com','net','org']
    result_arr = []
    for i in range(1,6):
        tmp_arr = {}
        tmp_arr['target_id'] = random.randint(1,9999)
        tmp_arr['hostname'] = random.choice(hostnames) + '.' + random.choice(hostnames) + '.' + random.choice(zones)
        tmp_arr['low_issues'] = random.randint(0,9)
        tmp_arr['medium_issues'] = random.randint(0,9)
        tmp_arr['high_issues'] = random.randint(0,9)
        tmp_arr['critical_issues'] = random.randint(0,9)
        result_arr.append(tmp_arr)
    return result_arr

def test_report_data():
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    result_arr = {
        'months': [],
        'critical_data': [],
        'high_data': [],
        'medium_data': [],
        'low_data': []
    }
    columns = range(1,random.randint(1,20))
    for i in columns:
        result_arr['months'].append(str(random.randint(1,30)) + ' ' + random.choice(months))
        result_arr['critical_data'].append(random.randint(1,10))
        result_arr['high_data'].append(random.randint(1,10))
        result_arr['medium_data'].append(random.randint(1,10))
        result_arr['low_data'].append(random.randint(1,10))
    return result_arr

def test_dashboard_first():
    return random.choice(types)

def test_issues_list(filter=None):
    result_arr = []
    tmp_arr = {}
    hostnames = ['test', 'main', 'index', 'preview', 'custom']
    for i in range(1,10):
        tmp_arr = {}
        tmp_type = random.choice(types)
        tmp_arr['id'] = i
        tmp_arr['type'] = tmp_type['title']
        tmp_arr['bg'] = tmp_type['type']
        tmp_arr['order'] = tmp_type['order']
        tmp_arr['issue_title'] = ''.join(random.choice(['hello', 'apple', 'something', 'yeah', 'nope', 'lalala']) for _ in range(5))
        tmp_arr['description'] = 'Description of Issue'
        tmp_arr['links'] = [
            'https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)',
            'https://en.wikipedia.org/wiki/Cross-site_scripting'
        ]
        tmp_arr['recomendation'] = 'Some test'
        tmp_arr['occurences'] = []
        for p in range (1, 10):
            tmp_arr['occurences'].append(
                {
                    'target': tmp_arr['issue_title'],
                    'port': random.randint(1,9999),
                    'version': str(random.randint(0,5)) + '.' + str(random.randint(1,10)) + '.' + str(random.randint(1,50)),
                    'path': '/' + random.choice(hostnames),
                    'affcted_parameter': ''.join(random.choice(['a', 'b', 'c', 'd', 'e', 'f']) for _ in range(1)),
                    'age': str(random.randint(1,10)) + ' days',
                    'scanner_output': ' View ',
                    'other': '<div class="pull-right dropdown text-default"><button data-toggle="dropdown" type="button" '
                             'aria-expanded="false" aria-haspopup="true" class="btn btn-white dropdown-toggle"><i '
                             'class="fas fa-ellipsis-h"></i></button> <ul aria-labelledby="dropdown-' + str(random.randint(1,99999)) + '" '
                             'class="dropdown-menu"><li class="dropdown-header">Snooze by ...</li> <li><a href="#" '
                             'title="" class="snooze-issue">accepting risk</a></li> <li><a href="#" title="" '
                             'class="snooze-issue">marking as false positive</a></li> <li><a href="#" title="" '
                             'class="snooze-issue">adding mitigating controls</a></li></ul></div> '
                }
            )
        if filter is not None:
            if (tmp_arr['type']).lower() == filter:
                result_arr.append(tmp_arr)
        else:
            result_arr.append(tmp_arr)


    return sorted(result_arr, key=lambda k: k['order'], reverse=True)

def get_cnt_group_issues(arr):
    types_issues = ['Low', 'Medium', 'High','Critical']
    result = {
        "Low" : 0,
        "Medium": 0,
        "High": 0,
        "Critical": 0
    }
    cnt = 0
    for t in types_issues:
        for i in arr:
            if i['type'] == t:
                result[t] += 1
    return result


def get_top_issues():
    return issues
