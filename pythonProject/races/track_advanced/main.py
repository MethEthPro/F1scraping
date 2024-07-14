import requests
from bs4 import BeautifulSoup as soup
import sys
import datetime
import pandas
import os
now = datetime.datetime.now()
curr_year = now.year


def get_page(url):
    page = requests.get(url, headers={
        "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"})
    doc = soup(page.content, "html.parser")
    return doc


def get_tbody(race_name, y):
    url = "https://www.formula1.com/en/results.html/"+str(y)+"/races/" + \
        race_name+"/race-result.html"
    doc = get_page(url)
    site_wrapper = doc.find(class_="site-wrapper")
    main = site_wrapper.find(class_="template template-resultsarchive")
    inner_class = main.find(class_="inner-wrap ResultArchiveWrapper")
    result_archive = inner_class.find(class_="ResultArchiveContainer")
    results_archive_wrapper = result_archive.find(
        class_="resultsarchive-wrapper")
    content = results_archive_wrapper.table
    tbody = content.tbody

    return tbody

def get_tbody_stats(link):
    url = link
    doc = get_page(url)
    site_wrapper = doc.find(class_="site-wrapper")
    main = site_wrapper.find(class_="template template-resultsarchive")
    inner_class = main.find(class_="inner-wrap ResultArchiveWrapper")
    result_archive = inner_class.find(class_="ResultArchiveContainer")
    results_archive_wrapper = result_archive.find(
        class_="resultsarchive-wrapper")
    content = results_archive_wrapper.table
    tbody = content.tbody

    return tbody

def get_driver_position(driver_name):
    driver_position_list = []
    i = 1
    for tag in driver_name:
        driver_position_list.append(i)
        i = i + 1

    return driver_position_list


def get_driver_number(tbody):
    list_of_driver_number = []
    tds = tbody.find_all("td",class_="dark hide-for-mobile")
    for td in tds :
        numbers =  td.get_text()
        if not numbers:
            continue
        else:
            list_of_driver_number.append(numbers)


    return(list_of_driver_number)


def get_driver_name(tbody):
    list_of_names = []
    tds = tbody.find_all("td", class_="dark bold")
    for td in tds:
        names = td.find_all(
            True, {"class": ["hide-for-tablet", "hide-for-mobile"]})
        if not names:
            continue
        else:
            name = names[0].string + " " + names[1].string
            list_of_names.append(name)

    return list_of_names


def get_team_name(tbody):
    list_of_teams = []
    tds = tbody.find_all("td", class_="semi-bold uppercase hide-for-tablet")
    for td in tds:
        list_of_teams.append(td.text)

    return list_of_teams


def track_year_list(value,driver_name_list):
    value_list = []

    for item in driver_name_list:
        value_list.append(value)
    return value_list
def get_laps(tbody,num):
    list_of_completed_laps = []
    tds = tbody.find_all("td", class_="bold")
    final_values = []
    possible_values = []
    j = 1
    for k in range(num):
        possible_values.append(j)
        j = j + 5

    for td in tds:
            list_of_completed_laps.append(td.text)
    for j in possible_values:
        if j < len(list_of_completed_laps):
            final_values.append(list_of_completed_laps[j])



    return final_values

def extra_1(tbody,num):
    list_of_time_of_day = []
    tds = tbody.find_all("td", class_="dark bold")
    final_values = []
    possible_values = []
    j = 1
    for k in range(num):
        possible_values.append(j)
        j = j + 4
    for td in tds:
            list_of_time_of_day.append(td.text)

    for j in possible_values:
        if j < len(list_of_time_of_day):
            final_values.append(list_of_time_of_day[j])
    for z in range(len(final_values)):
        if z < len(final_values):
            if final_values[z] == '':
                final_values[z] = 0

    return final_values

def extra_2(tbody,num):

    list_of_time = []
    possible_values = []
    final_values = []
    tds = tbody.find_all("td", class_="dark bold")
    j = 2
    for k in range(num):
        possible_values.append(j)
        j = j + 4


    for td in tds:

        list_of_time.append(td.text)

    for j in possible_values:
        if j<len(list_of_time):
            final_values.append(list_of_time[j])

    for z in range(len(final_values)):
        if z < len(final_values):
            if final_values[z] == '':
                final_values[z] = 0

    return final_values


def extra_3(tbody,num):

    list_of_avg_speed = []

    possible_values = []
    final_values = []
    tds = tbody.find_all("td", class_="dark bold")
    j = 3
    for k in range(num):
        possible_values.append(j)
        j = j + 4
    for td in tds:

        list_of_avg_speed.append(td.text)

    for j in possible_values:
        if j < len(list_of_avg_speed):
            final_values.append(list_of_avg_speed[j])

    for z in range(len(final_values)):
        if z < len(final_values):
            if final_values[z] == '':
                final_values[z] = 0
    return final_values

