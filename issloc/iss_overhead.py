#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests
import time


#http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3

def main():
    """your code goes below here"""
    
    # stuck? you can always write comments
    # Try describe the steps you would take manually
    try:
        lat = float(input("What is the latitude of your coordinates\nEnter a float between 90 and -90: "))
        if lat > 90:
            print("Latittude must be less than 90")
            lat = float(input("What is the latitude of your coordinates\nEnter a float between 90 and -90: "))
        elif lat < -90:
            print("Latitude must be more than -90")
            lat = float(input("What is the latitude of your coordinates\nEnter a float between 90 and -90: "))

        
    except ValueError:
        print("Please enter valid coordinate which is a float(0.0) between 90 and -90")
        lat = float(input("What is the latitude of your coordinates\nEnter a float between 90 and -90: "))

    try:
        lon = float(input("What is the longitude of your coordinates\nEnter a float between 180 and -180: "))
        # if ans(lon) > 180:
        if lon > 180:
            print("Longitude must be less than 180")
            lon = float(input("What is the longitude of your coordinates\nEnter a float between 180 and -180: "))
        elif lon < -180:
            print("Longitude must be more than -180")
            lon = float(input("What is the longitude of your coordinates\nEnter a float between 180 and -180: "))

        
    except ValueError:
        print("Please enter valid coordinate which is a float(0.0) between 180 and -180")
        lon = float(input("What is the longitude of your coordinates\nEnter a float between 180 and -180: "))

    print(f"The next time the ISS will be overhead is: {getData(lat,lon)}")

def getData(lat,lon):
    data = requests.get(f"http://api.open-notify.org/iss-pass.json?lat={lat:.1f}&lon={lon:.1f}")
    human_data = data.json()
    epoch_time = (human_data['response'][0]['risetime'])
    my_time = time.ctime(epoch_time)
    return my_time


if __name__ == "__main__":
    main()

