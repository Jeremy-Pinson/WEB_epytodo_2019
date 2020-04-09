#!/usr/bin/env python3

import pymysql


def database_connect():
    connect = pymysql.connect("localhost", "root", "root", "epytodo")
    cursor = connect.cursor()
    return cursor, connect

