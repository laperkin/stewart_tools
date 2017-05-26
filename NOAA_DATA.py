from bs4 import BeautifulSoup
import requests
import pdfkit
from geopy.geocoders import Nominatim

address = input('Type Address')
geolocator = Nominatim()
location = geolocator.geocode(address)

lat = location.latitude
lon = location.longitude

print(lat, lon)

url = "http://hdsc.nws.noaa.gov/hdsc/pfds/pfds_printpage.html?lat={}&lon={}&data=depth&units=english&series=pds".format(lat,lon)
headers = {'User-Agent':'Mozilla/5.0'}

print(url)

###pdfkit.from_url(url,'out.pdf')
