import argparse,time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
 
parser = argparse.ArgumentParser(description='Reciosbot Will Spam your site introducing funny user agent in logs')
parser.add_argument('--url', type=str, nargs='?', help='URL to be called')
parser.add_argument('--user_agent', nargs='?', help='Funny user agent to be used',default='ReciosBot/Doing_My_Part')
parser.add_argument('--requests', type=int, nargs='?', help='Number of requests to be done', default=5)
parser.add_argument('--interval', type=float, nargs='?', help='Interval in miliseconds between requests', default=0.5)
inputArgs = parser.parse_args()

# Some info about runtime
print("#############################################")
print(" RECIOSBOT: Navahasos en er pesho since 2021 ")
print("By Sergio 'EverythingForATeamMate' Fernandez")
print("#############################################")
print("- Selected URL is "+inputArgs.url)
print("- UserAgent "+ inputArgs.user_agent + " will be used.")
print("- A number of "+ str(inputArgs.requests) + " requests will be done, with a " + str(inputArgs.interval) + " seconds between requests")
print("#############################################")

# This function makes the magic
def call_shit(url, user_agent):
    # Virtual display and so
    display = Display(visible=0, size=(800, 600))
    display.start()
    # UserAgent magic
    options=Options()
    options.set_preference("general.useragent.override", user_agent)
    # Run the headless browser
    driver = Firefox(options=options)
    driver.get(inputArgs.url)
    driver.quit()
    # Obviously, stop the virtual display
    display.stop()

def main():
    count = 1
    while count <= inputArgs.requests:
        print("==> Request number " + str(count) + " of " + str(inputArgs.requests))
        call_shit(inputArgs.url,inputArgs.user_agent)
        time.sleep(inputArgs.interval)
        count += 1
    print("############################################")
    print("##           PUES YA ESTARÍA              ##")
    print("############################################")

main()
