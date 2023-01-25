import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import has12_data_config as mc
import smtplib
from email.message import EmailMessage

driver = webdriver.Firefox()

wait = WebDriverWait(driver, 10)

driver.get(mc.url)
my_identification = input("identification number:")

id_elem = wait.until(EC.element_to_be_clickable((By.NAME, "id")))
pass_elem = driver.find_element(By.CSS_SELECTOR, "input[name='pw']")
iden_elem = driver.find_element(By.CSS_SELECTOR, "input[name='user_code']")
id_elem.send_keys(mc.my_id)
pass_elem.send_keys(mc.my_pw)
iden_elem.send_keys(my_identification)
login_elem = driver.find_element(By.CSS_SELECTOR, "input[type='image']")
login_elem.click()


agree_first_elem = wait.until(EC.element_to_be_clickable((By.ID, "agr1_y")))
agree_second_elem = driver.find_element(By.CSS_SELECTOR, "input[id='agr2_y']")
agree_first_elem.click()
agree_second_elem.click()
agree_ok_elem = driver.find_element(By.CSS_SELECTOR, "input[type='button']")
agree_ok_elem.click()


take_class_elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='../student/consent.php']")))
take_class_elem.click()




while True :
    driver.refresh()
    table_elem = wait.until((EC.element_to_be_clickable((By.CSS_SELECTOR, "table[width='100%'][cellspacing='0'][cellpadding='0']"))))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    tennis_elem = soup.select("font[color='red']")
    if(tennis_elem[26].text != '마감'):
        print('수강신청 요망')
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login('your gmail account', 'your gmail account app password')#구글 앱 비밀번호 발급 검색 후 따라하고 앱 비밀번호 복붙
        msg = EmailMessage()
        msg['Subject'] = "수강신청 가능"
        msg.set_content("현재 설정한 수강과목이 신청 가능한 상태입니다.")
        msg['From'] = 'your gmail address'
        msg['To'] = 'your any email address'
        smtp.send_message(msg)
    time.sleep(1)
