# -*- coding: utf-8 -*-
# Author:  Felipe Fronchetti
# Contact: fronchettiemail@gmail.com
# Dataset folder have a large size with a huge amount of files depending of what you collect.
# This code is responsible for retrieve the necessary data of each project and move it to the website folder.
# If you have questions, mail me.

try:
    import os
    import csv
except ImportError as error:
    raise ImportError(error)
