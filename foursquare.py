#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      CMH
#
# Created:     21/04/2015
# Copyright:   (c) CMH 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import all of the libraries
import httplib
import urllib
import json
import pprint

def insta( offset ):
    conn = httplib.HTTPSConnection("api.foursquare.com")

    headers = {"":""}
    parameters = "client_id=177e5e845cdf455380a79a33fba7edb4"
    #conn.request("GET", "/v1/tags/skidrokyo/media/recent", parameters, headers)

    #perhsing
    #lat = "34.0493159"
    #lng = "-118.251259"

    #7th metro
    #lat = "34.0486116"
    #lng = "-118.261131"

    #pico station
    #lat = "34.04366"
    #lng = "-118.264843"

    #civic center
    #lat = "34.0534652"
    #lng = "-118.250671"

    #union station
    #lat = "34.0550474"
    #lng = "-118.2381289"

    #chinatown
    #lat = "34.0629137"
    #lng = "-118.238279"

    #little tokyo
    #lat = "34.0507486"
    #lng = "-118.237853"

    conn.request("GET", "/v2/venues/explore?ll=" + lat + "," + lng + "&client_id=NTQ5TQIWJSFKEZDPBJAZJ1Z2GZN3X1JN5IWNA4EHY54FNANA&client_secret=RUXCJO50EHTST4WM0X4ZSO5HDGKIV42KNYCDIY1ZRYXIOPLL&v=20150421&radius=800&limit=50&offset=" + offset)

    # Get the response and print the response information eg. 200 OK or 404 Not Found
    response = conn.getresponse()
    #print response.status, response.reason

    # Get and print the actual data
    data = response.read()

    # Iteration 2 parse the json into a more useful data structure
    parsed_json = json.loads(data)

    # Load the pretty printer so that we can better see the structure of the data
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(parsed_json['response']['groups'][0]['items'])
    #pp.pprint(parsed_json['response']['totalResults'])
    #pp.pprint(parsed_json['data'])
    #pp.pprint(data)

    #'''
    #json.dumps( parsed_json, sort_keys=True, indent=4, separators=(',', ': ') )
    cont = 1
    items = parsed_json['response']['groups'][0]['items']
    for item in items:
        #theLine = ""
        try:
            print item['venue']['location']['lat'], ",",
            print item['venue']['location']['lng'], ",",
            print item['venue']['name'], ",",
            print item['tips'][0]['canonicalUrl'], ",",
            print ""
        except TypeError:
            pass
        except KeyError:
            pass
        #try:
            #print (item['location']['longitude'])
            #print (",")
        #except TypeError:
            #pass
    # Close the connection
    conn.close()
    try:
        #print int(offset) + 50
        if int(offset) + 50 < int(parsed_json['response']['totalResults']):
            insta( str( int(offset) + 50 ) );
    except TypeError:
            pass
    except KeyError:
        pass
    #'''
insta("0");