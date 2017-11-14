import json
from datetime import datetime

with open('projects.json', 'r') as json_file:
    projects_json = json.load(json_file)

projects_information = {}

for language in projects_json.keys():
    for project in projects_json[language]['items']:
        project_name = project['name']
        project_language = project['language']
        project_age = 2017 - int(datetime.strptime(project['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)
        project_domain = ' - '
        project_owner = project['owner']['type']
