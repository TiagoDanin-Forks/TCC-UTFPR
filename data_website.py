# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# Dataset folder have a large size with a huge amount of files depending of what you collect.
# This code is responsible for move the necessary data of each project to the website folder.
# If you have questions, mail me.

try:
    import os
    import json
except ImportError as error:
    raise ImportError(error)

def move_files_to_folder(source_folder, destination_folder):
    for source_file in os.listdir(source_folder):
        if 'first_contributions' in source_file or 'about' in source_file or '.png' in source_file:
            source = source_folder + '/' + source_file
            destination_file = destination_folder + '/' + source_file
            if os.path.isfile(destination_file):
                os.remove(destination_file)
            print('Creating a copy of ' + source + ' to website dataset...')
            os.system('cp ' + source + ' ' + destination_file)

website_folder = 'Website/dataset-website'
if not os.path.isdir(website_folder):
    os.mkdir(website_folder)

# Main method.
if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)

    # For each repository folder within each language folder, execute:
    for language in dictionary.keys():
        # If language folder does not exist in website folder
        if not os.path.isdir(website_folder + '/' + language):
            os.mkdir(website_folder + '/' + language)

        repositories = dictionary[language]['items']
        for repository in repositories:
            # The folder where the files are located
            dataset_folder = 'Dataset' + '/' + language + '/' + repository['name']
            # The folder where the files will be moved
            website_dataset_folder = website_folder + '/' + language + '/' + repository['name']

            if not os.path.isdir(website_dataset_folder):
                os.mkdir(website_dataset_folder)

            move_files_to_folder(dataset_folder, website_dataset_folder)
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
