#!/usr/bin/python3

import pymysql
from Config import *

#########################################################################
def get_all_domains():
    # Open database connection (ip, username, password, dbName)
    db = pymysql.connect(ip, username, password, dbName)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        sql = "SELECT * FROM domains"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error in getting all domains!")
        print(e)
    cursor.close()
    db.close()

def get_latest_domain(id):
    # Open database connection (ip, username, password, dbName)
    db = pymysql.connect(ip, username, password, dbName)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        sql = "SELECT * FROM domains WHERE id > %s"
        val = (str(id),)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error in getting lastest domain(s)!")
        print(e)
    cursor.close()
    db.close()

def update_last_domain_id(id):
    # Open database connection (ip, username, password, dbName)
    db = pymysql.connect(ip, username, password, dbName)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        sql = "UPDATE coreDNS SET id = %s"
        val = (str(id),)
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        print("Error in updating last domain id!")
        print(e)
        db.rollback()
    db.close()

def init_last_domain():
    # Open database connection (ip, username, password, dbName)
    db = pymysql.connect(ip, username, password, dbName)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        sql = "DELETE FROM coreDNS"
        cursor.execute(sql)
        db.commit()

        sql = "INSERT INTO coreDNS (id) VALUES (1)"
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print("Error in initialize last domain!")
        print(e)
        db.rollback()
    cursor.close()
    db.close()

def get_last_domain_id():
    # Open database connection (ip, username, password, dbName)
    db = pymysql.connect(ip, username, password, dbName)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        sql = "SELECT * FROM coreDNS"
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("Error in getting last domain id!")
        print(e)
    cursor.close()
    db.close()