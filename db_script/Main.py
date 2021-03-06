from TwitterIOC import TwitterIOC
from TaxiExecute import TaxiClientToDatabase
from DatabaseClient import DatabaseConnect
from TimeManager import TimeManager

############# CONFIG #############
# ------------- TAXII CLIENT -------------
OTX_TAXI_CLIENT = {
    "hostURL": 'otx.alienvault.com',
    "useHHTPS": True,
    "discoveryPath": 'taxii/discovery',
    "usernameKey": "e3a88efb05eb78a2c2affd8e78598fef969643976b06a9ad3998051fa2f37a15",
    "password": 'X^7PGvy0$c3$Kzk',
    "collectionNames": ['user_maldatabase'],
}

TWITTER_IOC = {"hostURL": "http://tweettioc.com/feed/domain"}
# ------------- DATE -------------
# Must be in format: YYYY-MM-DDTHH:MM:SS.ssssss+/-hh:mm (ISO8601)
# To specify specific time, use BEGIN_DATE. Otherwise, script will find a file
# -- If LAST_TIME_UPDATE.txt file NOT FOUND and BEGIN_DATE = None, script will Download All
BEGIN_DATE = None

# ------------- DATABASE -------------
DATABASE_HOST_NAME = "localhost"
DATABASE_USERNAME = "root"
DB_USER_PASSWORD = "password"
DATABASE_NAME = "DomainServer"
AUTH_PLUGIN = "mysql_native_password"


#################### MAIN ########################
# Create a time manager
timeManager = TimeManager(BEGIN_DATE)
# Create a database Client
databaseClient = DatabaseConnect(
    DATABASE_HOST_NAME, DATABASE_USERNAME, DB_USER_PASSWORD, DATABASE_NAME, AUTH_PLUGIN
)
# Create a AlientVault TAXII Client and Connect to database
alientvaultTaxiAndDatabaseConnect = TaxiClientToDatabase(
    OTX_TAXI_CLIENT['hostURL'],
    OTX_TAXI_CLIENT['useHHTPS'],
    OTX_TAXI_CLIENT['discoveryPath'],
    OTX_TAXI_CLIENT['usernameKey'],
    OTX_TAXI_CLIENT['password'],
    OTX_TAXI_CLIENT['collectionNames'],
    databaseClient,
    timeManager,
)

# Download STIXX File and Insert to database
alientvaultTaxiAndDatabaseConnect.get_STIX_and_insert_database()

# Create a Twitter IOC client and connect to database
twitterIOCAndDatabaseConnect = TwitterIOC(hostURL=TWITTER_IOC["hostURL"], myDatabase=databaseClient)

# Downloaf a text file and insert to database
twitterIOCAndDatabaseConnect.get_domain_and_insert_database()

# Update time
timeManager.write_time_to_file()