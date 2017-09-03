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
            ax.plot(newcomer_x_axis, newcomer_y_axis,
                    '-', linewidth=2)
            ax.set_ylim(ymin=0)
            plt.yticks([number for number in range(0, 141)])
            plt.xticks([datetime(year, 1, 1)
                        for year in range(2004, 2019, 2)])
            ax.xaxis.set_minor_locator(mdates.YearLocator())
            ax.yaxis.set_major_locator(MultipleLocator(20))
            ax.yaxis.set_minor_locator(MultipleLocator(5))

            ax_second = ax.twinx()
            ax_second.plot(contribution_x_axis,
                           contribution_y_axis, '--', color='crimson', linewidth=2)
            ax_second.set_ylim(ymin=0)
            plt.yticks([number for number in range(0, 501)])
            plt.xticks([datetime(year, 1, 1)
                        for year in range(2004, 2019, 2)])
            ax_second.xaxis.set_minor_locator(mdates.YearLocator())
            ax_second.yaxis.set_major_locator(MultipleLocator(100))
            ax_second.yaxis.set_minor_locator(MultipleLocator(25))

            plt.title(self.repository['name'])
            plt.xlabel(u'Years')
            ax.set_ylabel(u'# Newcomers')
            ax_second.set_ylabel(u'# Commits')

            plt.savefig(self.folder + '/contributions.eps',
                        bbox_inches='tight')

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
            Chart.newcomers()
            # Chart.newcomers_and_contributions()
else:
    print '[Error] You should collect the projects list first. Use collector .py.'
