#import requests
#from bs4 import BeautifulSoup
import pandas as pd

#alternative path
#r = requests.get('https://eurovisionworld.com/eurovision/2023')
#soup = BeautifulSoup(r.text, 'html.parser')
#results = soup.select('span', attrs={'table', ''})
#Just a moment...Enable JavaScript and cookies to continue

#This file creates the data_table.csv file from voting.txt, which is used in the main.py file. 

country_dict = {'at':'Austria', 'be':'Belgium', 'ch':'Switzerland', 'de':'Germany', 'dk':'Denmark', 'gb':'Great Britain', 'it':'Italy', 'lu':'Luxemburg', 'nl':'Netherlands', 'fr':'France', 'se':'Sweden', 'mc':'Monaco', 'no':'Norway', 'es':'Spain', 'fi':'Finnland', 'yu':'Yugoslavia', 'pt':'Portugal', 'ie':'Ireland', 'mt':'Malta', 'il':'Israel', 'gr':'Greek', 'tr':'Turkey', 'ma':'Morocco', 'cy':'Cyprus', 'is':'Iceland', 'ba':'Bosnia & Herzegovina', 'hr':'Croatia', 'si':'Slovenia', 'ee':'Estonia', 'hu':'Hungary', 'lt':'Lithuania', 'pl':'Poland', 'ro':'Romania', 'ru':'Russia', 'sk':'Slovakia', 'mk':'North Macedonia', 'lv':'Latvia', 'ua':'Ukrania', 'ad':'Andorra', 'al':'Albania', 'by':'Belarus', 'cs':'Serbia & Montenegro', 'bg':'Bulgaria', 'md':'Moldova', 'am':'Armenia', 'cz':'Czech Republic', 'ge':'Georgia', 'me':'Montenegro', 'rs':'Serbia', 'az':'Azerbaijan', 'sm':'San Marino', 'au':'Australia'}

df_bf2016 = pd.DataFrame(columns=['Year', 'Vote from', 'Vote to', 'Point'])
df_af2016 = pd.DataFrame(columns=['Year', 'Vote from', 'Vote to', 'Point', 'Jury', 'Public'])
with open(r'voting.txt', 'r', encoding='utf-8') as f:
    for _ in range(65):
        vote_row = []
        row = f.readline()
        row = row.rstrip()
        row = row.replace(' ', '')
        row = row.replace('],', '')
        row = row.replace('"', '')
        voting_list = row.split("[")
        year = int(voting_list[0].replace(',', ''))

        if year < 2016: 
            for i in range(1, len(voting_list)):
                voting_list[i] = voting_list[i].strip()
                vote = voting_list[i].split(",")

                if i == len(voting_list)-1:
                    vote[2] = vote[2].replace(']', '')

                df_bf2016.loc[len(df_bf2016)] = [year, country_dict[vote[0]], country_dict[vote[1]], int(vote[2])]
        
        else:
            for i in range(1, len(voting_list)):
                voting_list[i] = voting_list[i].strip()
                vote = voting_list[i].split(",")

                if i == len(voting_list)-1:
                    vote[4] = vote[4].replace(']', '')

                df_af2016.loc[len(df_af2016)] = [year, country_dict[vote[0]], country_dict[vote[1]], int(vote[2]), int(vote[3]), int(vote[4])]

df_all = df_bf2016.merge(df_af2016, how = 'outer')

df_all.to_csv(r'eurovision project\data_table.csv', sep='\t', index=False)