def get_q_laps(tbody):
    list_of_q_laps= []
    tds = tbody.find_all("td",class_="semi-bold hide-for-mobile")
    for td in tds :
        numbers =  td.get_text()
        if not numbers:
            continue
        else:
            list_of_q_laps.append(numbers)


    return(list_of_q_laps)


def get_ul_options(race_name, y):
    url = "https://www.formula1.com/en/results.html/"+str(y)+"/races/" + \
        race_name+"/race-result.html"
    doc = get_page(url)
    site_wrapper = doc.find(class_="site-wrapper")
    main = site_wrapper.find(class_="template template-resultsarchive")
    inner_class = main.find(class_="inner-wrap ResultArchiveWrapper")
    result_archive = inner_class.find(class_="ResultArchiveContainer")
    results_archive_wrapper = result_archive.find(
        class_="resultsarchive-wrapper")
    ul = results_archive_wrapper.ul

    return ul


def get_races(doc):
    main = doc.main
    article = main.article
    container = article.find(class_="resultsarchive-filter-container")
    rarchive1 = container.find(
        class_="resultsarchive-filter-wrap")
    rarchive2 = rarchive1.find_next(class_="resultsarchive-filter-wrap")
    rarchive3 = rarchive2.find_next(class_="resultsarchive-filter-wrap")
    lis = rarchive3.find_all("li", class_="resultsarchive-filter-item")
    race_links = []
    race_in_year = []
    # bunu dict ile yapmaya calis , try to use a dictionary here
    for li in lis:
        race_links.append([item["data-value"]
                           for item in li.find_all() if "data-value" in item.attrs])
    for i in range(len(race_links)) :
        race_in_year.append(race_links[i][0].strip("-/1234567890"))

    return race_links

def get_year_input():
    year = []

    try :

        ipt = input("What year do you want?\nIf multiple, seperate with comma,if you want range then give starting year and ending year separated with commas\n")
        ipt = ipt.split(",")
        garbage = int(ipt[0])

    except ValueError :
        print("please enter an year next time")
        sys.exit(1)

    else:

        if len(ipt) >2:
            while int(ipt[0]) < 1950 or int(ipt[1]) > curr_year:
                print(f"Trying to act smart. Year should be given between 1950 and {curr_year}.a\n")
                sys.exit(1)
            for y in ipt:
                year.append(int(y))
                year=set(year)
                year = list(year)
        elif len(ipt) == 2:
            while int(ipt[0]) < 1950 or int(ipt[1]) > curr_year or int(ipt[0]) > curr_year or int(ipt[1]) < 1950:
                print(f"Trying to act smart. Year should be given between 1950 and {curr_year}.b\n")
                sys.exit(1)
            if ipt[0] > ipt[1] :
                for y in ipt:
                    year.append(int(y))
            else:
                for y in range(int(ipt[0]), int(ipt[1]) + 1):
                    year.append(y)

        elif len(ipt) == 1:
            while int(ipt[0]) < 1950 or int(ipt[0]) > curr_year:
                print(f"Trying to act smart. Year should be given between 1950 and {curr_year}.c\n")
                sys.exit(1)
            year.append(int(ipt[0]))
    print(year)
    return year


def get_race_input(races, y):
    print("These are the races of", y,
          "select the race you want by typing number of it.")

    for i in range(len(races)):
        print(i, "-", races[i][0].strip("-/1234567890"))
    ipt = input("Enter: ")
    while int(ipt) > len(races) or int(ipt) < 0:
        ipt = input("Get your shit together and try again: , choose from the range provided  ")
    # print("selected:", races[int(ipt)])
    if int(ipt) == 0:
        print("cant fetch ")
        sys.exit(1)
    else:
        print("selected:", races[int(ipt)][0].strip("-/1234567890"))
        return races[int(ipt)][0]

def get_choices_list(ul) :
    list_of_choices = []
    choices = ul.find_all("a", class_="side-nav-item-link ArchiveLink")
    print('these are the choices')
    for choice in choices:
        actual_choice = choice.string
        list_of_choices.append(actual_choice)


    return list_of_choices

the_final_mapping_dic = {
    'RACE RESULT': 'race-result',
    'FASTEST LAPS': 'fastest-laps',
    'PIT STOP SUMMARY': 'pit-stop-summary',
    'STARTING GRID': 'starting-grid',
    'QUALIFYING': 'qualifying',
    'PRACTICE 3': 'practice-3',
    'PRACTICE 2': 'practice-2',
    'PRACTICE 1': 'practice-1',
    'SPRINT' : 'sprint-results',
    'SPRINT GRID': 'sprint-grid',
    'SPRINT QUALIFYING': 'sprint-qualifying',
    'SPRINT SHOOTOUT': 'sprint-shootout'

}
the_prior_mapping_dic={}

def mapping(list_of_choices,user_choice) :
    global the_prior_mapping_dic
    for i in range(len(list_of_choices)):
        the_prior_mapping_dic[i+1] = list_of_choices[i].upper()

    return the_prior_mapping_dic[int(user_choice)]

