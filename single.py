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
    from matplotlib.ticker import MultipleLocator
    import itertools
    import pandas
    import statsmodels.api as sm
    import json
    import os
except ImportError as error:
    raise ImportError(error)

# Sets chart stylesheet (Matplotlib Gallery)
plt.style.use('bmh')


class RepositoryChart():

    # Initial method. Sets values used during the entire process.
    def __init__(self, folder, project_name):
        self.folder = folder
        self.project_name = project_name

    # Line chart method. Creates a time series chart comparing pull requests,
    # newcomers and commits.
    def newcomers_pulls_and_contributions(self):
        if os.path.isfile(self.folder + '/pull_requests.json') and os.path.isfile(self.folder + '/first_contributions.txt') and os.path.isfile(self.folder + '/contributions.txt'):
            contribution_file = open(self.folder + '/contributions.txt', 'r')
            pull_file = json.load(
                open(self.folder + '/pull_requests.json', 'r'))
            newcomer_file = open(self.folder + '/first_contributions.txt', 'r')

            pull_list = []
            newcomer_list = []
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

            pull_x_axis = [pull_tuple[0]
                           for pull_tuple in pull_ordered_list]
            pull_y_axis = [pull_tuple[1]
                           for pull_tuple in pull_ordered_list]

            newcomer_x_axis = [newcomer_tuple[0]
                               for newcomer_tuple in newcomer_ordered_list]
            newcomer_y_axis = [newcomer_tuple[1]
                               for newcomer_tuple in newcomer_ordered_list]

            contribution_x_axis = [contribution_tuple[0]
                                   for contribution_tuple in contribution_ordered_list]
            contribution_y_axis = [contribution_tuple[1]
                                   for contribution_tuple in contribution_ordered_list]

            ax = host_subplot(111, axes_class=AA.Axes)
            plt.subplots_adjust(right=0.75)

            ax_second = ax.twinx()
            ax_third = ax.twinx()
            offset = 60
            new_fixed_axis = ax_third.get_grid_helper().new_fixed_axis
            ax_third.axis["right"] = new_fixed_axis(loc="right", axes=ax_third,
                                                    offset=(offset, 0))
            ax_third.axis["right"].toggle(all=True)

            ax.set_xlabel(u'Years')
            ax.set_ylabel(u'# Newcomers')
            ax.set_ylim(ymin=0)
            ax.set_ylim(0, 141)
            ax.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax.yaxis.set_major_locator(MultipleLocator(20))
            ax.yaxis.set_minor_locator(MultipleLocator(5))
            line_newcomer, = ax.plot(newcomer_x_axis, newcomer_y_axis,
                                     '-', linewidth=2, label='Newcomers')

            ax_second.set_xlabel(u'Years')
            ax_second.set_ylabel(u'# Pull requests')
            ax_second.set_ylim(ymin=0)
            ax_second.set_ylim(0, 400)
            ax_second.set_xlim(datetime(2004, 1, 1), datetime(2018, 1, 1))
            ax_second.yaxis.set_major_locator(MultipleLocator(50))
            ax_second.yaxis.set_minor_locator(MultipleLocator(10))
            line_pull, = ax_second.plot(pull_x_axis,
                                        pull_y_axis, '-.', color='green', linewidth=2, label='Pull requests')

            ax_third.set_xlabel(u'Years')
            ax_third.set_ylabel(u'# Commits')
            ax_third.set_ylim(ymin=0)
            ax_third.set_ylim(0, 1201)
            ax_third.set_xlim(datetime(2010, 1, 1), datetime(2018, 1, 1))
            ax_third.yaxis.set_major_locator(MultipleLocator(100))
            ax_third.yaxis.set_minor_locator(MultipleLocator(50))
            line_contribution, = ax_second.plot(contribution_x_axis,
                                                contribution_y_axis, '--', color='crimson', linewidth=2, label='Commits')

            plt.legend((line_newcomer, line_pull, line_contribution),
                       ('Newcomers', 'Pull requests', 'Commits'))
            plt.title(self.project_name)
            plt.savefig(self.folder + '/newcomers_contributions_pulls.png',
                        bbox_inches='tight')
            plt.clf()

        else:
            print('Error processing ' + self.project_name + ' project.')
            print(
                '\033[97m\033[1m-> Newcomer or pull request file does not exist.\033[0m Please, collect them first.')

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
            '''
            No tipo estatico, os resultados do mean squared error foram muito altos. Deveriam ser baixos. 
            pred = results.get_prediction(start=last.replace(month = last.month - 6).date(),dynamic=False)
            pred_ci = pred.conf_int()
            y_forecasted = pred.predicted_mean
            mse = ((y_forecasted - y) ** 2).mean()
            print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
            Abaixo eu tento usar a predicao dinamica:
            '''
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
languages = ['C', 'C++', 'Clojure', 'Erlang',
             'Go', 'Haskell', 'Java', 'JavaScript', 'Objective-C',
             'Perl', 'PHP', 'Python', 'Ruby', 'Scala', 'TypeScript']

if os.path.isfile('projects.json'):
    with open('projects.json', 'r') as file:
        dictionary = json.load(file)

    for language in dictionary.keys():
        repositories = dictionary[language]['items']
        for repository in repositories:
            folder = 'Dataset' + '/' + language + '/' + repository['name']
            Chart = RepositoryChart(folder, repository['name'])
            Chart.newcomers_pulls_and_contributions()
            Chart.newcomers_forecasting()
else:
    print('Error processing projects.json file.')
    print('\033[97m\033[1m-> A file with a projects list does not exist. \033[0m Please, collect it first.')
