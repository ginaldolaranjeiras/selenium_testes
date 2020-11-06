from models.tricentis import PageTest

# Webdriver route
PATH = r'selenium_testes\webdriverchrome\chromedriver.exe'

# Test object
URL = r'http://sampleapp.tricentis.com/101/app.php'

# Test instance
tricentis_test = PageTest(driver_path=PATH, url=URL)

tricentis_test.open_browser()

# Fill enter vehicle data
tricentis_test.select_tab(tab_id="entervehicledata")
tricentis_test.fill_text_by_id(element_id="make", content="Audi")
tricentis_test.fill_text_by_id(element_id="model", content="Scooter")
tricentis_test.fill_text_by_id(element_id="cylindercapacity", content="150")
tricentis_test.fill_text_by_id(element_id="engineperformance", content="300")
tricentis_test.fill_text_by_id(element_id="dateofmanufacture", content="06/03/2020")
tricentis_test.fill_text_by_id(element_id="numberofseats", content="2")
tricentis_test.select_option_by_xpath(element_xpath="//*[@id='insurance-form']/div/section[1]/div[7]/p/label[2]")
tricentis_test.fill_text_by_id(element_id="numberofseatsmotorcycle", content="2")
tricentis_test.fill_text_by_id(element_id="fuel", content="Petrol")
tricentis_test.fill_text_by_id(element_id="payload", content="200")
tricentis_test.fill_text_by_id(element_id="totalweight", content="300")
tricentis_test.fill_text_by_id(element_id="listprice", content="1000")
tricentis_test.fill_text_by_id(element_id="licenseplatenumber", content="zzz-9999")
tricentis_test.fill_text_by_id(element_id="annualmileage", content="10000")
tricentis_test.button_click_by_id(button_id="nextenterinsurantdata")


# Fill enter insurance data
tricentis_test.select_tab(tab_id="enterinsurantdata")
tricentis_test.fill_text_by_id(element_id= "firstname", content= "Alan")
tricentis_test.fill_text_by_id(element_id= "lastname", content= "Garner")
tricentis_test.fill_text_by_id(element_id= "birthdate", content= "03/06/1993")
tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[4]/p/label[1]")
tricentis_test.fill_text_by_id(element_id= "streetaddress", content= "Avenida Brasil")
tricentis_test.fill_text_by_id(element_id= "country", content= "Brasil")
tricentis_test.fill_text_by_id(element_id= "zipcode", content= "37915000")
tricentis_test.fill_text_by_id(element_id= "city", content= "São Paulo")
tricentis_test.fill_text_by_id(element_id= "occupation", content= "Employee")
tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[10]/p/label[1]")
tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[10]/p/label[3]")
tricentis_test.fill_text_by_id(element_id= "website", content= "www.google.com")
tricentis_test.button_click_by_id(button_id= "nextenterproductdata")


# Fill enter product data
tricentis_test.select_tab("enterproductdata")
tricentis_test.fill_text_by_id(element_id= "startdate", content= "01/01/2021")
tricentis_test.fill_text_by_id(element_id= "insurancesum", content= "2000000")
tricentis_test.fill_text_by_id(element_id= "meritrating", content= "Bonus 3")
tricentis_test.fill_text_by_id(element_id= "damageinsurance", content= "Partial Coverage")
tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[3]/div[5]/p/label[2]")
tricentis_test.fill_text_by_id(element_id= "courtesycar", content= "No")
tricentis_test.button_click_by_id(button_id= "nextselectpriceoption")

# Fill select price option
tricentis_test.select_tab("selectpriceoption")
tricentis_test.select_option_by_xpath("//*[@id='priceTable']/tfoot/tr/th[2]/label[2]")
tricentis_test.button_click_by_id("nextsendquote")

# Fill send code
tricentis_test.select_tab("sendquote")
tricentis_test.fill_text_by_id(element_id="email", content="ginaldolaranjeiras@gmail.com")
tricentis_test.fill_text_by_id(element_id="phone", content="5579991147935")
tricentis_test.fill_text_by_id(element_id="username", content="alan_garner")
tricentis_test.fill_text_by_id(element_id="password", content="abC123")
tricentis_test.fill_text_by_id(element_id="confirmpassword", content="abC123")
tricentis_test.fill_text_by_id(element_id="Comments", content="It's a hard form!")
tricentis_test.button_click_by_id("sendemail")

# Await
tricentis_test.delay_timer(10)

# Close test
tricentis_test.quit_test()
