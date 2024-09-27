import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 확장 프로그램 폴더 경로 설정
extension_folder = r'C:\Users\Owner\AppData\Local\Google\Chrome\User Data\Default\Extensions\mpbjkejclgfgadiemmefgebjfooflfhl\3.1.0_0'

# Chrome 옵션 설정
chrome_options = webdriver.ChromeOptions()

# 확장 프로그램 폴더 로드
chrome_options.add_argument(f'--load-extension={extension_folder}')

# WebDriver 실행
driver = webdriver.Chrome(options=chrome_options)

# 확장 프로그램 및 Chrome Driver 세팅 완료

def bypass_recaptcha(url):
    driver.get(url)
    #bypass_recaptcha 함수 호출하며 전달된 url 값을 get으로 chrome driver에 로드

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
    #chrome driver에서 reCAPTCHA iframe 확인 후 해당 iframe으로 switch

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']/div[@class='recaptcha-checkbox-border']"))).click()
    #체크박스 클릭 가능할때까지 최대 10초까지 대기 한 후 체크박스 클릭

    driver.switch_to.default_content()
    #클릭 후 원래 iframe 밖의 요소로 switch

    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge expires in two minutes']")))
    #다시 그림 인증 캡챠 iframe으로 switch

    while True:
    #Burst:Captcha Solver for Humans 인증 실패했을때를 대비해 반복적인 클릭을 위해 무한반복문 사용
        try:
            WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='button-holder help-button-holder']"))).click()
            #captcha 퍼즐 자동 풀이 버튼 클릭
        except selenium.common.exceptions.StaleElementReferenceException:
            #만약 StaleElementReferenceException에러 즉, 찾을 수 없다면
            pass
            #이미 클릭 중인 상태인 것이니 pass
        except selenium.common.exceptions.ElementClickInterceptedException:
            #만약 ElementClickInterceptedException에러 즉, 모종의 이유로 클릭할 수 없는 상태라면 해당 iframe이 비활성화 된 것이니 체크 완료된 것.
            print("bypassed")
            break
            #그러므로 reCAPTCHA 퍼즐인증이 수행완료됐고, 완료 됐으니 무한반복문 탈출

def __main__():
    url = 'https://patrickhlauke.github.io/recaptcha/'
    bypass_recaptcha(url)

__main__()
