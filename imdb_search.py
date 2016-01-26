from bs4 import BeautifulSoup
import urllib2
import imdb
import urllib
import requests
import cookielib
import mechanize

def login(personID):

    cookiejar = cookielib.LWPCookieJar() 
    br = mechanize.Browser()
    br.set_cookiejar( cookiejar ) 

    # Browser options 
    br.set_handle_equiv(True) 
    br.set_handle_gzip(True) 
    br.set_handle_redirect(True) 
    br.set_handle_referer(True) 
    br.set_handle_robots(False) 

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)

    br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Firefox/3.0.1' ) ] 

    # authenticate 
    br.open("https://pro-labs.imdb.com/login") 
    formcount=0
    for frm in br.forms():  
      if str(frm.attrs["class"])=="styled_form":
        break
      formcount=formcount+1
    br.select_form(nr=formcount)
    print "formcount",formcount


    # these two come from the code you posted
    # where you would normally put in your username and password
    br["emailAddress"] = '<USERNAME>'
    br["password"] = '<PASSWORD>'
    response = br.submit()


def search_person(person):
    imdb_access = imdb.IMDb()
    result = imdb_access.search_person(person)
    personID = result[0].personID

    convert_url_text(str(personID))

def convert_url_text(personID):
    url = br.open("https://pro-labs.imdb.com/name/nm"+personID+"/?ref_=sch_int") 
    returnPage = url.read() 

    search_page(returnPage)


def search_page(page):

    soup = BeautifulSoup(page, 'html.parser')

    headers = soup.find_all("li", class_="header ellipsis")
    for header in headers:
        name = header.findNextSibling()
        print header.getText()
        print name.getText()


# search_person("Cat Alter")