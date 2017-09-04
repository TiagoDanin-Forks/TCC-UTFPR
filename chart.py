# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for generate each chart used in our research.
# Read each method or class docstring to understand how it works. If you have
# questions, mail me.

try:
    from datetime import datetime
    from collections import Counter
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator
    import matplotlib.dates as mdates
    import numpy
    import json
    import os
except ImportError as error:
    raise ImportError(error)


class RepositoryChart():

    def __init__(self, folder):
        self.folder = folder

        if os.path.isfile(self.folder + '/about.json'):
            with open(self.folder + '/about.json', 'r') as about_file:
                self.repository = json.load(about_file)
        else:
            print '[Error] About file doesn\'t exists. Please, use collector.py to create one.'
            raise

    def newcomers(self):
        if os.path.isfile(self.folder + '/first_contributions.txt'):
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            newcomer_list = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    newcomer_list.append(datetime.strptime(
                        entry_date, '%Y-%m-%d').date().replace(day=15))

            newcomer_ordered_list = Counter(newcomer_list)
            newcomer_ordered_list = sorted(newcomer_ordered_list.items())
            x_axis = [newcomer_tuple[0]
                      for newcomer_tuple in newcomer_ordered_list]
            y_axis = [newcomer_tuple[1]
                      for newcomer_tuple in newcomer_ordered_list]

            fig, ax = plt.subplots()
            plt.title(self.repository['name'])
            plt.xlabel(u'Years')
            plt.ylabel(u'# Newcomers')
            ax.plot(x_axis, y_axis,
                    '-', linewidth=2)
            ax.set_ylim(ymin=0)
            plt.xticks([datetime(year, 1, 1)  # X axis values
                        for year in range(2004, 2019, 2)])
            plt.yticks([number for number in range(0, 141)])  # Y axis values
            ax.xaxis.set_minor_locator(mdates.YearLocator())  # X axis range
            ax.yaxis.set_major_locator(MultipleLocator(20))  # Y axis range
            ax.yaxis.set_minor_locator(MultipleLocator(5))  # Y axis range
            plt.savefig(self.folder + '/newcomers.eps', bbox_inches='tight')

        else:
            print '[Error] Newcomers file doesn\'t exists. Please, use collector.py to create one.'

    def newcomers_and_contributions(self):
        if os.path.isfile(self.folder + '/contributions.txt') and os.path.isfile(self.folder + '/first_contributions.txt'):
            contribution_file = open(self.folder + '/contributions.txt', 'r')
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            contribution_list = []
            newcomer_list = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    newcomer_list.append(datetime.strptime(
                        entry_date, '%Y-%m-%d').date().replace(day=15))

            for line in contribution_file:
                contribution_date = line.strip()

                if contribution_date:
                    contribution_list.append(datetime.strptime(
                        contribution_date, '%Y-%m-%d').date().replace(day=15))

            contribution_ordered_list = Counter(contribution_list)
            contribution_ordered_list = sorted(
                contribution_ordered_list.items())

            newcomer_ordered_list = Counter(newcomer_list)
            newcomer_ordered_list = sorted(newcomer_ordered_list.items())

            contribution_x_axis = [contribution_tuple[0]
                                   for contribution_tuple in contribution_ordered_list]
            contribution_y_axis = [contribution_tuple[1]
                                   for contribution_tuple in contribution_ordered_list]

            newcomer_x_axis = [newcomer_tuple[0]
                               for newcomer_tuple in newcomer_ordered_list]
            newcomer_y_axis = [newcomer_tuple[1]
                               for newcomer_tuple in newcomer_ordered_list]

            fig, ax = plt.subplots()
            ax_second = ax.twinx()

            ax.set_xlabel(u'Years')
            ax.set_ylabel(u'# Newcomers')
            ax.set_ylim(ymin=0)
            ax.set_ylim(0, 141)
            ax.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax.yaxis.set_major_locator(MultipleLocator(20))
            ax.yaxis.set_minor_locator(MultipleLocator(5))
            line_newcomer, = ax.plot(newcomer_x_axis, newcomer_y_axis,
                                     '-', linewidth=2, label='Newcomers')

            ax_second.set_xlabel(u'Years')
            ax_second.set_ylabel(u'# Commits')
            ax_second.set_ylim(ymin=0)
            ax_second.set_ylim(0, 1201)
            ax_second.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax_second.yaxis.set_major_locator(MultipleLocator(100))
            ax_second.yaxis.set_minor_locator(MultipleLocator(50))
            line_contribution, = ax_second.plot(contribution_x_axis,
                                                contribution_y_axis, '--', color='crimson', linewidth=2, label='Commits')
            plt.legend((line_newcomer, line_contribution),
                       ('Newcomers', 'Commits'))
            plt.savefig(self.folder + '/contributions.eps',
                        bbox_inches='tight')

        else:
            print '[Error] Newcomers and commits files doesn\'t exists. Please, use collector.py to create them.'

    def newcomers_and_pulls(self):
        if os.path.isfile(self.folder + '/pull_requests.json') and os.path.isfile(self.folder + '/first_contributions.txt'):
            pull_file = json.load(
                open(self.folder + '/pull_requests.json', 'r'))
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            pull_list = []
            newcomer_list = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    newcomer_list.append(datetime.strptime(
                        entry_date, '%Y-%m-%d').date().replace(day=15))

            for pull in pull_file:
                pull_date = pull['created_at']

                if pull_date:
                    pull_list.append(datetime.strptime(
                        pull_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

            pull_ordered_list = Counter(pull_list)
            pull_ordered_list = sorted(pull_ordered_list.items())

            newcomer_ordered_list = Counter(newcomer_list)
            newcomer_ordered_list = sorted(newcomer_ordered_list.items())

            pull_x_axis = [pull_tuple[0]
                           for pull_tuple in pull_ordered_list]
            pull_y_axis = [pull_tuple[1]
                           for pull_tuple in pull_ordered_list]

            newcomer_x_axis = [newcomer_tuple[0]
                               for newcomer_tuple in newcomer_ordered_list]
            newcomer_y_axis = [newcomer_tuple[1]
                               for newcomer_tuple in newcomer_ordered_list]

            fig, ax = plt.subplots()
            ax_second = ax.twinx()

            ax.set_xlabel(u'Years')
            ax.set_ylabel(u'# Newcomers')
            ax.set_ylim(ymin=0)
            ax.set_ylim(0, 141)
            ax.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax.yaxis.set_major_locator(MultipleLocator(20))
            ax.yaxis.set_minor_locator(MultipleLocator(5))
            line_newcomer, = ax.plot(newcomer_x_axis, newcomer_y_axis,
                                     '-', linewidth=2, label='Newcomers')

            ax_second.set_xlabel(u'Years')
            ax_second.set_ylabel(u'# Pull requests')
            ax_second.set_ylim(ymin=0)
            ax_second.set_ylim(0, 1201)
            ax_second.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax_second.yaxis.set_major_locator(MultipleLocator(100))
            ax_second.yaxis.set_minor_locator(MultipleLocator(50))
            line_pull, = ax_second.plot(pull_x_axis,
                                        pull_y_axis, '--', color='green', linewidth=2, label='Pull requests')
            plt.legend((line_newcomer, line_pull),
                       ('Newcomers', 'Pull requests'))
            plt.savefig(self.folder + '/pull_requests.eps',
                        bbox_inches='tight')
            plt.clf()

        else:
            print '[Error] Newcomers and commits files doesn\'t exists. Please, use collector.py to create them.'

languages = ['C', 'C++', 'Clojure', 'Erlang',
             'Go', 'Haskell', 'Java', 'JavaScript', 'Objective-C',
             'Perl', 'PHP', 'Python', 'Ruby', 'Scala', 'TypeScript']

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)

    for language in dictionary.keys():
        # We'll use just the first three projects per language
        repositories = dictionary[language]['items'][0:3]
        for repository in repositories:
            folder = 'Dataset' + '/' + language + '/' + repository['name']
            Chart = RepositoryChart(folder)
            # Chart.newcomers()
            # Chart.newcomers_and_contributions()
            Chart.newcomers_and_pulls()
else:
    print '[Error] You should collect the projects list first. Use collector .py.'
