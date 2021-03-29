from time import sleep
from datetime import date, time, datetime, timedelta
import xlrd
from selenium.webdriver.common.by import By
import csv
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pickle
import random as rd
import mouse as ms
import keyboard as kb
from selenium import webdriver
import logging


def miranda_1(driver,any_list):
    # Title. Have to click and select gender.
    xpath_gender = '//div[@class="col-lg-4 position-relative"]//select[@id="inputState"]'
    #Name Xpath
    xpath_name = '//div[@class="col-lg-4 position-relative"]//input[@type="text"][@id="nome"]'
    #Email Xpath
    xpath_email = '//div[@class="col-lg-4 position-relative"]//input[@type="email"][@id="email"]'
    # Day of Birth
    xpath_day = '//div[@class="col-lg-4 position-relative"]//select[@name="giorno_nascita"]'
    # Month of Birth
    xpath_month = '//div[@class="col-lg-4 position-relative"]//select[@name="mese_nascita"]'
    # Year of Birth
    xpath_year = '//div[@class="col-lg-4 position-relative"]//select[@name="anno_nascita"]'
    #Privacy checkbox Xpath
    xpath_privacy = '//div[@class="col-lg-4 position-relative"]//input[@id="checkbox_accettazione_2"]'
    #Finalize,submit form button.
    xpath_submit = '//div[@class="col-lg-4 position-relative"]//button[@class="btn btn-primary btn-block"]'

    name=any_list[0]
    gender=any_list[1]
    date_of_birth=any_list[2].split('/')
    day, month, year= date_of_birth[1],date_of_birth[0],date_of_birth[2]
    email=any_list[3]
    # source_url = any_list[4]
    # user_agent = any_list[5]
    # user_ip = any_list[6]
    # new_list=[name,gender,day,month,year,email]

    user_input = [[name, xpath_name], [gender,xpath_gender], [day,xpath_day], [month,xpath_month]
                  , [year,xpath_year], [email,xpath_email]]
    for d,i in enumerate(user_input):
        xpath=i[1]
        input_value = i[0]
        if d == 2 or d ==3 or d == 4:
            coordinates = func(driver,xpath)
            input_value = int(input_value)
            dropdown(driver, coordinates, xpath,input_value=input_value)
        elif d == 0 or d==5:
            coordinates = func(driver,xpath)
            execute_func(coordinates, input_value=input_value)
        elif d==1:
            if input_value=='male':
                coordinates = func(driver, xpath_gender)
                click_only(driver, coordinates, xpath_gender)
                driver.find_element_by_xpath('//div[@class="col-lg-4 position-relative"]//select[@id="inputState"]/option[@value="M"]').click()
                kb.press_and_release('esc')
            elif input_value=='female':
                coordinates = func(driver, xpath_gender)
                click_only(driver, coordinates, xpath_gender)
                driver.find_element_by_xpath('//div[@class="col-lg-4 position-relative"]//select[@id="inputState"]/option[@value="F"]').click()
                kb.press_and_release('esc')
    priv_coord= func(driver,xpath_privacy)
    click_only(driver,priv_coord,xpath_privacy)
    #submit_coord = func(driver, xpath_submit)
    #click_only(driver,submit_coord,xpath_submit)


