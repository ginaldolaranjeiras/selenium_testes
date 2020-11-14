import behave
from models.tricentis import PageTest

def before_all(context):
    # Test instance
    context.tricentis_test = PageTest(driver_path=r'chromedriver.exe', url=r'http://sampleapp.tricentis.com/101/app.php')
    #open browser
    context.tricentis_test.open_browser()

def after_all(context):
    context.tricentis_test.delay_timer(20)
    context.tricentis_test.quit_test()
