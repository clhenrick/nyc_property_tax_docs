from sys import argv
import csv
import requests
import bs4
import time
import random

url = "http://nycprop.nyc.gov/nycproperty/nynav/jsp/selectbbl.jsp"
headers = {'User-Agent' : 'Mozilla/5.0'}

data = {
    'FFUNC': 'C',
    'q49_boro': '1',
    'q49_block_id': '01221',
    'q49_lot': '0007',
    'q49_prp_ad_street_no': '109',    
    'q49_prp_nm_street': 'WEST 90 STREET',                   
    'q49_prp_id_apt_num': '',     
    'q49_prp_ad_city': 'New york',            
    'q49_prp_cd_state': 'NY',
    'q49_prp_cd_addr_zip': '10024',
    'bblAcctKeyIn1': '1',
    'bblAcctKeyIn2': '01221',
    'bblAcctKeyIn3': '0007',
    'bblAcctKeyIn4': '',
    'ownerName': 'NYC HOUSING AUTHORITY',
    'ownerName1': 'NYC HOUSING AUTHORITY',                                                 
    'ownerName2': '',                                                                     
    'ownerName3': '',                                                                     
    'ownerName4': '',                                                                     
    'ownercount': '1',
    'returnMsg':'Note: &#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;',                                             
    'FMSG2': '02/03/06 10:30AM -       B4 5000-SEND-VARIABLES'     
}

response = requests.post(url, headers=headers, data=data)
print response

print '=============================================='

soup = bs4.BeautifulSoup(response.text)
print soup