def diana_1(driver,any_list):
    # Title. Have to click and select gender.
    xpath_gender = '//div[@class="ecco_iner ecco_two"]//select[@name="stato_civile"]'
    #Name Xpath
    xpath_name = '//div[@class="ecco_iner ecco_two"]//label[@for="nome"]'
    #Surname Xpath
    xpath_surname = '//div[@class="ecco_iner ecco_two"]//label[@for="cognome"]'
    #Email Xpath
    xpath_email = '//div[@class="ecco_iner ecco_two"]//label[@for="email"]'
    # Day of Birth
    xpath_day = '//div[@class="ecco_iner ecco_two"]//label[@for="giorno_nascita"]'
    # Month of Birth
    xpath_month = '//div[@class="ecco_iner ecco_two"]//label[@for="mese_nascita"]'
    # Year of Birth
    xpath_year = '//div[@class="ecco_iner ecco_two"]//label[@for="anno_nascita"]'
    #Privacy checkbox Xpath
    xpath_privacy = '//div[@class="ecco_iner ecco_two"]//label[@for="checkbox_accettazione_1"]/input'
    #Finalize,submit form button.
    xpath_submit = '//div[@class="ecco_iner ecco_two"]//a[@id="button-submit-form"]/img'

    name=any_list[0]
    surname=''
    gender=any_list[1]
    date_of_birth=any_list[2].split('/')
    day, month, year= date_of_birth[1],date_of_birth[0],date_of_birth[2]
    email=any_list[3]
    # source_url = any_list[4]
    # user_agent = any_list[5]
    # user_ip = any_list[6]
    # new_list=[name,gender,day,month,year,email]

    user_input = [[name, xpath_name], [gender,xpath_gender], [day,xpath_day], [month,xpath_month]
                  , [year,xpath_year], [email,xpath_email]]
    for d,i in enumerate(user_input):
        xpath=i[1]
        input_value = i[0]
        if d == 2 or d ==3 or d == 4:
            coordinates = func(driver,xpath)
            dropdown(driver, coordinates, xpath,input_value=input_value)
        elif d == 0 or d==5:
            coordinates = func(driver,xpath)
            execute_func(coordinates, input_value=input_value)
        elif d==1:
            if input_value=='male':
                coordinates = func(driver, xpath_gender)
                click_only(driver, coordinates, xpath_gender)
                driver.find_element_by_xpath('//div[@class="ecco_iner ecco_two"]//select[@name="stato_civile"]/option[@value="sig"]').click()
                kb.press_and_release('esc')
            elif input_value=='female':
                coordinates = func(driver, xpath_gender)
                click_only(driver, coordinates, xpath_gender)
                random_title_ele=rd.choice(['sig.ra','sig.na'])
                driver.find_element_by_xpath(f'//div[@class="ecco_iner ecco_two"]//select[@name="stato_civile"]/option[@value="{random_title_ele}"]').click()
                kb.press_and_release('esc')

    priv_coord= func(driver,xpath_privacy)
    click_only(driver,priv_coord,xpath_privacy)
    #submit_coord = func(driver, xpath_submit)
    #click_only(driver,submit_coord,xpath_submit)


