from selenium import webdriver
import time


cats = ['Offense', 'Defense', 'Special Teams']

o_pos_list = ['QB', 'RB', 'WR', 'FB', 'TE', 'T', 'G', 'C']
d_pos_list = ['DE', 'DT', 'ILB', 'OLB', 'CB', 'SS', 'FS']
st_pos_list = ['K', 'LS', 'P', 'RS', 'ST']

pos_dict = {'Offense': o_pos_list, 'Defense': d_pos_list, 'Special Teams': st_pos_list}

options = webdriver.ChromeOptions()
# change these 2 line to load your chrome profile and location of the chrome app
# this is important because you must be logged into nfl.com
options.add_argument("user-data-dir=/Users/caseyfinnicum/Library/Application Support/Google/Chrome/")
chrome_driver_binary = "/Users/caseyfinnicum/Desktop/python_projects/nfl_pro_bowl_vote/chromedriver"

driver = webdriver.Chrome(options=options)

# base url will bring to the QB section within the offense category
driver.get('https://www.nfl.com/pro-bowl/ballot/')

# pause for 2 seconds to load the page
time.sleep(2)


def voteforposition():
    # find all of the elements in the html that match the raiders logo
    elem_list = driver.find_elements_by_xpath(
        "//img[contains(@src,'https://imagecomposer.nfl.com/image/fetch/q_80,h_216,w_264,"
        "c_fill/https://static.www.nfl.com/image/private/f_auto,q_auto/league/y2saimpyifuahldhzetn')]")
    print('player found!')

    for elem in elem_list:
        driver.execute_script("arguments[0].click();", elem)


def switchPagesVote(pos_dict_in):
    for category, pos_list in pos_dict_in.items():
        # select the category, first should be offense
        driver.find_element_by_xpath("//div[text()='" + category + "']").click()

        for pos in pos_list:
            # switch to the pos of interest
            driver.find_element_by_xpath("//div[text()='" + pos + "']").click()
            # pause for 2 seconds after reaching the page
            time.sleep(2)
            # vote for the raiders!
            voteforposition()
            # pause for 1 second after voting before switching pages
            time.sleep(1)

        # wait 1 second after completing the category
        time.sleep(1)

    # review the selections
    driver.find_element_by_xpath("//div[text()='Review Selections']").click()
    # Wait 2 seconds before trying to submit
    time.sleep(2)
    # submit the selections
    driver.find_element_by_xpath("//div[text()='Submit']").click()
    # close the browser
    time.sleep(2)
    driver.close()


switchPagesVote(pos_dict)

