from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import os

# Your info
firstName = 'X'
lastName = 'X'
email = 'X@X.com'
phone = '(XXX) XXX-XXXX'
location = 'X, X, X'
resumeLocation = ('C:\\Users\\X.pdf')
bachName = 'X'                          # School Name
bachDegree = 'X'                        # Degree Earned
bachDiscipline = 'X'                    # Discipline
bachStartMo = 'X'                       # Month Started
bachStartY = 'X'                        # Year Started
bachEndMo ='X'                          # Month Ended
bachEndY = 'X'                          # Year Ended
assName = 'X'                           # School Name
assDegree = 'X'                         # Degree Earned
assDiscipline = 'X'                     # Discipline
assStartMo = 'X'                        # Month Started
assStartY = 'X'                         # Year Started
assEndMo ='X'                           # Month Ended
assEndY = 'X'                           # Year Ended


jobs = [    ]   # List of URLs as strings

driver = webdriver.Chrome()
count = 0
for i in jobs:
    driver.get(i)

    # 1st section, basic info
    firstNameBox = driver.find_element_by_id('first_name')
    firstNameBox.send_keys(firstName)
    lastNameBox = driver.find_element_by_id('last_name')
    lastNameBox.send_keys(lastName)
    emailBox = driver.find_element_by_id('email')
    emailBox.send_keys(email)
    phoneBox = driver.find_element_by_id('phone')
    phoneBox.send_keys(phone)
    locationBox = driver.find_element_by_id('job_application_location')
    locationBox.send_keys(location)
    attachResume = driver.find_element_by_xpath("//input[@type='file']")
    attachResume.send_keys(resumeLocation)

    # 2nd section, education
    BS1 = driver.find_element_by_id('s2id_education_school_name_0')
    BS1.click()
    BS1 = driver.find_element_by_xpath("//input[@type='text']")
    BS1.send_keys(bachName)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    BS2 = driver.find_element_by_id('s2id_education_degree_0')
    BS2.click()
    BS2 = driver.find_element_by_xpath("//input[@type='text']")
    BS2.send_keys(bachDegree)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    BS3 = driver.find_element_by_id('s2id_education_discipline_0')
    BS3.click()
    BS3 = driver.find_element_by_xpath("//input[@type='text']")
    BS3.send_keys(bachDiscipline)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    BS4 = driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[1]')
    BS4.send_keys(bachStartMo)
    BS5 = driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[2]')
    BS5.send_keys(bachStartY)
    BS6 = driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[1]')
    BS6.send_keys(bachEndMo)
    BS7 = driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[2]')
    BS7.send_keys(bachEndY)

    # Can repeat for as many degrees as you want to add
    addAnotherEd1 = driver.find_element_by_id('add_education')
    addAnotherEd1.click()
    AS1 = driver.find_element_by_id('s2id_education_school_name_1')
    AS1.click()
    AS1 = driver.find_element_by_xpath("//input[@type='text']")
    AS1.send_keys(assName)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    AS2 = driver.find_element_by_id('s2id_education_degree_1')
    AS2.click()
    AS2 = driver.find_element_by_xpath("//input[@type='text']")
    AS2.send_keys(assDegree)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    AS3 = driver.find_element_by_id('s2id_education_discipline_1')
    AS3.click()
    AS3 = driver.find_element_by_xpath("//input[@type='text']")
    AS3.send_keys(assDiscipline)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    AS4 = driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[1]')
    AS4.send_keys(assStartMo)
    AS5 = driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[2]')
    AS5.send_keys(assStartY)
    AS6 = driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[1]')
    AS6.send_keys(assEndMo)
    AS7 = driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[2]')
    AS7.send_keys(assEndY)

    # Questionnaire
    edConfirm = driver.find_element_by_id('job_application_answers_attributes_0_answer_selected_options_attributes_0_question_option_id')
    edConfirm.click()
    ugGPA = Select(driver.find_element_by_id('job_application_answers_attributes_1_answer_selected_options_attributes_1_question_option_id'))
    ugGPA.select_by_index(X)
    gGPA = Select(driver.find_element_by_id('job_application_answers_attributes_2_answer_selected_options_attributes_2_question_option_id'))
    gGPA.select_by_index(X)
    dGPA = Select(driver.find_element_by_id('job_application_answers_attributes_3_answer_selected_options_attributes_3_question_option_id'))
    dGPA.select_by_index(X)
    SAT = Select(driver.find_element_by_id('job_application_answers_attributes_4_answer_selected_options_attributes_4_question_option_id'))
    SAT.select_by_index(X)
    ACT = Select(driver.find_element_by_id('job_application_answers_attributes_5_answer_selected_options_attributes_5_question_option_id'))
    ACT.select_by_index(X)
    GRE = Select(driver.find_element_by_id('job_application_answers_attributes_6_answer_selected_options_attributes_6_question_option_id'))
    GRE.select_by_index(X)
    GMAT = Select(driver.find_element_by_id('job_application_answers_attributes_7_answer_selected_options_attributes_7_question_option_id'))
    GMAT.select_by_index(X)
    spaceXHis = Select(driver.find_element_by_id('job_application_answers_attributes_8_answer_selected_options_attributes_8_question_option_id'))
    spaceXHis.select_by_index(X)
    profEx = Select(driver.find_element_by_id('job_application_answers_attributes_10_answer_selected_options_attributes_10_question_option_id'))
    profEx.select_by_index(9)
    basicQual = Select(driver.find_element_by_id('job_application_answers_attributes_11_boolean_value'))
    basicQual.select_by_index(X)
    relocate = Select(driver.find_element_by_id('job_application_answers_attributes_12_boolean_value'))
    relocate.select_by_index(X)
    hearAbout = Select(driver.find_element_by_id('job_application_answers_attributes_17_answer_selected_options_attributes_17_question_option_id'))
    hearAbout.select_by_index(X)
    authWork = Select(driver.find_element_by_id('job_application_answers_attributes_19_answer_selected_options_attributes_19_question_option_id'))
    authWork.select_by_index(X)
    citizen = Select(driver.find_element_by_id('job_application_answers_attributes_20_answer_selected_options_attributes_20_question_option_id'))
    citizen.select_by_index(X)

    # US EOEI, optional
    gender = Select(driver.find_element_by_id('job_application_gender'))
    gender.select_by_index(X)
    hisp = Select(driver.find_element_by_id('job_application_hispanic_ethnicity'))
    hisp.select_by_index(X)
    race = Select(driver.find_element_by_id('job_application_race'))
    race.select_by_index(X)
    vet = Select(driver.find_element_by_id('job_application_veteran_status'))
    vet.select_by_index(X)
    disability = Select(driver.find_element_by_id('job_application_disability_status'))
    disability.select_by_index(X)

    driver.implicitly_wait(5)
    submit = driver.find_element_by_id('submit_app')
    submit.click()
    count +=1
    driver.implicitly_wait(5)

print('Done, submitted ', count, ' applications')