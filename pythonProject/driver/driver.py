import requests
from bs4 import BeautifulSoup as soup
import sys,datetime
import pandas


# we will use a dictionary with the key being driver positions and values being a list
# with first element being driver name , then nationality , then car , then pts
# and we also need the driver code like VALBOT01 for VALTERRI BOTTAS s
# so its like first 3 letters of first name and second name and then 01

now= datetime.datetime.now()
curr_year = now.year
def get_page(url):
    page = requests.get(url, headers={
        "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"})
    doc = soup(page.content, "html.parser")
    return doc

def get_all_drivers_tbody(y):
    url = "https://www.formula1.com/en/results.html/"+str(y)+"/drivers.html"
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

def get_driver_tbody(y,driver_name,driver_code):
    url = "https://www.formula1.com/en/results.html/" + str(y) + "/drivers/" + str(driver_code.upper()) + '/' + str(driver_name.replace(" ","-").lower()) + '.html'
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

def get_driver_grand_prix_list(tbody):
    driver_grand_prix_list = []
    tds = tbody.find_all("a", class_="dark ArchiveLink")
    for td in tds :
        grand_prix = td.string
        driver_grand_prix_list.append(grand_prix)

    return driver_grand_prix_list

def get_grand_prix_date(tbody):
    dates_list = []
    tds = tbody.find_all("td", class_="dark bold")
    i = 1
    for td in tds:
        date = td.string
        if i%2 != 0:
            dates_list.append(date)
        i = i + 1

    return dates_list

def get_grand_prix_points(tbody):
    points_list = []
    tds = tbody.find_all("td", class_="dark bold")
    i = 1
    for td in tds:
        point = td.string
        if i%2 == 0:
            points_list.append(point)
        i = i + 1

    return points_list

def get_grand_prix_position(tbody):
    position_list = []
    tds = tbody.find_all("td", class_="dark")
    i = 1
    for td in tds:
        position = td.string
        if i == 1:
            i = i+1
        elif i == 2 :
            position_list.append(position)
            i = i + 1
        elif i == 3:
            i = 1


    return position_list

def get_driver_car(tbody) :
    car_list = []
    tds = tbody.find_all("a", class_="grey semi-bold uppercase ArchiveLink")
    for td in tds:
        car = td.string
        car_list.append(car)

    return car_list

def get_driver_name(tbody):
    list_of_names = []
    tds = tbody.find_all("a", class_="dark bold ArchiveLink")
    for td in tds:
        names = td.find_all(
            True, {"class": ["hide-for-tablet", "hide-for-mobile"]})
        if not names:
            print(names)
        else:
            name = names[0].string + " " + names[1].string
            list_of_names.append(name)

    return list_of_names

def get_driver_nationality(tbody):
    nationalities = []
    tds_for_nat = tbody.find_all(
        "td", class_="dark semi-bold uppercase")
    for td_for_teams in tds_for_nat:
        team = td_for_teams.string
        nationalities.append(team)
        # print("Team:", team)

    return nationalities

def get_team_name(tbody):
    list_of_teams = []
    tds = tbody.find_all("a", class_="grey semi-bold uppercase ArchiveLink")
    for td in tds:
        list_of_teams.append(td.text)

    return list_of_teams

def get_points(tbody):
    list_of_points = []
    tds = tbody.find_all("td",class_='dark bold')

    for td in tds:
        list_of_points.append(td.text)


    return list_of_points

def get_driver_code(names_list):
    driver_code_list = []
    for name in names_list:
        new_name = name.split(' ')
        final_name = new_name[0][:3] + new_name[1][:3] +'01'
        driver_code_list.append(final_name)

    return driver_code_list

the_dic = {}
the_dic_2 = {}
def create_one_driver_dic(driver_name,grand_prix_list,date_list,car_list,pos_list,pts_list,y):
    global the_dic_2

    the_dic_2["DRIVER"] = driver_name
    the_dic_2['GRAND PRIX'] = grand_prix_list
    the_dic_2['DATE'] = date_list
    the_dic_2['CAR'] = car_list
    the_dic_2['RACE POSITION'] = pos_list
    the_dic_2['PTS'] = pts_list
    the_dic_2['YEAR'] = y

    return the_dic_2

def create_all_drivers_dic(name_list,nat_list,team_list,pts_list,driver_code_list,y):
    global the_dic
    position_list = []
    for i in range(len(name_list)):

        position_list.append(i)

    the_dic['POS'] = position_list
    the_dic['DRIVER'] = name_list
    the_dic['NATIONALITY'] = nat_list
    the_dic['CAR'] = team_list
    the_dic['PTS'] = pts_list
    the_dic['CODE'] = driver_code_list
    the_dic['YEAR'] = y


    return the_dic

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


dataframe_list = []
def print_choices(name_list):
    print(f"0 : for all")
    for i in range(len(name_list)):
        print(f"{i+1} : {name_list[i]}")

def save_csv_file(dic_list,file_name):
    global dataframe_list
    for dic in dic_list:

        df = pandas.DataFrame(dic)
        dataframe_list.append(df)

    final_df = pandas.concat(dataframe_list)

    final_df.to_csv(file_name,index=0)

the_all_drivers_dic_list = []
the_one_driver_dic_list = []

def main():
    year = get_input()
    print("please be consistent if you choose all then go for all for each year , if you chose a driver then dont go for all for years left ")
    for y in year:
        print(f"scraping year {y}")

        tbody = get_all_drivers_tbody(y)
        names_list = get_driver_name(tbody)
        print_choices(names_list)
        user_choice = input("choose the number next to driver to see his results of the year or "
                            "choose 0 to show results of all drivers across the year you selected\n")
        nat_list = get_driver_nationality(tbody)
        team_list = get_team_name(tbody)
        pts_list = get_points(tbody)
        driver_code_list = get_driver_code(names_list)


        if int(user_choice) == 0:
            the_all_drivers_dic_list = []

            the_all_drivers_dic = create_all_drivers_dic(names_list, nat_list, team_list, pts_list, driver_code_list,y)
            the_all_drivers_dic_list.append(the_all_drivers_dic)
            save_csv_file(the_all_drivers_dic_list, file_name="driver_standings_all.csv.")



        else:
            the_one_driver_dic_list = []
            driver_code = driver_code_list[int(user_choice)-1]
            driver_name = names_list[int(user_choice)-1]
            driver_tbody = get_driver_tbody(y,driver_name,driver_code)
            driver_grand_prixs = get_driver_grand_prix_list(driver_tbody)
            dates_ = get_grand_prix_date(driver_tbody)
            car_ = get_driver_car(driver_tbody)
            points_ = get_grand_prix_points(driver_tbody)
            positions_ = get_grand_prix_position(driver_tbody)
            the_one_driver_dic = create_one_driver_dic(driver_name,driver_grand_prixs,dates_,car_,positions_,points_,y)

            the_one_driver_dic_list.append(the_one_driver_dic)
            save_csv_file(the_one_driver_dic_list,file_name="Driver_standings_of_driver.csv")












main()