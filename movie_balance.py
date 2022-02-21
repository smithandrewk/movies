#!/usr/bin/env python3
import pandas as pd
movies = pd.read_csv("m.csv")

while(True):
    x = movies.sample()
    y = movies.sample()
    x_title = x['Title'].values[0]
    y_title = y['Title'].values[0]
    choice = input(f'Do you like \n{x_title} \n\nor \n\n{y_title} better? \n\nPress 1 or 2.')
    if(choice=='1'):
        movies.loc[movies['Title'] == x_title,'Rating']+=1
    elif(choice=='2'):
        movies.loc[movies['Title'] == y_title,'Rating']+=1
    else:
        break
movies.to_csv('m.csv',index=False)
