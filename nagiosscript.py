#!/usr/bin/env python
import sys
import httplib

# loope over sites and if anython but 200 or 301 shows sound alarm

for site_name in ["prolinuxhub.com", "prolinuxhub.com", "site2.com",  # REPLACE WITH YOUR WEBSITES
]:
    try:
        conn = httplib.HTTPConnection(site_name)
        conn.request("HEAD", "/")
        r1 = conn.getresponse()
        conn.close()
        website_return = r1.status
        if website_return != 200 and website_return != 301:
            print "Problem with " + site_name
	    sys.exit(2)

    except Exception as e:
        print "Possibly server down " + site_name
	sys.exit(2)
    
