from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Caminho para o webdriver na máquina
PATH = 'webdriverchrome\chromedriver'

# Objeto de teste - aplicação web
URL = 'http://sampleapp.tricentis.com/101/app.php'

# Run webdriver
driver = webdriver.Chrome(PATH)
driver.get(URL)

# Fill vehicle data
make = driver.find_element_by_id("make")
make.click()
make.send_keys("Audi")
make.send_keys(Keys.RETURN)

model = driver.find_element_by_id("model")
model.click()
model.send_keys("Scooter")
model.send_keys(Keys.RETURN)

cylinder_capacity = driver.find_element_by_id("cylindercapacity")
cylinder_capacity.send_keys('150')
cylinder_capacity.send_keys(Keys.RETURN)

engine_performance = driver.find_element_by_id("engineperformance")
engine_performance.send_keys('300')
engine_performance.send_keys(Keys.RETURN)

date_of_manufacture = driver.find_element_by_id("dateofmanufacture")
date_of_manufacture.click()
date_of_manufacture.send_keys('06/03/2020')
date_of_manufacture.send_keys(Keys.RETURN)

number_of_seats = driver.find_element_by_id("numberofseats")
number_of_seats.click()
number_of_seats.send_keys("2")
number_of_seats.send_keys(Keys.RETURN)

right_hand_drive = driver.find_element_by_xpath("//*[@id='insurance-form']/div/section[1]/div[7]/p/label[2]")
right_hand_drive.click()
right_hand_drive.send_keys(Keys.RETURN)

number_of_seats_motorcycle = driver.find_element_by_id("numberofseatsmotorcycle")
number_of_seats_motorcycle.click()
number_of_seats_motorcycle.send_keys("2")
number_of_seats_motorcycle.send_keys(Keys.RETURN)

fuel = driver.find_element_by_id("fuel")
fuel.click()
fuel.send_keys("Petrol")
fuel.send_keys(Keys.RETURN)

payload = driver.find_element_by_id("payload")
payload.send_keys('200')
payload.send_keys(Keys.RETURN)

total_weight = driver.find_element_by_id("totalweight")
total_weight.send_keys('300')
total_weight.send_keys(Keys.RETURN)

list_price = driver.find_element_by_id("listprice")
list_price.send_keys('1000')
list_price.send_keys(Keys.RETURN)

license_plate_number = driver.find_element_by_id("licenseplatenumber")
license_plate_number.send_keys('ZZZ-9999')
license_plate_number.send_keys(Keys.RETURN)

annual_mileage = driver.find_element_by_id("annualmileage")
annual_mileage.send_keys('10000')
annual_mileage.send_keys(Keys.RETURN)

next_button_insurant = driver.find_element_by_id("nextenterinsurantdata")
next_button_insurant.click()

# Fill insurance data
first_name = driver.find_element_by_id("firstname")
first_name.send_keys('Alan')
first_name.send_keys(Keys.RETURN)

last_name = driver.find_element_by_id("lastname")
last_name.send_keys('Garner')
last_name.send_keys(Keys.RETURN)

birth_date = driver.find_element_by_id("birthdate")
birth_date.click()
birth_date.send_keys('06/03/1983')
birth_date.send_keys(Keys.RETURN)


gender = driver.find_element_by_xpath("//*[@id='insurance-form']/div/section[2]/div[4]/p/label[1]")
gender.click()
gender.send_keys(Keys.RETURN)

street_address = driver.find_element_by_id("streetaddress")
street_address.send_keys('Avenida Brasil')
street_address.send_keys(Keys.RETURN)

country = driver.find_element_by_id("country")
country.click()
country.send_keys("Brazil")
country.send_keys(Keys.RETURN)

zipcode = driver.find_element_by_id("zipcode")
zipcode.send_keys('49900000')
zipcode.send_keys(Keys.RETURN)

city = driver.find_element_by_id("city")
city.send_keys('São Paulo')
city.send_keys(Keys.RETURN)

occupation = driver.find_element_by_id("occupation")
occupation.click()
occupation.send_keys("Employee")

hobbie1 = driver.find_element_by_xpath("//*[@id='insurance-form']/div/section[2]/div[10]/p/label[1]")
hobbie1.click()
hobbie1.send_keys(Keys.RETURN)
hobbie2 = driver.find_element_by_xpath("//*[@id='insurance-form']/div/section[2]/div[10]/p/label[3]")
hobbie2.click()
hobbie2.send_keys(Keys.RETURN)

website = driver.find_element_by_id("website")
website.send_keys("www.google.com")
website.send_keys(Keys.RETURN)

next_button_product = driver.find_element_by_id("nextenterproductdata")
next_button_product.click()

# Fill product data
start_date = driver.find_element_by_id("startdate")
start_date.click()
start_date.send_keys('01/01/2021')
start_date.send_keys(Keys.RETURN)

insurance_sum = driver.find_element_by_id("insurancesum")
insurance_sum.click()
insurance_sum.send_keys("2000000")
insurance_sum.send_keys(Keys.RETURN)

merit_rating = driver.find_element_by_id("meritrating")
merit_rating.click()
merit_rating.send_keys("Bonus 3")
merit_rating.send_keys(Keys.RETURN)

damage_insurance = driver.find_element_by_id("damageinsurance")
damage_insurance.click()
damage_insurance.send_keys("Partial Coverage")
damage_insurance.send_keys(Keys.RETURN)


optional_products = driver.find_element_by_xpath("//*[@id='insurance-form']/div/section[3]/div[5]/p/label[2]")
optional_products.click()
optional_products.send_keys(Keys.RETURN)

courtesy_car = driver.find_element_by_id("courtesycar")
courtesy_car.click()
courtesy_car.send_keys("No")
courtesy_car.send_keys(Keys.RETURN)

next_button_select_price = driver.find_element_by_id("nextselectpriceoption")
next_button_select_price.click()

# fill select price option
prince_option = driver.find_element_by_xpath("//*[@id='priceTable']/tfoot/tr/th[2]/label[2]")
prince_option.click()
prince_option.send_keys(Keys.RETURN)

next_button_send_quote = driver.find_element_by_id("nextsendquote")
next_button_send_quote.click()

# fill send quote
email = driver.find_element_by_id("email")
email.click()
email.send_keys("ginaldolaranjeiras@gmail.com")
email.send_keys(Keys.RETURN)

phone = driver.find_element_by_id("phone")
phone.click()
phone.send_keys("5579991147935")
phone.send_keys(Keys.RETURN)

username = driver.find_element_by_id("username")
username.click()
username.send_keys("alan_garner")
username.send_keys(Keys.RETURN)

password = driver.find_element_by_id("password")
password.click()
password.send_keys("abC123")
password.send_keys(Keys.RETURN)

confirm_password = driver.find_element_by_id("confirmpassword")
confirm_password.click()
confirm_password.send_keys("abC123")
confirm_password.send_keys(Keys.RETURN)


next_button_send_email = driver.find_element_by_id("sendemail")
next_button_send_email.click()


time.sleep(30)

driver.quit()
