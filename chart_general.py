# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for generate charts related to all the projects at once.
# If you have questions, mail me.

try:
    import matplotlib
    from matplotlib.ticker import MultipleLocator
    import matplotlib.pyplot as plt
    import json
    import os
except ImportError as error:
    raise ImportError(error)

# Sets stylesheet
plt.style.use('seaborn-colorblind')
matplotlib.use('Agg')

# Returns the file size in number of lines
def get_file_size(file_name):
    with open(file_name, 'r') as this:
        for i, j in enumerate(this):
            pass
    return i + 1

class GeneralChart():

    # Initial method. Sets values used during the entire process.
    def __init__(self, dictionary):
        self.about_list = []
        self.dictionary = dictionary

        for language in self.dictionary.keys():
            repositories = self.dictionary[language]['items']
            for repository in repositories:
                self.about_list.append(repository)

    # Creates a boxplot chart based on projects stars, forks and watchers
    # Charts are created using matplotlib library and the data we collect before.
    def stars_forks_and_watchers(self):
        stars = []
        forks = []
        watchers = []

        for about in self.about_list:
            stars.append(about['stargazers_count'])
            forks.append(about['forks_count'])
            watchers.append(about['watchers_count'])

        fig = plt.figure()
        boxplot = plt.boxplot([stars, forks, watchers],
                              showfliers=False, patch_artist=True)
        plt.setp(boxplot['boxes'], linewidth=1.5)
        plt.setp(boxplot['whiskers'], linewidth=1.5)
        plt.setp(boxplot['caps'], linewidth=1.5)
        plt.setp(boxplot['medians'], linewidth=1.5)

        for patch in boxplot['medians']:
            patch.set_color('black')

        for patch in boxplot['boxes']:
            patch.set_facecolor('white')

        plt.xticks([1, 2, 3], ['# Star', '# Fork',
                               '# Watcher'], fontsize=12)
        plt.ylim(ymin=0)
        plt.savefig('stars_forks_and_watchers.eps', bbox_inches='tight')

    # Creates a boxplot chart based on projects contributors, pull requests and contributions
    # Charts are created using matplotlib library and the data we collect before.
    def contributors_pulls_and_commits(self):
        contributors = []
        pull_requests = []
        contributions = []

        for language in self.dictionary.keys():
            repositories = self.dictionary[language]['items']
            for repository in repositories:
                folder = 'Dataset' + '/' + language + '/' + repository['name']

                number_of_contributors = get_file_size(folder + '/first_contributions.txt')
                number_of_commits = get_file_size(folder + '/contributions.txt')

                with open(folder + '/pull_requests.json', 'r') as pulls_file:
                    number_of_pulls = len(json.load(pulls_file))

                contributors.append(int(number_of_contributors))
                contributions.append(int(number_of_commits))
                pull_requests.append(int(number_of_pulls))

        fig = plt.figure()
        boxplot = plt.boxplot([contributors, contributions, pull_requests],
                              showfliers=False, patch_artist=True)
        plt.setp(boxplot['boxes'], linewidth=1.5)
        plt.setp(boxplot['whiskers'], linewidth=1.5)
        plt.setp(boxplot['caps'], linewidth=1.5)
        plt.setp(boxplot['medians'], linewidth=1.5)

        for patch in boxplot['medians']:
            patch.set_color('black')

        for patch in boxplot['boxes']:
            patch.set_facecolor('white')

        plt.xticks([1, 2, 3], ['# Contributor', '# Contribution',
                               '# Pull request'], fontsize=12)
        plt.ylim(ymin=0)
        plt.savefig('contributors_pulls_and_contributions.eps', bbox_inches='tight')

    # Creates a bar chart based on projects features. These projects may or may not have these features.
    # Charts are created using matplotlib library and the data we collect before.
    def has_issues_projects_and_wiki(self):
        has_issues = 0
        has_projects = 0
        has_wiki = 0
        total_of_projects = len(self.about_list)

        for about in self.about_list:
            if about['has_issues'] is True:
                has_issues = has_issues + 1
            if about['has_projects'] is True:
                has_projects = has_projects + 1
            if about['has_wiki'] is True:
                has_wiki = has_wiki + 1

        fix, ax = plt.subplots()
        bar_width = 0.4
        bar_issues = plt.bar(1, has_issues, color='white',
                             edgecolor='black', linewidth=1, width=bar_width, label='Has the feature')
        plt.bar(1, total_of_projects - has_issues, color='silver',
                edgecolor='black', linewidth=1, width=bar_width, label='Does not have the feature', bottom=has_issues, hatch='//')
        bar_projects = plt.bar(2, has_projects, color='white',
                               edgecolor='black', linewidth=1, width=bar_width)
        plt.bar(2, total_of_projects - has_projects, color='silver',
                edgecolor='black', linewidth=1, width=bar_width, bottom=has_projects, hatch='//')
        bar_wiki = plt.bar(3, has_wiki, color='white',
                           edgecolor='black', linewidth=1, width=bar_width)
        plt.bar(3, total_of_projects - has_wiki, color='silver',
                edgecolor='black', linewidth=1, width=bar_width, bottom=has_wiki, hatch='//')

        plt.xticks([1, 2, 3], ('Issue Tracker', 'Project Board', 'Wiki'))
        plt.ylabel('# Project')
        plt.ylim(ymin=0)
        plt.legend()
        plt.savefig('has_features.eps', bbox_inches='tight')

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        projects_file = json.load(file)

    G = GeneralChart(projects_file)
    G.stars_forks_and_watchers()
    G.contributors_pulls_and_commits()
    G.has_issues_projects_and_wiki()
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
