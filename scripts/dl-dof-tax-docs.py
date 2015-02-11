from sys import argv
import csv
import requests
import bs4
import time
import random

script, filename = argv

# f = open(filename)

url = "http://nycprop.nyc.gov/nycproperty/nynav/jsp/selectbbl.jsp"
headers = {'User-Agent' : 'Mozilla/5.0'}

count = 0

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)

    try:
        for row in reader:
            print row
            # example url from arcis http://a836-acris.nyc.gov/bblsearch/bblsearch.asp?borough=3&block=1306&lot=35
            block = row[1]
            lot = row[2]
            address = row[11]
            
            url2post = "http://nycprop.nyc.gov/nycproperty/nynav/jsp/stmtassesslst.jsp"
            # print "the address is %s and the url is: %s" % (address, url2post)

            data = {
                'FFUNC': 'C',
                'q49_boro': '1',
                'q49_block_id': '01221',
                'q49_lot': '0007',
                q49_prp_ad_street_no: '109',    
                q49_prp_nm_street: 'WEST 90 STREET',                   
                q49_prp_id_apt_num: '',     
                q49_prp_ad_city: 'New york',            
                q49_prp_cd_state: 'NY',
                q49_prp_cd_addr_zip: '10024',
                bblAcctKeyIn1: '1',
                bblAcctKeyIn2: '01221',
                bblAcctKeyIn3: '0007',
                bblAcctKeyIn4: '',
                ownerName: 'NYC HOUSING AUTHORITY',
                ownerName1: 'NYC HOUSING AUTHORITY',                                                 
                ownerName2: '',                                                                     
                ownerName3: '',                                                                     
                ownerName4: '',                                                                     
                ownercount: '1',
                returnMsg:Note: '&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;&#65533;',                                             
                FMSG2: '02/03/06 10:30AM -       B4 5000-SEND-VARIABLES'     
            }

            print data

            t = open(address + ".csv", 'w+')
            # write column headers
            t.write("Reel/Pg/File,CRFN, Lot, Partial, Doc Date, Recorded / Filed, Document Type, Pages, Party1, Party2, Party3 / Other, More Party 1/2 Names, Corrected / Remarks, Doc Amount\n")

            response = requests.post(url, headers=headers,data=data)
            soup = bs4.BeautifulSoup(response.text)
            
            print soup            

    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


