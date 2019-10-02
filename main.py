import sys
from flask import Flask, url_for, request, render_template
from functions import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/dashboard')
def index():
    return render_template('dashboard.html', nav_menu=navigation_menu, page_title=page_titles["/dashboard"], first_card=test_dashboard_first(), issues=get_top_issues())

@app.route('/issues', methods=['GET'])
def issues():
    issues_list = test_issues_list()
    return render_template('issues.html',  nav_menu=navigation_menu, page_title=page_titles["/issues"], issues_list=issues_list, group_issues=get_cnt_group_issues(issues_list))

@app.route('/issues/<filter>', methods=['GET'])
def issues_filter(filter):
    issues_list = test_issues_list(filter)
    return render_template('issues.html',  nav_menu=navigation_menu, page_title=page_titles["/issues"], issues_list=issues_list, group_issues=get_cnt_group_issues(issues_list))

@app.route('/issues/<int:type>', methods=['GET'])
def issues_type(type):
    issues_list = test_issues_list()
    return render_template('issues.html', nav_menu=navigation_menu, page_title=page_titles["/issues"],
                           issues_list=issues_list, group_issues=get_cnt_group_issues(issues_list))


@app.route('/network', methods=['GET'])
def network():
    return render_template('network.html',  nav_menu=navigation_menu, page_title=page_titles["/network"])

@app.route('/reports', methods=['GET'])
def reports():
    return render_template('reports.html',  nav_menu=navigation_menu, page_title=page_titles["/reports"])

@app.route('/targets', methods=['GET'])
def targets():
    return render_template('targets.html',  nav_menu=navigation_menu, page_title=page_titles["/targets"], items=test_targets_data())

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', nav_menu=navigation_menu, page_title="404 - Page not found"), 404


@app.route('/create_database', methods=['GET', 'POST'])
def create_database():
    return create_database()

@app.route('/data_source', methods=['POST'])
def test_dt():
    return test_network_data()

@app.route('/delete_target', methods=['POST'])
def delete_target():
    return request.form['target_id'] # function to delete target

@app.route('/scan_target', methods=['POST'])
def scan_target():
    return request.form['target_id'] # function to scan target

@app.route('/get_report_data', methods=['POST'])
def get_report_data():
    return test_report_data()

if __name__ == '__main__':
    app.run(debug=True)


