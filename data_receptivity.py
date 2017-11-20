# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com

from __future__ import unicode_literals

try:
    import os
    import csv
    import numpy as np
    from datetime import datetime
    import json
except ImportError as error:
    raise ImportError(error)

class Receptivity():

    def classify_receptivity(self):
        projects = {}

        with open('data_newcomers_output.csv', 'r') as newcomers_file:
            reader = csv.DictReader(newcomers_file)
            for row in reader:
                projects[row['project_name']] = float(row['newcomers_mean'])

        receptivity_average = sum(projects.values()) / len(projects.values())
        receptive_projects = {}
        nonreceptive_projects = {}
	print receptivity_average

        for project in projects:
            if projects[project] >= receptivity_average:
                receptive_projects[project] = projects[project]
            else:
                nonreceptive_projects[project] = projects[project]

        return receptive_projects, nonreceptive_projects

    def create_receptivity_files(self, receptive_projects, nonreceptive_projects):
        csv_rows = {}
        reader = csv.reader(open('data_indicators_output.csv', 'r'))
        domain_reader = csv.reader(open('domains.csv', 'r'))
        writer_receptive = csv.writer(open('data_receptive.csv', 'w'))
        writer_nonreceptive = csv.writer(open('data_nonreceptive.csv', 'w'))

        header = reader.next() # Ignore header
        header.append('newcomers_mean')
        header.append('language')
        header.append('age')
        header.append('domain')
        header.append('owner')
        writer_receptive.writerow(header)
        writer_nonreceptive.writerow(header)

        with open('projects.json', 'r') as json_file:
            projects_json = json.load(json_file)

        projects_information = {}
        projects_domain = {}

        domain_reader.next()
        for project in domain_reader:
            # project = domain
            projects_domain[project[0]] = project[1]

        for language in projects_json.keys():
            for project in projects_json[language]['items']:
                project_name = project['name']
                project_language = project['language']
                project_age = 2017 - int(datetime.strptime(project['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)
                if project_name in projects_domain.keys():
                    project_domain = projects_domain[project_name]
                else:
                    project_domain = ''
                project_owner = project['owner']['type']
                projects_information[project_name] = {'language':project_language,'age':project_age,'domain':project_domain,'owner':project_owner}

        for row in reader:
            if row[0] in receptive_projects.keys() and row[0] in projects_information.keys():
                for project in receptive_projects:
                    if row[0] == project:
                        row.append(float(round(receptive_projects[project], 3)))
                        row.append(projects_information[project]['language'])
                        row.append(projects_information[project]['age'])
                        row.append(projects_information[project]['domain'])
                        row.append(projects_information[project]['owner'])
                        writer_receptive.writerow(row)

            elif row[0] in nonreceptive_projects.keys() and row[0] in projects_information.keys():
                for project in nonreceptive_projects:
                    if row[0] == project:
                        row.append(float(round(nonreceptive_projects[project], 3)))
                        row.append(projects_information[project]['language'])
                        row.append(projects_information[project]['age'])
                        row.append(projects_information[project]['domain'])
                        row.append(projects_information[project]['owner'])
                        writer_nonreceptive.writerow(row)
            else:
                print('[Error] Did not find a category for: ' + row['project_name'])

A = Receptivity()
receptive_projects, nonreceptive_projects = A.classify_receptivity()
A.create_receptivity_files(receptive_projects, nonreceptive_projects)
