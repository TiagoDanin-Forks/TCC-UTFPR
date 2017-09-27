# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# This code is responsible for generate charts related to a single repository.
# Read each method or docstring in RepositoryChart class to understand how it works. If you have
# questions, mail me.

try:
    from datetime import datetime
    from collections import Counter
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import host_subplot
    import mpl_toolkits.axisartist as AA
    from matplotlib.ticker import MultipleLocator, MaxNLocator
    from matplotlib.dates import YearLocator
    import itertools
    import pandas
    import statsmodels.api as sm
    import json
    import os
except ImportError as error:
    raise ImportError(error)

# Sets stylesheet
plt.style.use('seaborn-colorblind')

class RepositoryChart():

    # Initial method. Sets values used during the entire process.
    def __init__(self, folder, project_name):
        self.folder = folder
        self.project_name = project_name
        print('Executing charts for: ' + self.project_name + '.')

    # Chart method. Creates a time series chart comparing pull requests, newcomers and contributions.
    def newcomers_pulls_and_contributions(self):
        if os.path.isfile(self.folder + '/pull_requests.json') and os.path.isfile(self.folder + '/first_contributions.txt') and os.path.isfile(self.folder + '/contributions.txt'):
            # Data processing
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            contribution_file = open(self.folder + '/contributions.txt', 'r')
            pull_file = json.load(
                open(self.folder + '/pull_requests.json', 'r'))

            newcomer_list = []
            pull_list = []
            contribution_list = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    newcomer_list.append(datetime.strptime(
                        entry_date, '%Y-%m-%d').date().replace(day=15))

            for line in pull_file:
                pull_date = line['created_at']

                if pull_date:
                    pull_list.append(datetime.strptime(
                        pull_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

            for line in contribution_file:
                contribution_date = line.strip()

                if contribution_date:
                    contribution_list.append(datetime.strptime(
                        contribution_date, '%Y-%m-%d').date().replace(day=15))

            pull_ordered_list = Counter(pull_list)
            pull_ordered_list = sorted(pull_ordered_list.items())

            newcomer_ordered_list = Counter(newcomer_list)
            newcomer_ordered_list = sorted(newcomer_ordered_list.items())

            contribution_ordered_list = Counter(contribution_list)
            contribution_ordered_list = sorted(
                contribution_ordered_list.items())

            newcomer_x_axis = [newcomer_tuple[0]
                               for newcomer_tuple in newcomer_ordered_list]
            newcomer_y_axis = [newcomer_tuple[1]
                               for newcomer_tuple in newcomer_ordered_list]

            pull_x_axis = [pull_tuple[0]
                           for pull_tuple in pull_ordered_list]
            pull_y_axis = [pull_tuple[1]
                           for pull_tuple in pull_ordered_list]

            contribution_x_axis = [contribution_tuple[0]
                                   for contribution_tuple in contribution_ordered_list]
            contribution_y_axis = [contribution_tuple[1]
                                   for contribution_tuple in contribution_ordered_list]

            # Generating charts
            lower_year = min([min(newcomer_x_axis),min(pull_x_axis),min(contribution_x_axis)]).year

            # Y Left -- Newcomers and Pull requests
            fig, axis_one = plt.subplots()
            line_newcomer, = axis_one.plot(newcomer_x_axis, newcomer_y_axis, linestyle='-', linewidth=1.3, label='Newcomer')
            line_pull, = axis_one.plot(pull_x_axis, pull_y_axis, linestyle='-.', linewidth=1.3, color='crimson', label='Pull request')
            axis_one.set_ylabel('# Newcomer / Pull request')
            axis_one.set_xlabel('Years')
            axis_one.set_ylim(ymin=0)
            axis_one.set_xlim(datetime(lower_year, 1, 1), datetime(2018, 1, 1))
            axis_one.xaxis.set_major_locator(YearLocator())
            axis_one.yaxis.set_major_locator(MaxNLocator(integer=True))

            # Y Right -- Contributions
            axis_two = axis_one.twinx()
            line_contribution, = axis_two.plot(contribution_x_axis, contribution_y_axis, linestyle='--', linewidth=1.3, color='green', label='Contribution')
            axis_two.set_ylabel('# Contribution')
            axis_two.set_xlabel('Years')
            axis_two.set_ylim(ymin=0)
            axis_two.set_xlim(datetime(lower_year, 1, 1), datetime(2018, 1, 1))
            axis_two.xaxis.set_major_locator(YearLocator())
            axis_two.yaxis.set_major_locator(MaxNLocator(integer=True))

            legend = plt.legend((line_newcomer, line_pull, line_contribution),
                       ('Newcomer', 'Pull request', 'Contribution'), loc='upper center', bbox_to_anchor=(0.5, 1.1),  shadow=False, ncol=3)
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(0.8)

            plt.title(self.project_name)
            plt.savefig(self.folder + '/newcomers_contributions_pulls.eps',
                        bbox_inches='tight')
            plt.clf()

        else:
            print('Error processing ' + self.project_name + ' project.')
            print(
                '\033[97m\033[1m-> Newcomer, pull request or contribution file does not exist.\033[0m Please, collect them first.')

    # Chart method. Creates a time series chart comparing stars, newcomers and forks.
    def newcomers_forks_and_stars(self):
        if os.path.isfile(self.folder + '/stars.json') and os.path.isfile(self.folder + '/forks.json') and os.path.isfile(self.folder + '/first_contributions.txt'):
            # Data processing
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            stars_file = json.load(
                open(self.folder + '/stars.json', 'r'))
            forks_file = json.load(
                open(self.folder + '/forks.json', 'r'))

            newcomer_list = []
            star_list = []
            fork_list = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    newcomer_list.append(datetime.strptime(
                        entry_date, '%Y-%m-%d').date().replace(day=15))

            for line in stars_file:
                star_date = line['starred_at']

                if star_date:
                    star_list.append(datetime.strptime(
                        star_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

            for line in forks_file:
                fork_date = line['created_at']

                if fork_date:
                    fork_list.append(datetime.strptime(
                        fork_date, '%Y-%m-%dT%H:%M:%SZ').date().replace(day=15))

            newcomer_ordered_list = Counter(newcomer_list)
            newcomer_ordered_list = sorted(newcomer_ordered_list.items())

            star_ordered_list = Counter(star_list)
            star_ordered_list = sorted(star_ordered_list.items())

            fork_ordered_list = Counter(fork_list)
            fork_ordered_list = sorted(fork_ordered_list.items())

            newcomer_x_axis = [newcomer_tuple[0]
                               for newcomer_tuple in newcomer_ordered_list]
            newcomer_y_axis = [newcomer_tuple[1]
                               for newcomer_tuple in newcomer_ordered_list]

            star_x_axis = [star_tuple[0]
                           for star_tuple in star_ordered_list]
            star_y_axis = [star_tuple[1]
                           for star_tuple in star_ordered_list]

            fork_x_axis = [fork_tuple[0]
                           for fork_tuple in fork_ordered_list]
            fork_y_axis = [fork_tuple[1]
                           for fork_tuple in fork_ordered_list]

            # Generating charts
            lower_year = min([min(newcomer_x_axis),min(fork_x_axis),min(star_x_axis)]).year

            # Y Left -- Newcomers and Forks
            fig, axis_one = plt.subplots()
            line_newcomer, = axis_one.plot(newcomer_x_axis, newcomer_y_axis, linestyle='-', linewidth=1.3, label='Newcomer')
            line_fork, = axis_one.plot(fork_x_axis, fork_y_axis, linestyle='-.', linewidth=1.3, color='crimson', label='Fork')
            axis_one.set_ylabel('# Newcomer / Fork')
            axis_one.set_xlabel('Years')
            axis_one.set_ylim(ymin=0)
            axis_one.set_xlim(datetime(lower_year, 1, 1), datetime(2018, 1, 1))
            axis_one.xaxis.set_major_locator(YearLocator())
            axis_one.yaxis.set_major_locator(MaxNLocator(integer=True))

            # Y Right -- Contributions
            axis_two = axis_one.twinx()
            line_star, = axis_two.plot(star_x_axis, star_y_axis, linestyle='--', linewidth=1.3, color='green', label='Star')
            axis_two.set_ylabel('# Star')
            axis_two.set_xlabel('Years')
            axis_two.set_ylim(ymin=0)
            axis_two.set_xlim(datetime(lower_year, 1, 1), datetime(2018, 1, 1))
            axis_two.xaxis.set_major_locator(YearLocator())
            axis_two.yaxis.set_major_locator(MaxNLocator(integer=True))

            legend = plt.legend((line_newcomer, line_fork, line_star),
                       ('Newcomer', 'Fork', 'Star'), loc='upper center', bbox_to_anchor=(0.5, 1.1),  shadow=False, ncol=3)
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(0.8)

            plt.title(self.project_name)
            plt.savefig(self.folder + '/newcomers_forks_stars.eps',
                        bbox_inches='tight')
            plt.clf()

        else:
            print('Error processing ' + self.project_name + ' project.')
            print(
                '\033[97m\033[1m-> Newcomer, star ou fork file does not exist.\033[0m Please, collect them first.')

    # Chart method. Creates a time series chart comparing pull requests and their status.
    def pulls_opened_closed_and_merged(self):
        if os.path.isfile(self.folder + '/pull_requests.json'):
            # Data processing
            pulls_file = json.load(
                open(self.folder + '/pull_requests.json', 'r'))

            opened_list = []
            closed_list = []
            merged_list = []

            for line in pulls_file:
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

            opened_ordered_list = Counter(opened_list)
            opened_ordered_list = sorted(opened_ordered_list.items())

            closed_ordered_list = Counter(closed_list)
            closed_ordered_list = sorted(closed_ordered_list.items())

            merged_ordered_list = Counter(merged_list)
            merged_ordered_list = sorted(merged_ordered_list.items())

            opened_x_axis = [opened_tuple[0]
                               for opened_tuple in opened_ordered_list]
            opened_y_axis = [opened_tuple[1]
                               for opened_tuple in opened_ordered_list]

            closed_x_axis = [closed_tuple[0]
                           for closed_tuple in closed_ordered_list]
            closed_y_axis = [closed_tuple[1]
                           for closed_tuple in closed_ordered_list]

            merged_x_axis = [merged_tuple[0]
                           for merged_tuple in merged_ordered_list]
            merged_y_axis = [merged_tuple[1]
                           for merged_tuple in merged_ordered_list]

            # Generating charts
            lower_year = min([date.year for date in closed_x_axis])

            # Y -- Opened, closed and merged pull requests
            fig, axis_one = plt.subplots()
            line_opened, = axis_one.plot(opened_x_axis, opened_y_axis, linestyle='-', linewidth=1.3, label='Open')
            line_closed, = axis_one.plot(closed_x_axis, closed_y_axis, linestyle='-.', linewidth=1.3, color='crimson', label='Closed')
            line_merged, = axis_one.plot(merged_x_axis, merged_y_axis, linestyle='-.', linewidth=1.3, color='green', label='Merged')
            axis_one.set_ylabel('# Pull Request Opened / Closed / Merged')
            axis_one.set_xlabel('Years')
            axis_one.set_ylim(ymin=0)
            axis_one.set_xlim(datetime(lower_year, 1, 1), datetime(2018, 1, 1))
            axis_one.xaxis.set_major_locator(YearLocator())
            axis_one.yaxis.set_major_locator(MaxNLocator(integer=True))

            legend = plt.legend((line_opened, line_closed, line_merged),
                       ('Open', 'Closed', 'Merged'), loc='upper center', bbox_to_anchor=(0.5, 1.1),  shadow=False, ncol=3)
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(0.8)

            plt.title(self.project_name)
            plt.savefig(self.folder + '/pulls_opened_closed_merged.eps',
                        bbox_inches='tight')
            plt.clf()

        else:
            print('Error processing ' + self.project_name + ' project.')
            print(
                '\033[97m\033[1m-> Pull request file does not exist.\033[0m Please, collect it first.')

    def newcomers_forecasting(self):
        if os.path.isfile(self.folder + '/first_contributions.txt'):
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')
            dates = []

            for line in newcomer_file:
                entry_date = line.rsplit(',', 1)[1].strip()

                if entry_date:
                    dates.append({'Date': entry_date, 'Occorrence': 1})

            data_frame = pandas.DataFrame(dates)
            data_frame = data_frame.set_index('Date')
            data_frame.index.name = None
            data_frame.index = pandas.to_datetime(data_frame.index)
            y = data_frame['Occorrence'].resample('MS').sum()
            y = y.fillna(y.bfill())

            p = d = q = range(0, 2)
            pdq = list(itertools.product(p, d, q))
            seasonal_pdq = [(x[0], x[1], x[2], 12)
                            for x in list(itertools.product(p, d, q))]

            aic_dictionary = {}
            for param in pdq:
                for param_seasonal in seasonal_pdq:
                    try:
                        mod = sm.tsa.statespace.SARIMAX(y,
                                                        order=param,
                                                        seasonal_order=param_seasonal,
                                                        enforce_stationarity=False,
                                                        enforce_invertibility=False)

                        results = mod.fit()
                        aic_dictionary[results.aic] = [param, param_seasonal]
                    except:
                        continue

            best_order, best_seasonal_order = aic_dictionary[
                min(aic_dictionary, key=aic_dictionary.get)]
            print min(aic_dictionary, key=aic_dictionary.get)

            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=best_order,
                                            seasonal_order=best_seasonal_order,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()
            last = max(y.index)

            pred_dynamic = results.get_prediction(start=last.replace(
                month=last.month - 6).date(), dynamic=True, full_results=True)
            pred_dynamic_ci = pred_dynamic.conf_int()
            y_forecasted = pred_dynamic.predicted_mean
            mse = ((y_forecasted - y) ** 2).mean()
            print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
            pred_uc = results.get_forecast(steps=12)
            pred_ci = pred_uc.conf_int()

            ax = y.plot(label='Newcomers', figsize=(20, 15))
            pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
            ax.fill_between(pred_ci.index,
                            pred_ci.iloc[:, 0],
                            pred_ci.iloc[:, 1], color='k', alpha=.25)
            ax.set_xlabel('Date')
            ax.set_ylabel('# Newcomers')

            plt.legend()
            plt.savefig(self.folder + '/newcomers_predict.png',
                        bbox_inches='tight')
            plt.clf()

# Main method. Instantiate one object for each of the projects.
if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)

    for language in dictionary.keys():
        repositories = dictionary[language]['items']
        for repository in repositories:
            if 'C' in language:
                folder = 'Dataset' + '/' + language + '/' + repository['name']

                for f in os.listdir(folder):
                    if '.png' in f or '.eps' in f:
                        os.remove(folder + '/' + f)

                Chart = RepositoryChart(folder, repository['name'])
                Chart.newcomers_pulls_and_contributions()
                Chart.newcomers_forks_and_stars()
                Chart.pulls_opened_closed_and_merged()
                # Chart.newcomers_forecasting()
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
