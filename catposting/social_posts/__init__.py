import mysql.connector

CAT_CONN = mysql.connector.connect(
    host="localhost",
    user="catposting",
    password="TBDDevelopment7654",
    database="catposting"
)

CURSOR = CAT_CONN.cursor()

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'