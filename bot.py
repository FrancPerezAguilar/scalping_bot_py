from selenium import webdriver

PATH = "./chromedriver"

driver = webdriver.Chrome(PATH)

# PcComponentes test website
driver.get(
    "https://www.pccomponentes.com/hp-pavilion-gaming-16-a0010ns-intel-core-i7-10750h-16gb-512gb-ssd-gtx-1650ti-161"
)

exists = False

while not exists:

    try:
        buttonToClick = driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/div[4]/div[3]/div/div[1]/div/button[3]"
        )

        print("No esta disponible para comprar")

        time.sleep(1)
        driver.refresh()

    except:
        buttonToClick = driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/div[4]/div[3]/div/div[1]/div/button[3]"
        )
        print("Vamos a comprar!")
        buttonToClick.click()
        exists = True


# End of execution
# driver.quit()