def on_time_furute_1(driver,any_list):
    # Title. Have to click and select gender.
    xpath_gender = '//div[@class="shadow border"]//select[@name="sesso"]'
    #Name Xpath
    xpath_name = '//div[@class="shadow border"]//input[@id="nome"]'
    #Surname Xpath
    xpath_surname = '//div[@class="shadow border"]//input[@id="cognome"]'
    #Email Xpath
    xpath_email = '//div[@class="shadow border"]//input[@id="email"]'
    # Day of Birth
    xpath_day = '//div[@class="shadow border"]//select[@name="giorno_nascita"]'
    # Month of Birth
    xpath_month = '//div[@class="shadow border"]//select[@name="mese_nascita"]'
    # Year of Birth
    xpath_year = '//div[@class="shadow border"]//select[@name="anno_nascita"]'
    #Privacy checkbox Xpath
    xpath_privacy = '//div[@class="shadow border"]//input[@id="checkbox_accettazione_2"]'
    #Finalize,submit form button.
    xpath_submit = '//div[@class="shadow border"]//button[@type="submit"]'

    name=any_list[0]
    surname=''
    gender=any_list[1]
    date_of_birth=any_list[2].split('/')
    day, month, year= date_of_birth[1],date_of_birth[0],date_of_birth[2]
    email=any_list[3]
    # source_url = any_list[4]
    # user_agent = any_list[5]
    # user_ip = any_list[6]
    # new_list=[name,gender,day,month,year,email]

    user_input = [[name, xpath_name], [gender,xpath_gender], [day,xpath_day], [month,xpath_month]
                  , [year,xpath_year], [email,xpath_email]]

    for d,i in enumerate(user_input):
        xpath=i[1]
        input_value = i[0]
        if d == 2 or d ==3 or d == 4:
            coordinates = func(driver,xpath)
            dropdown(driver, coordinates, xpath,input_value=input_value)
        elif d == 0 or d==5:
            coordinates = func(driver,xpath)
            execute_func(coordinates, input_value=input_value)
        elif d==1:
            if input_value=='male':
                coordinates = func(driver, xpath_gender)
                click_only(driver,coordinates,xpath_gender)
                driver.find_element_by_xpath('//div[@class="shadow border"]//select[@name="sesso"]/option[@value="M"]').click()
                kb.press_and_release('esc')
            elif input_value=='female':
                coordinates = func(driver, xpath_gender)
                click_only(driver, coordinates, xpath_gender)
                random_title_ele=rd.choice(['sig.ra','F'])
                driver.find_element_by_xpath(f'//div[@class="shadow border"]//select[@name="sesso"]/option[@value="{random_title_ele}"]').click()
                kb.press_and_release('esc')

    priv_coord= func(driver,xpath_privacy)
    click_only(driver,priv_coord,xpath_privacy)
    #submit_coord = func(driver, xpath_submit)
    #click_only(driver,submit_coord,xpath_submit)


def dropdown_v_christin(bot, coordinates, xpath,input_value=''):
    x = coordinates[0]
    y = coordinates[1]
    ms.move(x,y, duration=1)
    sleep(1)
    ms.click()
    sleep(1.7)
    [k for k in xpath.find_elements_by_xpath('.//option') if k.get_attribute('value') == input_value][0].click()
    sleep(2)
    kb.press_and_release('esc')


