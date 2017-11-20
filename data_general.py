# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for generate data related to all the projects at once.

try:
    import json
    import os
    import csv
    from datetime import datetime
except ImportError as error:
    raise ImportError(error)

# Returns the file size in number of lines
def get_file_size(file_name):
    with open(file_name, 'r') as this:
        for i, j in enumerate(this):
            pass
    return i + 1

class GeneralData():
    # Initial method. Sets values used during the entire process.
    def __init__(self, dictionary):
        self.about_list = []
        self.dictionary = dictionary

        for language in self.dictionary.keys():
            repositories = self.dictionary[language]['items']
            for repository in repositories:
                self.about_list.append(repository)

    def general(self):
        projects = {}
        for language in self.dictionary.keys():
            repositories = self.dictionary[language]['items']
            for repository in repositories:
                folder = 'Dataset' + '/' + language + '/' + repository['name']

                number_of_contributors = get_file_size(folder + '/first_contributions.txt')
                number_of_commits = get_file_size(folder + '/contributions.txt')

                with open(folder + '/pull_requests.json', 'r') as pulls_file:
                    number_of_pulls = len(json.load(pulls_file))

                projects[repository['name']] = {'Contributors': int(number_of_contributors), 'Contributions': int(number_of_commits), 'Pull-requests': int(number_of_pulls)}

        fieldnames=['Project', 'Age', 'Language', 'Stars', 'Watchers', 'Forks', 'Contributors', 'Contributions', 'Total_pulls', 'Has_issues', 'Has_project', 'Has_wiki']
        general_file = open('data_general.csv', 'w')
        writer = csv.DictWriter(general_file, fieldnames=fieldnames)
        writer.writeheader()

        for project in self.about_list:
            if project['has_issues'] is True:
                has_issues = 1
            else:
                has_issues = 0
            if project['has_projects'] is True:
                has_projects =  1
            else:
                has_projects = 0
            if project['has_wiki'] is True:
                has_wiki = 1
            else:
                has_wiki = 0

            age = 2017 - int(datetime.strptime(project['created_at'], '%Y-%m-%dT%H:%M:%SZ').date().year)
            writer.writerow({'Project': project['name'],
                             'Age': age,
                             'Language': project['language'],
                             'Stars': project['stargazers_count'],
                             'Watchers': project['watchers_count'],
                             'Forks': project['forks_count'],
                             'Has_issues': has_issues,
                             'Has_project': has_projects,
                             'Has_wiki': has_wiki,
                             'Total_pulls': projects[project['name']]['Pull-requests'],
                             'Contributors': projects[project['name']]['Contributors'],
                             'Contributions': projects[project['name']]['Contributions']})

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        projects_file = json.load(file)

    G = GeneralData(projects_file)
    G.general()
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
