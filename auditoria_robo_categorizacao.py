#versao 1.0 robo auditoria qualidesk 
#integracao com o robo de auditoria
#inicio 02.02.20

#imports necessarios
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec

#acesso ao robo
driver = webdriver.Chrome()
driver.get("https://qualidesk.qualicorp.com.br/itop2/pages/UI.php")

#LOGIN DE ACESSO
user = driver.find_element_by_xpath("""//*[@id="user"]""")
user.send_keys("login_")
pwd = driver.find_element_by_xpath("""//*[@id="pwd"]""")
pwd.send_keys("senha_")
enter_button = driver.find_element_by_xpath("""//*[@id="login"]/form/table/tbody/tr[3]/td/span/input""").click()



#ACESSO A FILA DE CHAMADOS  
driver.find_element_by_xpath("""//*[@id="AccordionMenu_MyShortcuts_250"]/a""").click()

rqs = int (driver.find_element_by_xpath("""//*[@id="total"]""").text)
request = int(rqs)
i = 1
while (i <= request):
    receive =  driver.find_element_by_xpath ("//*[@id='datatable_shortcut_250']/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[" + str(i) + "]")
    i += 1
    print (receive.text)