def christin_usa_1(driver,any_list):
    #Name Xpath
    xpath_name = '//ul[@class="christin"]/li[@_id="35a759d7-d12b-35fb-f468-34dd9cb9c223"][@class="bubble user"]//input'
    #Name submit button Xpath
    xpath_name_submit='//ul[@class="christin"]/li[@_id="35a759d7-d12b-35fb-f468-34dd9cb9c223"][@class="bubble user"]//button'
    #Email Xpath
    xpath_email = '//ul[@class="christin"]/li[@_id="e03e9515-b871-fd8f-09ce-34c67fca8c73"][@class="bubble user"]//input'
    #Email submit button Xpath
    xpath_email_submit='//ul[@class="christin"]/li[@_id="e03e9515-b871-fd8f-09ce-34c67fca8c73"][@class="bubble user"]//button'
    # DATE OF BIRTH
    xpath_date='//ul[@class="christin"]/li[@_id="0483694d-c641-ada5-de58-875c7a5fa019"][@class="bubble user"]/div/select'
    # DATE OF BIRTH SUBMIT BUTTON
    xpath_date_submit='//ul[@class="christin"]/li[@_id="0483694d-c641-ada5-de58-875c7a5fa019"][@class="bubble user"]/div/p/button'
    #Privacy checkbox Xpath
    xpath_privacy = '//ul[@class="christin"]/li[@_id="f8540212-91a3-3d8c-10a0-d4da3c136c40"][@class="bubble user"]/div/p'
    #Privacy submit Xpath
    xpath_privacy_submit='//ul[@class="christin"]/li[@_id="f8540212-91a3-3d8c-10a0-d4da3c136c40"][@class="bubble user"]/div/p/button'
    #Finalize,submit form button. It asks you if you want help from an other peep.
    xpath_submit = '//ul[@class="christin"]/li[@_id="e03e9515-b871-fd8f-09ce-34c67fca8c73"][@class="bubble user"]/div/p'
    #Finalize submit button.
    xpath_submit_submit='//ul[@class="christin"]/li[@_id="e03e9515-b871-fd8f-09ce-34c67fca8c73"][@class="bubble user"]/div/p/button'

    name=any_list[0]
    surname=''
    gender=any_list[1]
    date_of_birth=any_list[2].split('/')
    day, month, year= date_of_birth[1],date_of_birth[0],date_of_birth[2]
    email=any_list[3]
    # source_url = any_list[4]
    # user_agent = any_list[5]
    # user_ip = any_list[6]
    # new_list=[name,gender,day,month,year,email]

    # user_input = [[name, xpath_name], [gender,xpath_gender], [day,xpath_day], [month,xpath_month]
    #               , [year,xpath_year], [email,xpath_email]]

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_name)))
    coordinates = func(driver, xpath_name)
    execute_func(coordinates, input_value=name)
    coordinates = func(driver, xpath_name_submit)
    click_only(driver, coordinates, xpath_name_submit)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_date)))
    birth_elements=driver.find_elements_by_xpath(xpath_date)
    coordinates = func(driver, birth_elements[0], wander=True)
    dropdown_v_christin(driver, coordinates, birth_elements[0], input_value=str(day))
    coordinates = func(driver, birth_elements[1], wander=True)
    dropdown_v_christin(driver, coordinates, birth_elements[1], input_value=str(month))
    coordinates = func(driver, birth_elements[2], wander=True)
    dropdown_v_christin(driver, coordinates, birth_elements[2], input_value=str(year))
    coordinates = func(driver, xpath_date_submit)
    click_only(driver, coordinates, xpath_date_submit)

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath_privacy)))
    privacy_elements=driver.find_elements_by_xpath(xpath_privacy)
    coordinates = func(driver, privacy_elements[1], wander=True)
    click_only(driver, coordinates, privacy_elements[1])
    coordinates = func(driver, xpath_privacy_submit)
    click_only(driver, coordinates, xpath_privacy_submit)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_email)))
    coordinates = func(driver, xpath_email)
    execute_func(coordinates, input_value=email)
    coordinates = func(driver, xpath_email_submit)
    click_only(driver, coordinates, xpath_email_submit)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_submit)))
    submit_elements=driver.find_elements_by_xpath(xpath_submit)
    coordinates = func(driver, submit_elements[1], wander=True)
    click_only(driver, coordinates, submit_elements[1])
    coordinates = func(driver, xpath_submit_submit)
    click_only(driver, coordinates, xpath_submit_submit)


