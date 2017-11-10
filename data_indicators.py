# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com

try:
    import os
    import csv
    import json
    import numpy
    from datetime import timedelta
    from datetime import datetime
    from collections import Counter
except ImportError as error:
    raise ImportError(error)

class Indicators():

    def __init__(self, repository, folder):
        self.folder = folder

    def pulls_per_month(self):
        pull_file = json.load(open(self.folder + '/pull_requests.json', 'r'))
        pull_list = []
        opened_list = []
        merged_list = []
        closed_list = []

        for line in pull_file:
            pull_list.append(datetime.strptime(
                line['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

            if line['closed_at'] is not None:
                if line['merged_at'] is not None:
                    merged_date = line['merged_at']
                    merged_list.append(datetime.strptime(
                        merged_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))
                else:
                    closed_date = line['closed_at']
                    closed_list.append(datetime.strptime(
                        closed_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))
            else:
                opened_date = line['created_at']
                opened_list.append(datetime.strptime(
                    opened_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

        pull_ordered_list = Counter(pull_list)
        pull_ordered_list = [item[1] for item in pull_ordered_list.items()]

        opened_ordered_list = Counter(opened_list)
        opened_ordered_list = [item[1] for item in opened_ordered_list.items()]

        closed_ordered_list = Counter(closed_list)
        closed_ordered_list = [item[1] for item in closed_ordered_list.items()]

        merged_ordered_list = Counter(merged_list)
        merged_ordered_list = [item[1] for item in merged_ordered_list.items()]

        return numpy.mean(pull_ordered_list), numpy.mean(opened_ordered_list), numpy.mean(closed_ordered_list), numpy.mean(merged_ordered_list)

    def commits_per_month(self):
        contribution_file = open(self.folder + '/contributions.txt', 'r')
        contribution_list = []

        for line in contribution_file:
            contribution_date = line.strip()

            if contribution_date:
                contribution_list.append(datetime.strptime(
                    contribution_date, '%Y-%m-%d').date().replace(day=15))

        contribution_ordered_list = Counter(contribution_list)
        contribution_ordered_list = [item[1]
                                     for item in contribution_ordered_list.items()]

        return numpy.mean(contribution_ordered_list)

    def stars_per_month(self):
        stars_file = json.load(open(self.folder + '/stars.json', 'r'))
        star_list = []

        for line in stars_file:
            star_date = line['starred_at']

            if star_date:
                star_list.append(datetime.strptime(
                    star_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

        star_ordered_list = Counter(star_list)
        star_ordered_list = [item[1] for item in star_ordered_list.items()]

        return numpy.mean(star_ordered_list)

    def forks_per_month(self):
        forks_file = json.load(open(self.folder + '/forks.json', 'r'))
        fork_list = []

        for line in forks_file:
            fork_date = line['created_at']

            if fork_date:
                fork_list.append(datetime.strptime(
                    fork_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

        fork_ordered_list = Counter(fork_list)
        fork_ordered_list = [item[1] for item in fork_ordered_list.items()]

        return numpy.mean(fork_ordered_list)

    def languages_counter(self):
        languages_file = json.load(open(self.folder + '/languages.json', 'r'))
        number_of_used_languages = len(languages_file)
        return number_of_used_languages

    def has_readme(self):
        if os.path.isfile(self.folder + '/repository/README.MD') or os.path.isfile(self.folder + '/repository/README.md') or os.path.isfile(self.folder + '/repository/README'):
            return 1
        else:
            return 0

    def has_contributing(self):
        if os.path.isfile(self.folder + '/repository/CONTRIBUTING.MD') or os.path.isfile(self.folder + '/repository/CONTRIBUTING.md') or os.path.isfile(self.folder + '/repository/CONTRIBUTING'):
            return 1
        else:
            return 0

    def has_wiki(self):
        about_file = json.load(open(self.folder + '/about.json', 'r'))

        if about_file['has_wiki']:
            return 1
        else:
            return 0

    def has_project_board(self):
        about_file = json.load(open(self.folder + '/about.json', 'r'))

        if about_file['has_projects']:
            return 1
        else:
            return 0

    def has_issue_tracker(self):
        about_file = json.load(open(self.folder + '/about.json', 'r'))

        if about_file['has_issues']:
            return 1
        else:
            return 0

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
    raise

# In this step, we'll create the indicators data per project.
# The respective file in the repository is data_indicators_output.csv

fieldnames = ['project_name', 'pull_total_mean',
              'pull_opened_mean', 'pull_closed_mean',
              'pull_merged_mean', 'commits_mean',
              'stars_mean', 'forks_mean', 'languages_count',
              'has_readme', 'has_contributing',
              'has_wiki', 'has_project_board', 'has_issue_tracker']

with open('data_indicators_output.csv', 'w') as statistics_file:
    writer = csv.DictWriter(statistics_file, fieldnames=fieldnames)
    writer.writeheader()

for language in dictionary.keys():
    repositories = dictionary[language]['items']

    for repository in repositories:
        dataset_folder = 'Dataset' + '/' + \
            language + '/' + repository['name']

        A = Indicators(repository, dataset_folder)
        pull_total_mean, pull_opened_mean, pull_closed_mean, pull_merged_mean = A.pulls_per_month()
        commits_mean = A.commits_per_month()
        stars_mean = A.stars_per_month()
        forks_mean = A.forks_per_month()
        languages_count = A.languages_counter()
        has_readme = A.has_readme()
        has_contributing = A.has_contributing()
        has_wiki = A.has_wiki()
        has_project_board = A.has_project_board()
        has_issue_tracker = A.has_issue_tracker()

        with open('data_indicators_output.csv', 'a') as statistics_file:
            writer = csv.DictWriter(statistics_file, fieldnames=fieldnames)
            writer.writerow({'project_name': repository['name'],
                             'pull_total_mean': int(numpy.nan_to_num(pull_total_mean)),
                             'pull_opened_mean': int(numpy.nan_to_num(pull_opened_mean)),
                             'pull_closed_mean': int(numpy.nan_to_num(pull_closed_mean)),
                             'pull_merged_mean': int(numpy.nan_to_num(pull_merged_mean)),
                             'commits_mean': int(numpy.nan_to_num(commits_mean)),
                             'stars_mean': int(numpy.nan_to_num(stars_mean)),
                             'forks_mean': int(numpy.nan_to_num(forks_mean)),
                             'languages_count': languages_count,
                             'has_readme': has_readme,
                             'has_contributing': has_contributing,
                             'has_wiki': has_wiki,
                             'has_project_board': has_project_board,
                             'has_issue_tracker': has_issue_tracker})
