# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com

from __future__ import unicode_literals

try:
    import os
    import csv
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plot
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

        for project in projects:
            if projects[project] >= receptivity_average:
                receptive_projects[project] = projects[project]
            else:
                nonreceptive_projects[project] = projects[project]

        return receptive_projects, nonreceptive_projects

    def create_csv_files(self, receptive_projects, nonreceptive_projects):
        csv_rows = {}
        reader = csv.reader(open('data_indicators_output.csv', 'r'))
        writer_receptive = csv.writer(open('data_receptive.csv', 'w'))
        writer_nonreceptive = csv.writer(open('data_nonreceptive.csv', 'w'))

        header = reader.next()
        header.append('newcomers_mean')
        writer_receptive.writerow(header)
        writer_nonreceptive.writerow(header)

        for row in reader:
            if row[0] in receptive_projects.keys():
                for project in receptive_projects:
                    if row[0] == project:
                        row.append(receptive_projects[project])
                        writer_receptive.writerow(row)

            elif row[0] in nonreceptive_projects.keys():
                for project in nonreceptive_projects:
                    if row[0] == project:
                        row.append(nonreceptive_projects[project])
                        writer_nonreceptive.writerow(row)

            else:
                print('[Error] Didnt find a category for: ' + row['project_name'])

A = Receptivity()
receptive_projects, nonreceptive_projects = A.classify_receptivity()
A.create_csv_files(receptive_projects, nonreceptive_projects)