def esmeralda_1(driver,any_list):
    #3card pick. All cards
    xpath_cards='//div[@class="j-card-container"]//img'
    #Title/gender Xpath MALE
    xpath_male='//div[@id="name-step"]//div[@id="gender"]/a[@data-btn="male"]'
    #Title/gender Xpath FEMALE
    xpath_female='//div[@id="name-step"]//div[@id="gender"]/a[@data-btn="female"]'
    #Name Xpath
    xpath_name = '//div[@id="name-step"]//div[@id="first_name_container"]//input'
    #Surname Xpath
    xpath_surname = '//div[@id="name-step"]//div[@id="last_name_container"]//input'
    #Name submit button Xpath
    xpath_name_submit='//div[@id="name-step"]//div[@class="btn btn-primary btn-lg col-xs-12 col-sm-8 col-centered mt20"]'
    #Email Xpath
    xpath_email = '//div[@id="email-step"]//input[@type="email"]'
    # day OF BIRTH
    xpath_day='//div[@id="date-step"]//select[@id="day_select"]'
    #Month of Birth
    xpath_month='//div[@id="date-step"]//select[@id="month_select"]'
    #Year of Birth
    xpath_year='//div[@id="date-step"]//select[@id="year_select"]'
    # DATE OF BIRTH SUBMIT BUTTON
    xpath_date_submit='//div[@id="date-step"]//div[@class="row mt20"]/a'
    #Privacy checkbox Xpath
    xpath_privacy = '//div[@id="email-step"]//input[@type="checkbox"]'
    #Privacy+Email+Finalize submit Xpath
    xpath_privacy_submit='//div[@id="email-step"]//div[@class="btn btn-primary btn-lg col-xs-12 col-sm-8 col-centered mt20"]'


    name=any_list[0]
    surname=''
    gender=any_list[1]
    date_of_birth=any_list[2].split('/')
    day, month, year= date_of_birth[1],date_of_birth[0],date_of_birth[2]
    email=any_list[3]
    # source_url = any_list[4]
    # user_agent = any_list[5]
    # user_ip = any_list[6]
    # new_list=[name,gender,day,month,year,email]

    # user_input = [[name, xpath_name], [gender,xpath_gender], [day,xpath_day], [month,xpath_month]
    #               , [year,xpath_year], [email,xpath_email]]

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_cards)))
    cards=driver.find_elements_by_xpath(xpath_cards)
    pick_a_card_1=rd.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
    coordinates = func(driver, cards[pick_a_card_1], wander=True)
    click_only(driver, coordinates, cards[pick_a_card_1])
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_cards)))
    cards=driver.find_elements_by_xpath(xpath_cards)
    pick_a_card_2=rd.choice([0, 1, 2, 3, 4, 5, 6, 7])
    coordinates = func(driver, cards[pick_a_card_2], wander=True)
    click_only(driver, coordinates, cards[pick_a_card_2])
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_cards)))
    cards=driver.find_elements_by_xpath(xpath_cards)
    pick_a_card_3=rd.choice([0, 1, 2, 3, 4, 5, 6])
    coordinates = func(driver, cards[pick_a_card_3], wander=True)
    click_only(driver, coordinates, cards[pick_a_card_3])

    sleep(2)
    coordinates = func(driver, xpath_month)
    dropdown(driver, coordinates, xpath_month, input_value=month)
    coordinates = func(driver, xpath_day)
    dropdown(driver, coordinates, xpath_day, input_value=day)
    coordinates = func(driver, xpath_year)
    dropdown(driver, coordinates, xpath_year, input_value=year)
    coordinates = func(driver, xpath_date_submit)
    click_only(driver, coordinates, xpath_date_submit)

    sleep(2)
    if gender == 'male':
        coordinates = func(driver, xpath_male)
        click_only(driver, coordinates, xpath_male)
    elif gender == 'female':
        coordinates = func(driver, xpath_female)
        click_only(driver, coordinates, xpath_female)
    coordinates = func(driver, xpath_name)
    execute_func(coordinates, input_value=name)
    coordinates = func(driver, xpath_surname)
    execute_func(coordinates, input_value=name)
    coordinates = func(driver, xpath_name_submit)
    click_only(driver, coordinates, xpath_name_submit)

    sleep(2)
    coordinates = func(driver, xpath_email)
    execute_func(coordinates, input_value=email)
    coordinates = func(driver, xpath_privacy)
    click_only(driver, coordinates, xpath_privacy)
    coordinates = func(driver, xpath_privacy_submit)
    click_only(driver, coordinates, xpath_privacy_submit)
    sleep(2)


def get_config():
    config_file_name = 'config.json'
    with open(config_file_name, 'r') as js_read:
        config_json = json.load(js_read)
    return config_json


