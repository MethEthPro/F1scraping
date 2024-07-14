import requests
from bs4 import BeautifulSoup as soup
import time,pandas
import sys
import datetime
now = datetime.datetime.now()
curr_year = now.year


def get_page(url):
    page = requests.get(url, headers={
        "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"})
    doc = soup(page.content, "html.parser")
    return doc


def get_data(doc):
    site_wrapper = doc.find(class_="site-wrapper")
    main = site_wrapper.find(class_="template template-resultsarchive")
    inner_class = main.find(class_="inner-wrap ResultArchiveWrapper")
    result_archive = inner_class.find(class_="ResultArchiveContainer")
    results_archive_wrapper = result_archive.find(
        class_="resultsarchive-wrapper")
    content = results_archive_wrapper.table
    tbody = content.tbody
    return tbody

def get_team_name(tbody):
    teams_this_season = []
    tds_for_teams = tbody.find_all(
        "a", class_="dark bold uppercase ArchiveLink")
    for td_for_teams in tds_for_teams:
        team = td_for_teams.string
        teams_this_season.append(team)
        #print("Team:", team)
    return teams_this_season


def choose_team(team):
    print("0: for constructor standings")
    for i in range(len(team)):
        print(f"{i+1}: {team[i]}")
    user_input = input ("please choose a team to see results of that team for each race or 0 for constructor standings of that year\n")

    return user_input
mapped_dic = {}

def get_total_ponts(tbody):
    points_this_season = []
    tds_for_points = tbody.find_all(
        "td", class_="dark bold")
    for td_for_point in tds_for_points:
        team = td_for_point.string
        points_this_season.append(team)
        # print("Team:", team)
    return points_this_season

def get_track(tbody):
    tracks_this_season = []
    tds_for_tracks = tbody.find_all(
        "a", class_="dark ArchiveLink")
    for td_for_track in tds_for_tracks:
        track = td_for_track.string
        tracks_this_season.append(track)
        # print("Team:", team)
    return tracks_this_season

def date_of_grand_prix(tbody):
    dates_this_season = []
    tds_for_dates = tbody.find_all(
        "td", class_="dark bold")
    i = 0
    for td_for_date in tds_for_dates:
        if i %2 == 0:
            date = td_for_date.string
            dates_this_season.append(date)
        i = i +1
        # print("Team:", team)
    return dates_this_season

def point_of_grand_prix(tbody):
    points_this_grand_prix = []
    tds_for_points = tbody.find_all(
        "td", class_="dark bold")
    i = 0
    for td_for_point in tds_for_points:
        if i %2 != 0:
            point = td_for_point.string
            points_this_grand_prix.append(float(point))
        i = i +1
        # print("Team:", team)
    return points_this_grand_prix

def get_mapped_dic(team):
    global mapped_dic
    for i in range(len(team)):
        team_name = team[i].lower()

        final_team_name = team_name.replace(' ',"_")
        mapped_dic[i+1] = final_team_name
    return mapped_dic


the_dic_all = {}
def dic_for_constructor_standings(team_list,points_list,y):
    global the_dic_all
    the_dic_all["TEAM"] = team_list
    the_dic_all["PTS"] = points_list
    the_dic_all["YEAR"] = y

    return the_dic_all

def dic_for_individual_team(grand_prix_list,date_list,points_list,y):
    global the_dic_all
    the_dic_all["GRAND PRIX"] = grand_prix_list
    the_dic_all["DATE"] = date_list
    the_dic_all['PTS'] = points_list
    the_dic_all['YEAR'] = y

    return the_dic_all


dataframe_list = []
def save_csv_file(dic_list,file_name):
    global dataframe_list
    for dic in dic_list:

        df = pandas.DataFrame(dic)
        dataframe_list.append(df)

    final_df = pandas.concat(dataframe_list)

    final_df.to_csv(file_name,index=0)



dic_list_constructor = []
dic_list_individual= []

def get_input():
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






def main():

    year = get_input()
    len_year = len(year)
    print("either go for all or go for one you cant switch in between")
    for y in year:
        print("Scraping year", y)
        url = "https://www.formula1.com/en/results.html/" + \
            str(y)+"/team.html"
        doc = get_page(url)
        tbody = get_data(doc)
        team = get_team_name(tbody)
        user_choice = choose_team(team)
        if int(user_choice) == 0:
            dic_list_constructor = []
            total_points_list = get_total_ponts(tbody)
            dic_constructor = dic_for_constructor_standings(team,total_points_list,y)
            dic_list_constructor.append(dic_constructor)
            save_csv_file(dic_list_constructor, file_name="constructor_standings.csv")



        else:
            dic_list_individual = []
            mapped_dic = get_mapped_dic(team)
            team_name = mapped_dic[int(user_choice)]
            link = "https://www.formula1.com/en/results.html/"+str(y)+"/team/"+ team_name+".html"
            team_doc = get_page(link)
            team_tbody = get_data(team_doc)
            grand_prix_list = get_track(team_tbody)
            date_list = date_of_grand_prix(team_tbody)
            points_on_gp = point_of_grand_prix(team_tbody)
            dic_individual = dic_for_individual_team(grand_prix_list,date_list,points_on_gp,y)
            dic_list_individual.append(dic_individual)
            save_csv_file(dic_list_individual, file_name="individual_performance.csv")


        time.sleep(1)

    print("Process Finished Successfully")


main()
