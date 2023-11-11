#---------------Задание 21-1------------------
from openpyxl import Workbook
import pandas as pd
import numpy as np
import matplotlib as plt
import random
table=pd.DataFrame(columns=['ФИО Студента','Оплатил ли учёбу?','Номер телефона студента','ФИО Преподавателя','Провёл занятий','Осталось занятий'])
df=pd.DataFrame(table)
dft=df.T
dft.to_excel('Pupil.xlsx')