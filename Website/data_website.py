# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# Dataset folder have a large size with a huge amount of files depending of what you collect.
# This code is responsible for retrieve the necessary data of each project and move it to the website folder.
# If you have questions, mail me.

try:
    import os
    import json
except ImportError as error:
    raise ImportError(error)


def move_files(source_folder, destination_folder):
    for source_file in os.listdir(source_folder):
        destination_file = destination_folder + '/' + source_file

        if os.path.isfile(destination_file):
            os.remove(destination_file)

        if 'summary' in source_file:
            source = source_folder + '/' + source_file
            print('Creating a copy of ' + source + ' to website dataset...')
            os.system('cp ' + source + ' ' + destination_file)


website_folder = 'Website/dataset-website'

if not os.path.isdir(website_folder):
    os.mkdir(website_folder)

if os.path.isfile('projects.json'):

    with open('projects.json', 'r') as file:
        dictionary = json.load(file)

    for language in dictionary.keys():
        repositories = dictionary[language]['items']

        # If language folder does not exists in website
        if not os.path.isdir(website_folder + '/' + language):
            os.mkdir(website_folder + '/' + language)

        for repository in repositories:
            # The folder where the files are located
            dataset_folder = 'Dataset' + '/' + \
                language + '/' + repository['name']
            # The folder where the files will be moved
            website_dataset_folder = website_folder + \
                '/' + language + '/' + repository['name']

            # If project folder does not exists in website
            if not os.path.isdir(website_dataset_folder):
                os.mkdir(website_dataset_folder)

            move_files(dataset_folder, website_dataset_folder)

else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