def get_choice_input(list_of_choices):

    for i in range(len(list_of_choices)):
        print(f'{i+1} : {list_of_choices[i]}')
    print(
        "we have currently only scraped data of qualifying and fastest lap , rest all are in development so please choose wisely")
    user_choice = input('please enter number of the field you want stats of ')


    return user_choice

the_dic_all = {}

def create_dic_qualifying(drivers_standings_list, teams_list, lap_no_list, q1_list, q2_list,q3_list, year, track):
    global the_dic_all
    the_dic_all['GRAND PRIX'] = track
    the_dic_all['DRIVER STANDINGS'] = drivers_standings_list
    the_dic_all['TEAMS'] = teams_list
    the_dic_all['Q1'] = q1_list
    the_dic_all['Q2'] =q2_list
    the_dic_all['Q3'] = q3_list
    the_dic_all['LAPS'] = lap_no_list
    the_dic_all['YEAR'] = year

    return the_dic_all

def create_dic_fastest_laps(drivers_standings_list,teams_list,lap_no_list,time_of_day,time_list,avg_speed_list,year_list,track_list):
    global the_dic_all
    the_dic_all['GRAND PRIX'] = track_list
    the_dic_all['DRIVER STANDINGS'] = drivers_standings_list
    the_dic_all['TEAMS'] = teams_list
    the_dic_all['TIME OF DAY'] = time_of_day
    the_dic_all['TIME'] = time_list
    the_dic_all['AVG SPEED'] = avg_speed_list
    the_dic_all['LAPS'] = lap_no_list
    the_dic_all['YEAR'] = year_list

    return the_dic_all



dataframe_list = []
def save_csv_file(dic_list,file_name):
    global dataframe_list
    for dic in dic_list:

        df = pandas.DataFrame(dic)
        dataframe_list.append(df)

    final_df = pandas.concat(dataframe_list)

    final_df.to_csv(file_name,index=0)

dic_list_fastest_laps = []
dic_list_qualifying = []

def main():
    year = get_year_input()
    len_year = len(year)
    print(
        "please be consistent if you choose all then go for all for each year , if you chose a driver then dont go for all for years left ")
    for y in year:
        print("Scraping year", y)
        url = "https://www.formula1.com/en/results.html/"+str(y)+"/races.html"
        doc = get_page(url)
        race_links = get_races(doc)
        print(race_links)
        race_name = get_race_input(race_links, y)
        dic_list = []
        print(race_name)
        tbody = get_tbody(race_name, y)
        ul = get_ul_options(race_name,y)

        choice_list = get_choices_list(ul)

        user_choice = get_choice_input(choice_list)
        mapped_value = mapping(choice_list,user_choice)
        final_value_for_link = the_final_mapping_dic[mapped_value]
        link = "https://www.formula1.com/en/results.html/" +str(y) +"/races/" + str(race_name) + "/"+str(final_value_for_link)+".html"


        if mapped_value == "FASTEST LAPS":
            dic_list_fastest_laps = []
            tbody_2 = get_tbody_stats(link)
            driver_name_list = get_driver_name(tbody_2)
            driver_position = get_driver_position(driver_name_list)
            driver_number_list = get_driver_number(tbody_2)
            team_name_list = get_team_name(tbody_2)
            laps_list = get_laps(tbody_2,len(driver_name_list))
            time_of_day = extra_1(tbody_2,len(driver_name_list))
            time = extra_2(tbody_2,len(driver_name_list))
            avg_speed = extra_3(tbody_2,len(driver_name_list))
            year_list = track_year_list(y,driver_name_list)
            track_list = track_year_list(race_name,driver_name_list)
            dic_fastest_laps = create_dic_fastest_laps(driver_name_list,team_name_list,laps_list,time_of_day,time,avg_speed,year_list,track_list)
            dic_list_fastest_laps.append(dic_fastest_laps)
            save_csv_file(dic_list_fastest_laps,file_name="fastest_laps_info.csv")

        elif mapped_value == "QUALIFYING" :
            dic_list_qualifying = []
            tbody_2 = get_tbody_stats(link)
            driver_number_list = get_driver_number(tbody_2)
            driver_name_list = get_driver_name(tbody_2)
            driver_position = get_driver_position(driver_name_list)
            team_name_list = get_team_name(tbody_2)
            Q1 =extra_1(tbody_2,len(driver_name_list))
            Q2 = extra_2(tbody_2,len(driver_name_list))
            Q3 = extra_3(tbody_2,len(driver_name_list))
            q_lap = get_q_laps(tbody_2)
            dic_qualifying = create_dic_qualifying(driver_name_list,team_name_list,q_lap,Q1,Q2,Q3,y,race_name)
            dic_list_qualifying.append(dic_qualifying)
            save_csv_file(dic_list_qualifying,file_name="qualifying_info.csv")

main()