def func(bot, xpath='', wander=False):
    browser_navigation_panel_height = bot.execute_script('return window.outerHeight - window.innerHeight;')
    window_height = bot.execute_script("return window.innerHeight")  # 754
    if wander:
        element_location = xpath.rect
    else:
        element_location = bot.find_element_by_xpath(xpath).rect

    y = int(element_location['y'])
    x = int(element_location['x'])

    x_jitter = int(element_location['width']) * (rd.choice(list(range(20, 80))) / 100)
    y_jitter = int(element_location['height']) * (rd.choice(list(range(20, 80))) / 100)
    scroll_count = 0
    while True:
        positive_deltas = [k for k in range(1, 7)]
        negative_deltas = [-k for k in range(1, 7)]
        scroll_bar_position = bot.execute_script("return window.pageYOffset;")  # 300
        screen_y_limit = window_height + scroll_bar_position  # 1054
        if scroll_bar_position < y < screen_y_limit:
            target_y = (y - scroll_bar_position)
            target_y += browser_navigation_panel_height
            return (x + x_jitter, target_y + y_jitter)

        if scroll_bar_position >= y:
            wheel_delta = rd.choice(positive_deltas)

        else:
            wheel_delta = rd.choice(negative_deltas)
        ms.wheel(wheel_delta)  # - sign downside, + sign upside
        sleep(0.5)
        scroll_count += 1

        if scroll_count > 6:
            break


def execute_func(coordinates, input_value=''):
    x = coordinates[0]
    y = coordinates[1]
    ms.move(x,y, duration=1)
    if input_value:
        sleep(0.7)
        ms.click()
        for char in input_value:
            kb.write(char)
            sleep(0.3)


def dropdown(bot, coordinates, xpath,input_value=''):
    print(input_value)
    x = coordinates[0]
    y = coordinates[1]
    ms.move(x,y, duration=1)
    sleep(1)
    ms.click()
    sleep(1.7)
    [k for k in bot.find_element_by_xpath(xpath).find_elements_by_xpath('.//option') if k.get_attribute('value') == input_value][0].click()
    sleep(2)
    kb.press_and_release('esc')


def click_only(bot, coordinates, xpath, input_value=''):
    x = coordinates[0]
    y = coordinates[1]
    ms.move(x, y, duration=1)
    sleep(1)
    ms.click()


def no_click(coordinates, delay=1):
    x = coordinates[0]
    y = coordinates[1]
    ms.move(x, y, duration=1)
    sleep(delay)


def wandering(bot):
    elements_list = []
    a_tags = bot.find_elements_by_tag_name('a')
    span_tags = bot.find_elements_by_tag_name('span')
    div_tags = bot.find_elements_by_tag_name('div')
    for tag_a, tag_span, tag_div in zip(a_tags, span_tags, div_tags):
        elements_list += [tag_a, tag_span, tag_div]
        # elements_list += [tag_a]
    random_interval = [k for k in range(20,80)]
    random_delay = rd.choice(random_interval)/10

    random_interval = [k for k in range(4, 6)]
    random_element_number = rd.choice(random_interval)

    elements_to_wander = rd.choices(elements_list, k=random_element_number)
    if elements_to_wander:
        for i in elements_to_wander:
            try:
                coordinates = func(bot, i, wander=True)
                no_click(coordinates, delay=random_delay)
            except:
                pass
    else:
        return


