from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# Comment out any questions that are optional that you don't want to answer
# Your info
firstName = 'First'
lastName = 'Last'
email = 'X@X'
phone = '(XXX) XXX-XXXX'
resumeLocation = ('C://Users//X.xxx')
coverLetterLocation = ('C://Users//X.xxx')

# For the following sections, copy the answer to the question exactly how they would appear on the form
# 2nd section, education
ed1Name = "X"                                       # School Name
ed1Degree = "X"                                     # Degree Earned
ed1Discipline = 'X'                                 # Discipline
ed1StartMo = 'MM'                                   # Month Started
ed1StartY = 'YYYY'                                  # Year Started
ed1EndMo ='MM'                                      # Month Ended
ed1EndY = 'YYYY'                                    # Year Ended

# Can repeat for as many degrees as you want to add
ed2Name = "X"                                       # School Name
ed2Degree = "X"                                     # Degree Earned
ed2Discipline = 'X'                                 # Discipline
ed2StartMo = 'MM'                                   # Month Started
ed2StartY = 'YYYY'                                  # Year Started
ed2EndMo ='MM'                                      # Month Ended
ed2EndY = 'YYYY'                                    # Year Ended

# Questionnaire
ugGPA = '4.0 out of 4.0'                            # Undergraduate GPA
gGPA = 'Not applicable'                             # Graduate GPA
dGPA = 'Not applicable'                             # Doctoral GPA
sAT = 'Did not take'                                # SAT Score
aCT = 'Did not take'                                # ACT Score
gRE = 'Did not take'                                # GRE Score
gMAT = 'Did not take'                               # GMAT Score
spaceXHis = 'I have never worked for SpaceX'        # SpaceX Employment History
spaceXEmailAddress = 'X'                            # SpaceX Email Address
profEx = '0'                                        # Years of professional work experience
basicQual = 'Yes'                                   # Do you meet the basic qualificaitons?
relocate = 'Yes'                                    # Are you within a commutable distance or willing to relocate?
portfolioLocation = ('C://Users//X.xxx')
activeClearance = 'Secret'                          # Active Security Clearance(s)
linkedIn = 'X'                                      # LinkedIn Profile
addLink = 'X'                                       # Any Additional Content
hearAbout = 'Company Website'                       # How did you hear about this job?
pleaseSpecify = 'X'                                 # Please Specify
authWork = 'I am authorized to work in the United States for any employer'  # Are you legally authorized to work in the United States?
citizen = '(a) U.S. citizen or national of the United States'           # Citizenship Status

# US EOEI, optional
gender = 'X'                        # Gender
hisp = 'X'                          # Are you Hispanic/Latino?
race = 'X'                          # Race
vet = 'X'                           # Veteran Status
disability = "X"                    # Disability Status

jobs = [        # List of URLs as strings
    'X',
    'X',
    'X',
    'X'
    ]

driver = webdriver.Chrome()
count = 0
for job in jobs:
    driver.get(job)

    # 1st section, basic info
    driver.find_element_by_id('first_name').send_keys(firstName)
    driver.find_element_by_id('last_name').send_keys(lastName)
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('phone').send_keys(phone)
    driver.find_element_by_link_text('Locate me').click()
    driver.find_element_by_xpath("/html/body/div[3]/form/input[9]").send_keys(resumeLocation)
    driver.find_element_by_xpath("/html/body/div[4]/form/input[9]").send_keys(coverLetterLocation)

    # 2nd section, education
    driver.find_element_by_id('s2id_education_school_name_0').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed1Name)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_id('s2id_education_degree_0').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed1Degree)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_id('s2id_education_discipline_0').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed1Discipline)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[1]').send_keys(ed1StartMo)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[4]/fieldset/input[2]').send_keys(ed1StartY)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[1]').send_keys(ed1EndMo)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[1]/fieldset/div[5]/fieldset/input[2]').send_keys(ed1EndY)

    # Can repeat for as many degrees as you want to add
    driver.find_element_by_id('add_education').click()
    driver.find_element_by_id('s2id_education_school_name_1').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed2Name)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_id('s2id_education_degree_1').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed2Degree)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_id('s2id_education_discipline_1').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(ed2Discipline)
    driver.implicitly_wait(5)
    driver.find_element_by_id('selectedOption').click()
    driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[1]').send_keys(ed2StartMo)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[4]/fieldset/input[2]').send_keys(ed2StartY)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[1]').send_keys(ed2EndMo)
    driver.find_element_by_xpath('//*[@id="education_section"]/div[2]/fieldset/div[5]/fieldset/input[2]').send_keys(ed2EndY)

    # Questionnaire
    Select(driver.find_element_by_xpath("//*[contains(text(), 'GPA (Undergraduate)')]/select")).select_by_visible_text(ugGPA)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'GPA (Graduate)')]/select")).select_by_visible_text(gGPA)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'GPA (Doctorate)')]/select")).select_by_visible_text(dGPA)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'SAT Score')]/select")).select_by_visible_text(sAT)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'ACT Score')]/select")).select_by_visible_text(aCT)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'GRE Score')]/select")).select_by_visible_text(gRE)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'GMAT Score')]/select")).select_by_visible_text(gMAT)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'SpaceX Employment History')]/select")).select_by_visible_text(spaceXHis)
    driver.find_element_by_xpath("//*[contains(text(), 'If applicable, what is / was your SpaceX email address?')]").send_keys(spaceXEmailAddress)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'How many years of professional work experience do you have?')]/select")).select_by_visible_text(profEx)
    try:
        Select(driver.find_element_by_xpath("//*[contains(text(), 'Do you meet all of the Basic Qualifications listed for this job?')]/select")).select_by_visible_text(basicQual)
    except:
        pass
    Select(driver.find_element_by_xpath("//*[contains(text(), 'Are you within a commutable distance or willing to relocate?')]/select")).select_by_visible_text(relocate)
    driver.find_element_by_xpath("/html/body/div[5]/form/input[9]").send_keys(portfolioLocation)
    driver.find_element_by_xpath("//*[contains(text(), 'Active Security Clearance(s)')]").click()
    Select(driver.find_element_by_xpath("//*[contains(text(), 'Active Security Clearance(s)')]/select")).select_by_visible_text(activeClearance)
    driver.find_element_by_xpath("//*[contains(text(), 'LinkedIn Profile')]").send_keys(linkedIn)
    driver.find_element_by_xpath("//*[contains(text(), 'Additional Link')]").send_keys(addLink)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'How did you hear about this job?')]/select")).select_by_visible_text(hearAbout)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'Are you legally authorized to work in the United States?')]/select")).select_by_visible_text(authWork)
    Select(driver.find_element_by_xpath("//*[contains(text(), 'Citizenship Status')]/select")).select_by_visible_text(citizen)

    # US EOEI, optional
    Select(driver.find_element_by_id('job_application_gender')).select_by_visible_text(gender)
    Select(driver.find_element_by_id('job_application_hispanic_ethnicity')).select_by_visible_text(hisp)
    Select(driver.find_element_by_id('job_application_race')).select_by_visible_text(race)
    Select(driver.find_element_by_id('job_application_veteran_status')).select_by_visible_text(vet)
    Select(driver.find_element_by_id('job_application_disability_status')).select_by_visible_text(disability)

    driver.implicitly_wait(5)
    driver.find_element_by_id('submit_app').click()
    count +=1
    driver.implicitly_wait(5)
    driver.close()

print('Done, submitted ', count, ' applications')