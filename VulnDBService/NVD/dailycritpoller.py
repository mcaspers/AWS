## This script will poll the NVD database and pull any criticals for the prior day. Within AWS it leverages Lambda within a VPC as well as
## some other services that will be integrated later. Ultimately the goal is to store this data in S3 or somewhere else to trigger downstream
## work. For example, deriving/parsing out the impacted software somehow and then compare that to data in an automated software inventory.
# import the requests library
import requests
import datetime
from datetime import datetime, timedelta


# api endpoint
URL = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

# Date Parameter Values to be used later
today = datetime.now()
yesterday = today + timedelta(days=-1)

pubStartDate = yesterday.strftime("%Y-%m-%d" + "T00:00:00:000 UTC-05:00")
pubEndDate = today.strftime("%Y-%m-%d" + "T00:00:00:000 UTC-05:00")

# define parameter values
datesort = "publishDate"
severity = "CRITICAL"
totalresults = 2000

# defining parameters
PARAMS = {'sortBy':datesort, 'cvssV3Severity':severity, 'pubStartDate':pubStartDate, 'pubEndDate':pubEndDate}

# send the GET Request
r = requests.get(url = URL, params = PARAMS)

# extract in JSON
data = r.json()

# print the output
print(data)