def times(url, cap):
    total_access = round(cap * 100 / 35)
    print(total_access)
    minutes_amount = 24 * 60
    start = datetime.combine(date.today(), time(0, 0))
    minutes = []
    break_point = 0
    for i in range(minutes_amount):
        minutes.append(start)
        start += timedelta(minutes=1)
        if datetime.combine(date.today(), time(0, 0)) > start:
            break_point = i

    # ## ORIGINAL DISTRIBUTION
    # dist = {
    #     1: 0.04,  # %5 0,085
    #     2: 0.02,  # %2 0,105
    #     3: 0.11,  # %10  0,015
    #     4: 0.125,  # %10 0
    #     5: 0.175,  # %10
    #     6: 0.20,  # %20
    #     7: 0.195,  # %43
    #     8: 0.135  # %10 0,01
    # }

    dist = {
        1: 0,  # %5 0,085
        2: 0,  # %2 0,105
        3: 0,  # %10  0,015
        4: 0,  # %10 0
        5: 1,  # %10
        6: 0,  # %20
        7: 0,  # %43
        8: 0  # %10 0,01
    }


    probs = []
    quarter = 0
    filtered_cum_prob = 0
    for i in range(minutes_amount):
        if i % (minutes_amount / 8) == 0:
            quarter += 1

        cum_prob = dist[quarter]
        if i < break_point:
            filtered_cum_prob += cum_prob / (minutes_amount / 8)
            cum_prob = 0
        x = cum_prob / (minutes_amount / 8)
        probs.append(x)

    remaining_minutes = minutes_amount - break_point
    distributed_cum_prob = filtered_cum_prob / remaining_minutes
    new_probs = list(map(lambda x: x + distributed_cum_prob if x != 0 else 0, probs))

    distributed_time_table = rd.choices(minutes, weights=new_probs, k=total_access)
    time_table = [[i, url] for i in distributed_time_table]

    dist = {
        1: 0.1,  # %5
        2: 0.1,  # %2
        3: 0.1,  # %10
        4: 0.1,  # %10
        5: 0.1,  # %10
        6: 0.1,  # %20
        7: 0.1,  # %43
        8: 0.1,  # %10
        9: 0.1,
        10: 0.1,
    }
    probs = []
    quarter = 0
    for i in range(len(time_table)):
        if i % (round(len(time_table) / 10)) == 0:
            quarter += 1
        cum_prob = dist[quarter]
        x = cum_prob / (minutes_amount / 10)
        probs.append(x)

    distributed_ones = rd.choices(time_table, weights=probs, k=cap)
    new_distributed = []
    for i in time_table:
        if i in distributed_ones:
            i.append(1)
        else:
            i.append(0)
        new_distributed.append(i)

    return new_distributed


def main(user_input, url, task):

    PROXY = 'us.smartproxy.com:10000'  # IP:PORT or HOST:PORT
    user_agent = user_input[5]
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    #options.add_argument('--proxy-server=%s' % PROXY)
    options.add_argument(f"user-agent={user_agent}")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    bot = webdriver.Chrome(options=options)
    bot.get('https://thefutureologist.com/consulting')
    sleep(2)
    target_url = dc[url]
    bot.execute_script(f"javascript: window.location.href = '{target_url}' ")
    sleep(2.5)
    if 'miranda -' not in bot.title.lower() and 'christine' not in bot.title.lower() and 'diana' not in bot.title.lower() and 'come with me and open the door to your future.' not in bot.title.lower() and 'esmeralda' not in bot.title.lower():
        try:
            bot.quit()
        except:
            pass
        raise ConnectionError
    try:
        wandering(bot)
    except:
        pass
    if task == 1:
        try:
            if 'miranda-clairvoyant.com' in url:
                miranda_1(bot, user_input)

            elif 'hosting-dailyhoroscope.com' in url:
                on_time_furute_1(bot, user_input)

            elif 'christin-medium.com' in url:
                christin_usa_1(bot, user_input)

            elif 'diana-psychic.com' in url:
                diana_1(bot, user_input)

            elif 'esmeralda-free-psychic.com' in url:
                esmeralda_1(bot, user_input)
        except Exception as e:
            logging.error('ERROR OCCURED: %s',
                          f"Time: {datetime.now()} >> URL: {url} >> Task: {task} >> Input: {bot_list[bot_list_index]}",
                          exc_info=True)
            try:
                bot.quit()
            except:
                pass
    try:
        bot.quit()
    except:
        pass
    logging.info(
        f'INFO: {datetime.now()} | Task: {task} >> Status: Done >> URL: {url} >> Page Title: {bot.title} >>  Input: {user_input}')


