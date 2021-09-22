import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Initially 3 people did it correctly
git_usernames = ['tic',
'tballard34',
'Kalvinci',
'jackieannec'
'aparnakishore',
'katiemartins',
'sidman00',
'vgcecchetti',
'Ryphilen',
'kothmann1',
'asummerville',
'Mikokokokoto',
'ShahiHub',
'elixir-1',
'ShreyesBhat']


#attempted to automate getting data but too many variations 
def get_git_data_online(git_usernames):
    for username in git_usernames:
        response = requests.get("https://raw.githubusercontent.com/"+username+"/smart_and_health_buildings/main/README.md")
        if response.status_code==404:
            response = requests.get("https://raw.githubusercontent.com/"+username+"/smart_and_health_buildings/main/Lab_1/README.md")
        print(response.text)
        
       
def get_git_data_csv(filename):
    git_data = pd.read_csv(filename)
    return git_data

def question3(dataframe):
    #Question 3
    elmo_count = dataframe['Seaseme'].value_counts()['Elmo']
    return elmo_count
def question4(dataframe):
    #question 4
    cookie_night_owl = dataframe[(dataframe['Sleep_schedule']=='Night Owl') & (dataframe['Seaseme']=='Cookie Monster')].count()['Alias']
    print(cookie_night_owl)
    return cookie_night_owl
def question5(dataframe):
    #question 5
    #How many students do not support Elmo, does not play rock, and are morning birds?
    question5_solution = dataframe[(dataframe['Sleep_schedule']=='Morning bird') & (dataframe['Seaseme']!='Elmo') & (dataframe['RPS']!="Rock") ].count()['Alias']
    print(question5_solution)
    return question5_solution

def graph_answers(dataframe):
    
    y=[question3(dataframe),question4(dataframe),question5(dataframe)]
    x = ['Question 3','Question 4','Question 5']
    print(y)
    sns.catplot(x=x,y=y,kind="bar",data=dataframe)
    plt.show()






    


git_data = get_git_data_csv('lab2_data.csv')
graph_answers(git_data)





