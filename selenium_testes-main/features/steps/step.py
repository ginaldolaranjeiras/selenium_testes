from behave import *
from models.tricentis import PageTest

@given('que estou na pagina de formulário')
def step_impl(context):
    pass

# Fill enter vehicle data
@when('eu estou na aba preecha os dados do veículo')
def step_impl(context):
    context.tricentis_test.select_tab(tab_id="entervehicledata")

@when('eu preencho os campos do veículo com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id="make", content="Audi")
    context.tricentis_test.fill_text_by_id(element_id="model", content="Scooter")
    context.tricentis_test.fill_text_by_id(element_id="cylindercapacity", content="150")
    context.tricentis_test.fill_text_by_id(element_id="engineperformance", content="300")
    context.tricentis_test.fill_text_by_id(element_id="dateofmanufacture", content="06/03/2020")
    context.tricentis_test.fill_text_by_id(element_id="numberofseats", content="2")

@when('seleciono a direção direita como não')
def step_impl(context):
    context.tricentis_test.select_option_by_xpath(element_xpath="//*[@id='insurance-form']/div/section[1]/div[7]/p/label[2]")

@when('preencho os outros campos do veículo com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id( element_id="numberofseatsmotorcycle", content="2")
    context.tricentis_test.fill_text_by_id(element_id="fuel", content="Petrol")
    context.tricentis_test.fill_text_by_id(element_id="payload", content="200")
    context.tricentis_test.fill_text_by_id(element_id="totalweight", content="300")
    context.tricentis_test.fill_text_by_id(element_id="listprice", content="1000")
    context.tricentis_test.fill_text_by_id(element_id="licenseplatenumber", content="zzz-9999")
    context.tricentis_test.fill_text_by_id(element_id="annualmileage", content="10000")

@when('clico em próximo na página veículo')
def step_impl(context):
    context.tricentis_test.button_click_by_id(button_id="nextenterinsurantdata")

@then('eu vou para a dados do seguro')
def step_impl(context):
    assert context.failed is False

# Fill enter insurance data
@when('eu estou na aba preecha os dados do seguro')
def step_impl(context):
    context.tricentis_test.select_tab(tab_id="enterinsurantdata")

@when('eu preencho os campos do seguro com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id= "firstname", content= "Alan")
    context.tricentis_test.fill_text_by_id(element_id= "lastname", content= "Garner")
    context.tricentis_test.fill_text_by_id(element_id= "birthdate", content= "03/06/1993")

@when('seleciono o genero como masculino')
def step_impl(context):
    context.tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[4]/p/label[1]")

@when('preencho os outros campos do seguro com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id= "streetaddress", content= "Avenida Brasil")
    context.tricentis_test.fill_text_by_id(element_id= "country", content= "Brasil")
    context.tricentis_test.fill_text_by_id(element_id= "zipcode", content= "37915000")
    context.tricentis_test.fill_text_by_id(element_id= "city", content= "São Paulo")
    context.tricentis_test.fill_text_by_id(element_id= "occupation", content= "Employee")

@when('seleciono dois hobbies')
def step_impl(context):
    context.tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[10]/p/label[1]")
    context.tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[2]/div[10]/p/label[3]")

@when('preencho o campo website com o link')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id= "website", content= "www.google.com")

@when('clico em próximo para página do produto')
def step_impl(context):
    context.tricentis_test.button_click_by_id(button_id= "nextenterproductdata")

@then('eu vou para a aba dados do produto')
def step_impl(context):
    assert context.failed is False

# Fill enter product data
@when('eu estou na aba preecha os dados do produto')
def step_impl(context):
    context.tricentis_test.select_tab(tab_id="enterproductdata")

@when('eu preencho os campos do produto com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id= "startdate", content= "01/01/2021")
    context.tricentis_test.fill_text_by_id(element_id= "insurancesum", content= "2000000")
    context.tricentis_test.fill_text_by_id(element_id= "meritrating", content= "Bonus 3")
    context.tricentis_test.fill_text_by_id(element_id= "damageinsurance", content= "Partial Coverage")

@when('seleciono o produto opicional defesa legal')
def step_impl(context):
    context.tricentis_test.select_option_by_xpath(element_xpath= "//*[@id='insurance-form']/div/section[3]/div[5]/p/label[2]")

@when('preencho o campo de carro reserva como não')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id= "courtesycar", content= "No")

@when('clico em próximo para selecionar opção de preço')
def step_impl(context):
    context.tricentis_test.button_click_by_id(button_id= "nextselectpriceoption")

@then('eu vou para a aba opção de preço')
def step_impl(context):
    assert context.failed is False

#Fiil select price option

@when('eu estou na aba selecione uma opção de preço')
def step_impl(context):
    context.tricentis_test.select_tab(tab_id="selectpriceoption")

@when('eu seleciono uma opção')
def step_impl(context):
    context.tricentis_test.select_option_by_xpath("//*[@id='priceTable']/tfoot/tr/th[2]/label[2]")

@when('clico em próximo para a aba enviar cotação')
def step_impl(context):
    context.tricentis_test.button_click_by_id(button_id= "nextsendquote")

@then('eu vou para a aba enviar cotação')
def step_impl(context):
    assert context.failed is False

# Fill send code
@when('eu estou na aba para eviar cotação')
def step_impl(context):
    context.tricentis_test.select_tab(tab_id="sendquote")

@when('eu prencho os campos da cotação com os valores')
def step_impl(context):
    context.tricentis_test.fill_text_by_id(element_id="email", content="ginaldolaranjeiras@gmail.com")
    context.tricentis_test.fill_text_by_id(element_id="phone", content="5579991147935")
    context.tricentis_test.fill_text_by_id(element_id="username", content="alan_garner")
    context.tricentis_test.fill_text_by_id(element_id="password", content="abC123")
    context.tricentis_test.fill_text_by_id(element_id="confirmpassword", content="abC123")
    context.tricentis_test.fill_text_by_id(element_id="Comments", content="It's a hard form!")

@when('clico no botão enviar cotação')
def step_impl(context):
    context.tricentis_test.button_click_by_id("sendemail")
    context.tricentis_test.delay_timer(10)

@then('eu recebo a mensagem de sucesso')
def step_impl(context):
    assert context.failed is False
    