'tmelamed'
'123asdxyz'
if __name__ == '__main__':

    bot_list_file = 'Bot list v1.csv'
    bot_aff_file = 'Bot_afflinks_v1.xlsx'

    bot_list = []
    with open(bot_list_file, 'r', encoding='UTF-8') as rad:
        reader = csv.reader(rad)
        next(reader, None)
        for lines in reader:
            bot_list.append([lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6]])

    bot_aff_list = []
    wb = xlrd.open_workbook(bot_aff_file)
    sheet = wb.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        bot_aff_list.append(
            [sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2), sheet.cell_value(i, 3)])

    dc = {
        'miranda-clairvoyant.com': 'http://leadmining.go2cloud.org/aff_c?offer_id=1261&aff_id=1313&aff_sub=tob1',
        'diana-psychic.com':'http://leadmining.go2cloud.org/aff_c?offer_id=1215&aff_id=1313&aff_sub=tob2',
        'esmeralda-free-psychic.com':'http://leadmining.go2cloud.org/aff_c?offer_id=16&aff_id=1313&aff_sub=tob3',
        'christin-medium.com': 'http://leadmining.go2cloud.org/aff_c?offer_id=619&aff_id=1313&aff_sub=tob4',
        'hosting-dailyhoroscope.com': 'http://leadmining.go2cloud.org/aff_c?offer_id=1362&aff_id=1313&aff_sub=tob5'
            }

    config_file = get_config()
    miranda, hosting, esmeralda, christine, diana = config_file["miranda-clairvoyant.com"], config_file["hosting-dailyhoroscope.com"], config_file["christin-medium.com"],config_file["diana-psychic.com"],config_file["esmeralda-free-psychic.com"]

    if os.path.exists('used_user_inputs.pickle'):
        with open('used_user_inputs.pickle', 'r') as pckle:
            used_users = pickle.load(pickle)
    # Lead sayısının az olması burayı patlatabilir

    gender_names = {'Male':['Mr', 'Man'], 'Female':['Mrs', 'Ms', 'Miss', 'Woman']}
    urls_list = ['miranda-clairvoyant.com', 'hosting-dailyhoroscope.com', 'christin-medium.com', 'diana-psychic.com', 'esmeralda-free-psychic.com']
    caps = {'miranda-clairvoyant.com':miranda, 'diana-psychic.com': diana, 'esmeralda-free-psychic.com':esmeralda, 'christin-medium.com':christine, 'hosting-dailyhoroscope.com':hosting}
    task_list = [times(i, caps[i]) for i in urls_list]
    last_list = []
    for i in task_list:
        last_list += i

    sorted_timetable = sorted(last_list, key=lambda x: x[0])
    rd.shuffle(bot_list)
    bot_list_index = 0
    logging.basicConfig(level=logging.INFO, filename='Affibot log file.log')

    while True:
        now = datetime.now()  # time object
        print("now =", now)
        #true_values = [True for date in sorted_timetable if date[0]+timedelta(minutes=-1) < now < date[0]+timedelta(minutes=1)]
        process_time = ''
        for d, date in enumerate(sorted_timetable):
            if date[0]+timedelta(minutes=-1) < now < date[0]+timedelta(minutes=1):
                process_time = d
                break
        print(sorted_timetable[process_time+1:])
        if process_time:
            #process_time = true_values.index(True)
            error_count = 0
            while True:
                time_value_next, url, task = '[Blank]', '[Blank]', '[Blank]'
                try:
                    time_value_next, url, task = sorted_timetable[process_time + 1]
                    time_value_current, target_url, _  = sorted_timetable[process_time]
                    interval = time_value_next - time_value_current
                    interval_value = interval.seconds
                    main(bot_list[bot_list_index], url, task)
                    print('main finished')
                    sleep(interval_value)
                    process_time += 1
                    if task==1:
                        bot_list_index += 1
                    error_count = 0
                except Exception as ee:
                    logging.error('ERROR OCCURED: %s', f"Time: {datetime.now()} >> URL: {url} >> Task: {task} >> Input: {bot_list[bot_list_index]}", exc_info=True)
                    error_count += 1
                    if error_count > 3:
                        process_time += 1
                        bot_list_index += 1
                    elif error_count > 5:
                        print('Number of trials exceeded 5 thus the script is stopped')
                        quit()

        sleep(0.1)