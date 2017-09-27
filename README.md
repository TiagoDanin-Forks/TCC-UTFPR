# Term Paper / Repository
In this repository, you will find all the files related to the processes of data collection and chart creation used in Luiz Felipe's research. You will be able to reproduce and modify both of these processes based on the scripts we made available in this repository. We also provide our website source code if you want to be inspired by it to create new projects. If you experience problems while running these codes, please, feel free to contact us. 

Read our paper at: #

## Data Collection
The data collection process is based on two collection sources: <b>GitHub API </b> (V3) and <b>Git Repositories</b>. Data available in the API are collected using web requisitions in python, and data available in the repositories are collected using <i>git logs</i> in shellscript. All the source code is available at <a href="https://github.com/fronchetti/TCC-UTFPR/tree/master/Crawler">Crawler<a> folder. However, to make it simpler, we created a class that abstracts the execution process. If you want to reproduce our dataset, just execute <a href="https://github.com/fronchetti/TCC-UTFPR/blob/master/data_collector.py">this script</a>.

`NOTE: Please, to a complete and successful execution, read the comments in the code and change values when necessary.`

## Chart Creation
The charts creation process depends of what kind of chart you want to generate. There are two options: If you want to created charts related to all the projects at once, use this script. If you aim to created charts related to a single project, use this script. The scripts we made available are based on the dataset folder organization we created with the data collection process. If you want to create charts to a specific project, please, modify our code (We already tried to make it simple for this purpose!). In the chart creation process, we used <b>Matplotlib</b>, a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats. Reading your documentation is a good way to get started!

## Contact
Luiz Felipe Fronchetti Dias [Student] -- luizdias@alunos.utfpr.edu.br <br>
Igor Scaliante Wiese [Advisor] -- igor@utfpr.edu.br <br>
Igor Steinmacher [Advisor] -- igorfs@utfpr.edu.br <br>
Gustavo Pinto [Advisor] -- ghlp@cin.ufpe.br
