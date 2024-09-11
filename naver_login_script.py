from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyperclip
import time

browser = webdriver.Chrome()

user_id = 'test_id' # 실제로는 본인 id 사용
user_pw = 'test_pw' # 실제로는 본인 pw 사용

# 1. 네이버 이동
browser.get('http://naver.com')

# 2. 로그인 버튼 클릭 (CSS Selector 사용)
elem = browser.find_element(By.CSS_SELECTOR, '.MyView-module__link_login___HpHMW')
elem.click()

# 3. ID 복사 붙여넣기
elem_id = browser.find_element(By.ID, 'id')
elem_id.click()
pyperclip.copy(user_id)  # pyperclip 모듈을 사용하여 ID 복사
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 4. PW 복사 붙여넣기
elem_pw = browser.find_element(By.ID, 'pw')
elem_pw.click()
pyperclip.copy(user_pw)  # pyperclip 모듈을 사용하여 PW 복사
elem_pw.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 5. 로그인 버튼 클릭
browser.find_element(By.ID, 'log.login').click()

# 페이지 로드가 완료될 때까지 대기 (5초 대기)
time.sleep(5)

# 6. "등록" 버튼 클릭
browser.find_element(By.ID, 'new.save').click() 

# 무한 대기 (명시적으로 종료하기 전까지 창 유지)
while True:
    pass  # 스크립트가 계속 실행 중인 상태로 유지, 종료는 Ctrl + C 수동으로 입력


