import requests
import datetime
import argparse
import os
import subprocess


def step(title):
    print("----> {}".format(title))

def log(s):
    lines = s.splitlines()
    for line in lines:
        print("      {}".format(line))


def login(username, password):
    """
    Logs the user into the iGEM website with given credentials.

    @param username     The username
    @param password     The password
    @returns The session object
    """

    session = requests.Session()
    session.post("https://igem.org/Login2", data=dict(
        username=username,
        password=password,
        return_to="https://{}.igem.org/Main_Page".format(the_year),
        Login="Login"
    ))

    return session.cookies.get_dict()


def file_exists(filename, session, ignore_team_prefix=False):
    # Append the prefix to the filename
    prefixed_filename = filename
    if not ignore_team_prefix and not "T--{}".format(the_team) in prefixed_filename:
        prefixed_filename = "T--{}--{}".format(the_team, prefixed_filename)
    
    s = requests.Session()

    r = s.get("https://{}.igem.org/Special:ListFiles?limit=50&ilsearch={}&user=".format(the_year, prefixed_filename), cookies=session)
    print(r.content)
    return "No results" not in r.content


def upload_file(filename, session, ignore_team_prefix=False):
    # Append the prefix to the filename
    the_filename = filename
    if not ignore_team_prefix and not "T--{}".format(the_team) in the_filename:
        the_filename = "T--{}--{}".format(the_team, the_filename)

    s = requests.Session()

    # Upload the file
    r = s.post("https://{}.igem.org/Special:Upload".format(the_year), 
        files=dict(
            wpUploadFile=open(filename, "rb")
        ),    
        data=dict(
            wpDestFile=the_filename,
            wpUploadDescription=filename,
            #wpLicense="selected",
            wpWatchthis="1",

            #wpEditToken=#TODO: change,
        
            title="Special:Upload",
            wpDestFileWarningAck=True
        ), cookies=session)
    
    return r.content


def get_user_information(session):
    """
    Retrieves the user information form from the iGEM page

    @param session      The session obtained via login
    """
    s = requests.Session()

    # Retrieve the page
    r = s.get("https://igem.org/User_Information", cookies=session)
    print(r.content)


# Setup the parser
parser = argparse.ArgumentParser(description="Uploads a file to the iGEM server if it is not present.")
parser.add_argument("--team", help="Set the iGEM team", default=os.environ.get("IGEM_TEAM", None))
parser.add_argument("--year", help="Set the year of iGEM participation", default=os.environ.get("IGEM_YEAR", datetime.datetime.now().year))
parser.add_argument("--username", help="Set the username used for authentication", default=os.environ.get("IGEM_USERNAME", None))
parser.add_argument("--password", help="Set the password used for authentication", default=os.environ.get("IGEM_PASSWORD", None))

args = parser.parse_args()

the_year = args.year
the_team =  args.team
the_username = args.username
the_password = args.password

#############################################################################################################################
## Authenticate the user

step("Authenticate user")
session = login(the_username, the_password)
if not bool(session):
    log("Authentication failed. Please provide proper credentials in the $IGEM_USERNAME and $IGEM_PASSWORD environment variables.")
    exit(-1)


#############################################################################################################################
## Generate static pages

step("Generate static pages")
os.system("rm -rf public")
p = subprocess.Popen(["hugo"], stdout=subprocess.PIPE)
log(p.stdout.read())


#############################################################################################################################
## Locate all assets 

step("Locate all assets")


#############################################################################################################################
## Hash all files and compare to cache

step("Identify all new/updated assets")

#############################################################################################################################
## Upload all new assets

step("Upload all new/updated assets")

#############################################################################################################################
## Update asset locations in static pages

step("Update asset locations")

#############################################################################################################################
## Update wiki pages

step("Update wiki pages")



print("====> Website deployed:")
print("      https://{}.igem.org/Team:{}".format(the_year, the_team))

#get_user_information(session)
#print(file_exists("WelcomeToiGEM SDU.jpg", session, ignore_team_prefix=True))