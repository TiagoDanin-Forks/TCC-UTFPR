# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for generate each general chart used in our research.
# Read each method or class docstring to understand how it works. If you have
# questions, mail me.

try:
    import matplotlib.pyplot as plt
    import json
    import os
except ImportError as error:
    raise ImportError(error)
plt.style.use('bmh')


class GeneralChart():

    def __init__(self, dictionary):
        self.about_list = []
        self.dictionary = dictionary
        self.populate_about_list()

    def populate_about_list(self):
        for language in self.dictionary.keys():
            repositories = self.dictionary[language]['items'][0:3]
            for repository in repositories:
                folder = 'Dataset' + '/' + \
                    language + '/' + repository['name']
                if os.path.isfile(folder + '/about.json'):
                    with open(folder + '/about.json', 'r') as about_file:
                        json_about_file = json.load(about_file)
                        self.about_list.append(json_about_file)
                else:
                    print '[Error] About.json file does not exists for: ' + repository['name']
                    print 'You should collect project about file first. Use collector.py!'

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

        for patch in boxplot['boxes']:
            patch.set_facecolor('white')

        plt.title('Dataset')
        plt.xticks([1, 2, 3], ['# Stars', '# Forks',
                               '# Watchers'], fontsize=12)
        plt.ylim(0, 50000)
        plt.savefig('stars_forks_and_watchers.png', bbox_inches='tight')

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
        plt.bar(1, has_issues, color='lightblue',
                edgecolor='black', linewidth=1, width=bar_width)
        plt.bar(2, has_projects, color='lightgreen',
                edgecolor='black', linewidth=1, width=bar_width)
        plt.bar(3, has_wiki, color='coral',
                edgecolor='black', linewidth=1, width=bar_width)
        plt.xticks([1, 2, 3], ('Issues', 'Projects', 'Wiki'))
        plt.ylabel('# Projects using this feature')
        plt.ylim(0, total_of_projects + 1)
        plt.show()

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        projects_file = json.load(file)
    G = GeneralChart(projects_file)
    G.stars_forks_and_watchers()
    G.has_issues_projects_and_wiki()
else:
    print '[Error] Projects.json file does not exists. Use collector.py!'