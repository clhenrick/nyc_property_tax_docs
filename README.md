# nyc_property_tax_docs
Scraping data from NYC Dept Of Finance building tax document PDFs

## To Do:

- [ ] script to dl PDFs by bbl & date
- [ ] script to scrape data from tax documents
- [ ] determine which properties have rent stabilized units
- [ ] determine rent stabilized unit increase or decrease from 2009 - 2014

## URL Endpoints: 
* **Example URL for a PDF Document:** For a property in Staten Island (5) with the block 881 and lot 161:  
  http://nycprop.nyc.gov/nycproperty/StatementSearch?bbl=5008810161&stmtDate=20141121&stmtType=SOA
* **Note:** URLs don't all use the same date for statements so it might be better to do a POST request in the following URL: http://nycprop.nyc.gov/nycproperty/nynav/jsp/selectbbl.jsp  
Then do a search for the links to the quarterly statements.

### Form Data
```
FFUNC:C
q49_boro:1
q49_block_id:01221
q49_lot:0007
q49_prp_ad_street_no:109     
q49_prp_nm_street:WEST 90 STREET                   
q49_prp_id_apt_num:     
q49_prp_ad_city:New york            
q49_prp_cd_state:NY
q49_prp_cd_addr_zip:10024
bblAcctKeyIn1:1
bblAcctKeyIn2:01221
bblAcctKeyIn3:0007
bblAcctKeyIn4: 
ownerName:NYC HOUSING AUTHORITY
ownerName1:NYC HOUSING AUTHORITY                                                 
ownerName2:                                                                      
ownerName3:                                                                      
ownerName4:                        
```
  
## PDF scraping options
  * [pdf.js](http://mozilla.github.io/pdf.js/)
  * [pdf extract](https://github.com/nisaacson/pdf-extract)

## Resources
These things might be helpful:

- [Rent Stabilized Building List](https://github.com/clhenrick/dhcr-rent-stabilized-data) (via DHCR/RGB)
- [NYC Geo Client API](https://developer.cityofnewyork.us/api/geoclient-api)
- [NYC MapPluto data sets archive](http://www.nyc.gov/html/dcp/html/bytes/archive_pluto_mappluto.shtml)