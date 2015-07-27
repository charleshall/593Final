#-------------------------------------------------------------------------------
# Name:        module2
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

def insta( max_tag_id ):
    conn = httplib.HTTPSConnection("api.instagram.com")

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
    lat = "34.0507486"
    lng = "-118.237853"

    conn.request("GET", "/v1/locations/search?lat=" + lat + "&lng=" + lng + "&client_id=177e5e845cdf455380a79a33fba7edb4&max_tag_id=" + max_tag_id)

    #f = open('skidrokyo.csv','w')

    # Get the response and print the response information eg. 200 OK or 404 Not Found
    response = conn.getresponse()
    #print response.status, response.reason

    # Get and print the actual data
    data = response.read()

    # Iteration 2 parse the json into a more useful data structure
    parsed_json = json.loads(data)

    # Load the pretty printer so that we can better see the structure of the data
    pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(parsed_json['pagination'])
    #pp.pprint(parsed_json['meta'])
    #pp.pprint(parsed_json['data'])
    #pp.pprint(data)
    #json.dumps( parsed_json, sort_keys=True, indent=4, separators=(',', ': ') )
    cont = 1
    items = parsed_json['data']
    for item in items:
        #theLine = ""
        try:
            print item['latitude'], ",",
            #theLine = theLine + item['location']['latitude'] + ","
            print item['longitude'], ",",
            #theLine = theLine + item['location']['longitude'] + ","
            print item['name'], ","
            #theLine = theLine + item['link'] + ","
            #print item['images']['standard_resolution']['url']
            #theLine = item['location']['latitude']
            #theLine = theLine + item['location']['latitude'] + "," #+ item['location']['longitude'] + "," + item['link'] + "," + item['images']['standard_resolution']['url'] + "\n"
            #print theLine
            #print (",")
            #print "\n"
            #f.write(theLine)
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
    #f.close()
    conn.close()
    try:
        #print parsed_json['pagination']['next_max_id']
        insta(parsed_json['pagination']['next_max_id']);
    except TypeError:
            pass
    except KeyError:
        pass

insta("0");