#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      CMH
#
# Created:     17/04/2015
# Copyright:   (c) CMH 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import all of the libraries
import httplib
import urllib
import json
import pprint
import time

def insta( max_tag_id ):
    conn = httplib.HTTPSConnection("api.instagram.com")

    headers = {"":""}
    parameters = "client_id=177e5e845cdf455380a79a33fba7edb4"
    #conn.request("GET", "/v1/tags/skidrokyo/media/recent", parameters, headers)
    tag = "TrainLikeABeastLookLikeABeauty"
    conn.request("GET", "/v1/tags/" + tag + "/media/recent?client_id=177e5e845cdf455380a79a33fba7edb4&max_tag_id=" + max_tag_id)
    #conn.request("GET", "/v1/locations/search?lat=48.858844&lng=2.294351&distance=805&client_id=177e5e845cdf455380a79a33fba7edb4&max_tag_id=" + max_tag_id)

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
    pp.pprint(parsed_json['data'])
    #pp.pprint(data)
    #json.dumps( parsed_json, sort_keys=True, indent=4, separators=(',', ': ') )
    cont = 1
    items = parsed_json['data']
    for item in items:
        #theLine = ""
        try:
            print item['location']['latitude'], ",",
            #theLine = theLine + item['location']['latitude'] + ","
            print item['location']['longitude'], ",",
            #theLine = theLine + item['location']['longitude'] + ","
            print item['link'], ",",
            #theLine = theLine + item['link'] + ","
            print item['images']['standard_resolution']['url']
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
        time.sleep(5)
        insta(parsed_json['pagination']['next_max_id']);
    except TypeError:
            pass
    except KeyError:
        pass

insta("0");