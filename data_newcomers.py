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

def newcomers_per_week(folder, latest_created_at):
    newcomer_file = open(folder + '/first_contributions.txt', 'r')
    newcomer_list = []

    for line in newcomer_file:
        entry_date = line.rsplit(',', 1)[1].strip()

        if entry_date:
            entry_date = datetime.strptime(
                entry_date, '%Y-%m-%d').date()

            if entry_date >= latest_created_at:
                newcomer_list.append(entry_date.isocalendar()[1])

    newcomer_ordered_list = Counter(newcomer_list)

    return newcomer_ordered_list


if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
    raise

# In this step, we'll create the newcomers weekly data.
# The respective file in the repository is data_newcomers_output.csv

created_at = []

for language in dictionary.keys():
    repositories = dictionary[language]['items']

    for repository in repositories:
        created_at.append(repository['created_at'])

latest_created_at = max(created_at)
latest_created_at = datetime.strptime(latest_created_at,
                                      '%Y-%m-%dT%H:%M:%SZ').date()

week_series_dictionary = {}

for language in dictionary.keys():
    repositories = dictionary[language]['items']

    for repository in repositories:
        dataset_folder = 'Dataset' + '/' + \
            language + '/' + repository['name']

        newcomers = newcomers_per_week(
            dataset_folder, latest_created_at)

        week_series_dictionary[repository['name']] = newcomers

week_list = []
week_max = None
week_min = None

for week_series in week_series_dictionary.values():
    if week_series:
        if week_min is None:
            week_min = min(week_series)
        else:
            if min(week_series) < week_min:
                week_min = min(week_series)

        if week_max is None:
            week_max = max(week_series)
        else:
            if max(week_series) > week_max:
                week_max = max(week_series)

print 'The first week is ' + str(week_min) + ' and the last week is ' + str(week_max)

fieldnames = [week for week in range(week_min, week_max + 1)]

with open('data_newcomers_output.csv', 'w') as newcomers_file:
    writer = csv.DictWriter(newcomers_file, fieldnames=['project_name'] + fieldnames + ['newcomers_mean'])
    writer.writeheader()

for project in week_series_dictionary:
    csv_data = {}
    mean_list = []

    csv_data['project_name'] = project

    for week in fieldnames:
        if week in week_series_dictionary[project]:
            mean_list.append(week_series_dictionary[project][week])
            csv_data[week] = week_series_dictionary[project][week]
        else:
            csv_data[week] = 0

    if sum(mean_list) > 0:
        csv_data['newcomers_mean'] = sum(mean_list) / float(len(mean_list))
    else:
        csv_data['newcomers_mean'] = 0

    with open('data_newcomers_output.csv', 'a') as newcomers_file:
        writer = csv.DictWriter(newcomers_file, fieldnames=[
                                'project_name'] + fieldnames + ['newcomers_mean'])
        writer.writerow(csv_data)
