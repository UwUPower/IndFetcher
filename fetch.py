import requests
import json 
from datetime import datetime
import subprocess
import time

query = {'productKey':'DOC', 'persons':'1'}

# The IND API will be fetched automatically every 10 seconds until a targeted timeslot found
while True:

    # For fear that the programe is dead, this line is added
    print('I am running.')

    response = requests.get("https://oap.ind.nl/oap/api/desks/AM/slots/", params=query)

    rawText = response.text

    # Since the raw text format is malformed and and cannot be transformed to json 
    # further cleansing is done below
    cleanedText  = rawText.lstrip(")]}',\n")

    responseJson = json.loads(cleanedText)

    # The first date in the data array is the first available date for appoinment to collect residence permit in Amsterdam desk
    firstAvailableDateStr = responseJson.get('data')[0].get('date')

    firstAvailableDate = datetime.strptime(firstAvailableDateStr, '%Y-%m-%d')
    today = datetime.now()

    difference = int((firstAvailableDate - today).days)

    # If the first available date is within 3 weeks, popup a window message
    # Assume the difference should be greater than or eq to 1 because sometimes people drop their timeslot at the very last minute, and that time slot is useless.
    if difference <= 21 and difference >= 1:
        applescript = """
        display dialog "A near timeslot is found, please go to https://oap.ind.nl/oap/en/#/doc" ¬
        with title "IND timeslot withtin 3 weeks found" ¬
        with icon caution ¬
        buttons {"OK"}
        """

        subprocess.call("osascript -e '{}'".format(applescript), shell=True)

        # break the while loop if a targeted timeslot found
        break 

    # The IND API will be fetched automatically every 10 seconds
    time.sleep(10)


