""""
    Stock Utility -- will grab current price of share from a specified company and will send you email updates
    regarding price changes
"""

import requests
import smtplib
import sys
import tkinter as tk
from tkinter import messagebox

# Constants
HOST_EMAIL = ""
HOST_PASS = ""
RECIPIENT_EMAIL = ""
RECIPIENT_PASS = ""


class Request(object):

    def __init__(self, name):
        self.name = name
        self.price = ""

    def set_name(self, name):
        self.name = name
        self.grab_info()

    # if the search query does not exist, page.find() will return -1, which means that we shouldn't try to search
    def page_found(self, page_content, unknown_search):
        return page_content.find(unknown_search)

    # method that will actually scrape the chosen company's stock price
    def grab_info(self):
        # variables/deliverables
        comp_name = self.name
        url = "http://search.nasdaq.com/search?q="
        unknown_search = 'HTTP 404. The page you requested could not be found.'
        price_query = '<div id="qwidget_lastsale" class="qwidget-dollar">'
        title_query = 'var followObjTitle = "'
        delim_start = "http://www.nasdaq.com/symbol/"

        destination = requests.get(url + comp_name)
        content = destination.text

        start_index = (content.find(delim_start) + len(delim_start))
        end_index = content.find("<", start_index)

        abbreviation = (content[start_index:end_index])
        stock_page = delim_start + abbreviation
        page_goal = requests.get(stock_page)
        page = page_goal.text

        # end the program if the requested search does not exist
        if self.page_found(page, unknown_search) != -1:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(title="Error", message="Sorry, the requested company wasn't "
                                                        "found in the NASDAQ database. Please try redefining your search.")
            self.price = "Company not found"
            sys.exit()


        new_start_index = page.find(price_query) + len(price_query)
        new_end_index = page.find("</div>", new_start_index)

        new_title_start_index = page.find(title_query) + len(title_query)
        new_title_end_index = page.find('"', new_title_start_index)

        name = page[new_title_start_index:new_title_end_index]

        share_price = page[new_start_index:new_end_index]

        # calls the function that will send email alerts
        self.send_email(str(comp_name), str(share_price))
        self.price = share_price

    # any time that the price of a stock changes by more than 1%, an automated email will be sent to the user.
    def send_email(self, company, price):
        body = "Price of {} shares has updated. Price is now {}".format(company, price)

        msg = """Subject: %s\n
                   %s""" % (company, body)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(HOST_EMAIL, HOST_PASS)
        server.sendmail(RECIPIENT_EMAIL, RECIPIENT_PASS, msg)
        server.quit()





