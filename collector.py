# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for collect each project data used in our research.
# Read each method or class docstring to understand how it works. If you have
# questions, mail me.

try:
    import Crawler.crawler as GitCrawler
    import Crawler.search as GitSearch
    import Crawler.repository as GitRepository
    import json
    import subprocess
    import os
except ImportError as error:
    raise ImportError(error)


def popular_projects_per_language(languages, crawler):
    search = GitSearch.Search(crawler)
    repositories = {}

    for language in languages:
        print 'Looking for repositories written in ' + language
        repositories[language] = search.repositories(
            keywords='language:' + language.lower(), sort='stars')

    with open('projects.json', 'w') as file:
        json.dump(repositories, file, indent=4)

    return repositories


class RepositoryCollector():

    def __init__(self, repository, folder, crawler):
        self.organization, self.name = repository['full_name'].split('/')
        self.folder = folder
        self.object = GitRepository.Repository(
            self.organization, self.name, crawler)

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def clone(self):
        git_url = repository['git_url']

        if not os.path.exists(self.folder + '/repository'):
            os.makedirs(self.folder + '/repository')

            subprocess.call(['git', 'clone', git_url,
                             self.folder + '/repository'])

    def about(self):
        if not os.path.isfile(self.folder + '/about.json'):
            with open(self.folder + '/about.json', 'w') as about_file:
                json.dump(repository, about_file, indent=4)
        else:
            print '[Warning] A about file already exists. Delete it first.'

    def languages(self):
        if not os.path.isfile(self.folder + '/languages.json'):
            languages = self.object.languages()

            with open(self.folder + '/languages.json', 'w') as languages_file:
                json.dump(languages, languages_file, indent=4)
        else:
            print '[Warning] A languages file already exists. Delete it first.'

    def pull_requests(self):
        if not os.path.isfile(self.folder + '/pull_requests.json'):
            pull_requests = self.object.pull_requests(state='all')

            with open(self.folder + '/pull_requests.json', 'w') as pulls_file:
                json.dump(pull_requests, pulls_file, indent=4)
        else:
            print '[Warning] A pull requests file already exists. Delete it first.'

    def contributions(self):
        if not os.path.isfile(self.folder + '/contributions.txt'):
            if os.path.exists(self.folder + '/repository'):
                subprocess.call(['sh', 'contributions.sh',
                                 self.folder + '/repository'])
            else:
                print '[Error] Repository has not been cloned yet! Use the clone() method to create one.'
        else:
            print '[Warning] A contributions file already exists. Delete it first.'

    def first_contributions(self):
        if not os.path.isfile(self.folder + '/first_contributions.txt'):
            if os.path.exists(self.folder + '/repository'):
                subprocess.call(['sh', 'first_contributions.sh',
                                 self.folder + '/repository'])
            else:
                print '[Error] Repository has not been cloned yet! Use the clone() method to create one.'
        else:
            print '[Warning] A first contributions file already exists. Delete it first.'


crawler = GitCrawler.Crawler(
    '4161a8257efaea420c94', 'd814ec48927a6bd62c55c058cd028a949e5362d4')

languages = ['C', 'CoffeeScript', 'Clojure', 'Erlang',
             'Go', 'Haskell', 'Java', 'JavaScript', 'Objective-C',
             'Perl', 'PHP', 'Python', 'Ruby', 'Scala', 'TypeScript']

if not os.path.isfile('projects.json'):
    popular_projects_per_language(languages, crawler)

with open('projects.json', 'r') as file:
    dictionary = json.load(file)

for language in dictionary.keys():
    # We'll use just the first three projects per language
    repositories = dictionary[language]['items'][0:3]
    for repository in repositories:
        if not 'linux' in repository['name']:
            folder = 'Dataset' + '/' + language + '/' + repository['name']
            R = RepositoryCollector(repository, folder, crawler)
            R.clone()  # Clone the repository
            R.about()  # Create a file with the repository main information
            R.first_contributions()  # Create a file with the first contribution
            # of each contributor in repository
            R.languages()  # Create a file with the languages used in the
            # repository
            R.pull_requests()  # Create a file with all the pull requests created
            # in the repository
            R.contributions()  # Create a file with all commits created in the repository
