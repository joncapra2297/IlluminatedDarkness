# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

 To maintain the concept of an unverifiable afterlife, the church’s
 policing mechanisms lay out a system of supernatural monitoring and
 punishment. Using a system of beliefs and values, the Catholic Church
 prescribes certain moral norms and their transgressions. Sustaining
 the rationality of an uncertain system that lacks scientific credibility,
 the functionaries of the church become a “watching eye,” an arbiter of
 pro-social behavior in modern-day American society.

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Illuminated Darkness',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        #The user sees an image of the sun in a hazy sky over apple trees.

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('thealmighty.jpg',m.get_attribute('src'))

        a=self.browser.find_element_by_id('thesun')
        a.click()

        self.assertIn('Newpage',self.browser.title)

        h=self.browser.find_element_by_tag_name('h1')

        #the user goes back to the home page
        self.browser.back()

        # the user sees at the bottom of the page a link to credits
        l=self.browser.find_element_by_link_text('Credits')

        # the user clicks on the credits link
        l.click()

        # and sees the credits.html page
        a=self.browser.current_url
        self.assertIn("credits.html",a)



if __name__=="__main__":
        unittest.main(warnings="ignore")
