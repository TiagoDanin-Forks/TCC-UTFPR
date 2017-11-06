# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for collect data of each used in our research.
# If you have questions, mail me.

try:
    import multiprocessing
    from functools import partial
    import Crawler.crawler as GitCrawler
    import Crawler.search as GitSearch
    import Crawler.repository as GitRepository
    import json
    import subprocess
    import os
except ImportError as error:
    raise ImportError(error)

# This class is responsible for collect data of each project.
# To use it, send as parameter a repository main page, a folder to save the data
# and a Crawler.crawler object.
# Example of repository main page: https://api.github.com/repos/atom/atom

class Collector():

    def __init__(self, repository, folder, crawler):
        self.repository = repository
        self.organization, self.name = repository['full_name'].split('/')
        self.folder = folder
        self.object = GitRepository.Repository(
            self.organization, self.name, crawler)

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def clone(self):
        git_url = self.repository['git_url']

        if not os.path.exists(self.folder + '/repository'):
            os.makedirs(self.folder + '/repository')

            subprocess.call(['git', 'clone', git_url,
                             self.folder + '/repository'])
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Repository folder already exists.\033[0m Please, delete it first.')

    def about(self):
        if not os.path.isfile(self.folder + '/about.json'):
            with open(self.folder + '/about.json', 'w') as about_file:
                json.dump(self.repository, about_file, indent=4)
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> About file already exists.\033[0m Please, delete it first.')

    def languages(self):
        if not os.path.isfile(self.folder + '/languages.json'):
            languages = self.object.languages()

            with open(self.folder + '/languages.json', 'w') as languages_file:
                json.dump(languages, languages_file, indent=4)
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Languages file already exists.\033[0m Please, delete it first.')

    def stars(self):
        stars_file_lines = sum(1 for line in open(self.folder + '/stars.json', 'r'))

        if not os.path.isfile(self.folder + '/stars.json') or stars_file_lines < 10:
            stars = self.object.stars()

            with open(self.folder + '/stars.json', 'w') as stars_file:
                json.dump(stars, stars_file, indent=4)
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Stars file already exists.\033[0m Please, delete it first.')

    def forks(self):
        forks_file_lines = sum(1 for line in open(self.folder + '/forks.json', 'r'))

        if not os.path.isfile(self.folder + '/forks.json') or forks_file_lines < 10:
            forks = self.object.forks()

            with open(self.folder + '/forks.json', 'w') as forks_file:
                json.dump(forks, forks_file, indent=4)
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Forks file already exists.\033[0m Please, delete it first.')

    def pull_requests(self):
        if not os.path.isfile(self.folder + '/pull_requests.json'):
            pull_requests = self.object.pull_requests(state='all')

            with open(self.folder + '/pull_requests.json', 'w') as pulls_file:
                json.dump(pull_requests, pulls_file, indent=4)
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Pull requests file already exists.\033[0m Please, delete it first.')

    def contributions(self):
        if not os.path.isfile(self.folder + '/contributions.txt'):
            if os.path.exists(self.folder + '/repository'):
                subprocess.call(['sh', 'Crawler/contributions.sh',
                                 self.folder + '/repository'])
            else:
                print('Error processing ' + self.name + ' project.')
                print(
                    '\033[97m\033[1m-> Repository has not been cloned yet.\033[0m Contributions file failed.')
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Contributions file already exists.\033[0m Please, delete it first.')

    def first_contributions(self):
        if not os.path.isfile(self.folder + '/first_contributions.txt'):
            if os.path.exists(self.folder + '/repository'):
                subprocess.call(['sh', 'Crawler/first_contributions.sh',
                                 self.folder + '/repository'])
            else:
                print('Error processing ' + self.name + ' project.')
                print(
                    '\033[97m\033[1m-> Repository has not been cloned yet.\033[0m Newcomers file failed.')
        else:
            print('Error processing ' + self.name + ' project.')
            print(
                '\033[97m\033[1m-> Newcomers file already exists.\033[0m Please, delete it first.')

# This method collects, from a list of languages, the main projects listed
# in GitHub, sorted by number of stars.

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

# This method executes collection process in parallel, making the collector faster
# If you want to learn more about it, visit: http://sebastianraschka.com/Articles/2014_multiprocessing.html

def repositories_in_parallel(repository, language):
    # Folder where repository data will be saved
    folder = 'Dataset' + '/' + language + '/' + repository['name']
    # Collector object
    R = Collector(repository, folder, crawler)
    R.clone()  # Clone the repository
    R.about()  # Creates a general information file
    # Creates a file with the first contribution of each contributor in the
    # repository
    R.first_contributions()
    R.languages()  # Creates a file with the languages used in the repository
    R.pull_requests()  # Creates a file with all the pull requests submmited to the repository
    R.contributions()  # Creates a file with all the contributions submmited to the repository
    R.stars()  # Creates a file with all stars evaluated in the repository (Include evaluation date)
    R.forks()  # Creates a file with all the copies created from the repository


# Main method. Instantiate one object for each of the projects, and collects the data separately.
# Please, retrieve your own crawler client id and secret in this page:
# https://github.com/settings/applications/new

api_client_id = '4161a8257efaea420c94' # Please, specify your own client id
api_client_secret = 'd814ec48927a6bd62c55c058cd028a949e5362d4' # Please, specify your own client secret
crawler = GitCrawler.Crawler(api_client_id, api_client_secret)
parallel = multiprocessing.Pool(processes=5)

languages = ['C', 'CoffeeScript', 'Clojure', 'Erlang',
             'Go', 'Haskell', 'Java', 'JavaScript', 'Objective-C',
             'Perl', 'PHP', 'Python', 'Ruby', 'Scala', 'TypeScript']

if not os.path.isfile('projects.json'):
    print('Most popular projects per language file does not exist. Generating one...')
    popular_projects_per_language(languages, crawler)

with open('projects.json', 'r') as file:
    dictionary = json.load(file)

for language in dictionary.keys():
    repositories = dictionary[language]['items']
    # Collect projects data one by one is a too slow process.
    # To make it faster, we use multiprocessing, dividing the collection process between
    # multiple processes.
    parallel.map(partial(repositories_in_parallel, language=language), repositories)
