#By the CS 160 Mob, October 2019
# Not NULL PRIMARY KEY, user_id TEXT, rental_id TEXT
# Ryan Earl

import sqlite3
import csv
db = sqlite3.connect("zagster.sqlite3.db")
# open csv file
with open("sample.csv", 'r')as sample_csv:
    # Look at start of file
    # Grab a row of data
    lines=csv.reader(sample_csv, delimiter=',') 
    #Separate out all of the information
    for row in lines:
        user_id = row[0] 
        if user_id == "":
           user_id  = None
        rental_id = row[1]
        if rental_id == "":
            rental_id = None
        start_lat = row[2]
        if start_lat == "":
            start_lat = None
        start_lon = row[3]
        if  start_lon == "":
             start_lon = None
        end_lat = row[4]
        if end_lat == "":
            end_lat = None
        end_lon = row[5]
        if end_lon == "":
            end_lon = None
        start_time = row[6]
        if start_time == "":
            start_time = None
        end_time = [7]
        if end_time == "":
            end_time = None
        membership_name = row[8]
        if membership_name == "":
            membership_name = None
        sql_insert= f"""
        INSERT INTO rides (user_id, rental_id, start_lat, start_lon, end_lat, end_lon, start_time, end_time, membership_name)
        VALUES(?,?,?,?,?,?,?,?,?);
        """
        db.execute(sql_insert, [user_id, rental_id, start_lat, start_lon, end_lat, end_lon, start_time, end_time, membership_name])
        db.commit()
    db.close()