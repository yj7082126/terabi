# -*- coding: utf-8 -*-
"""
Created on Tue May 29 22:46:19 2018

@author: user
"""

import prestodb

def getConn(country, isconsole):
    if isconsole:
        conn1 = prestodb.dbapi.connect(
            host='52.68.176.156',
            port=8080,
            user='yam',
            catalog='hive',
            schema='tera_console_report_' + country,
        )
        conn2 = prestodb.dbapi.connect(
            host='52.68.176.156',
            port=8080,
            user='yam',
            catalog='hive',
            schema='tera_console_dw_' + country,
        )       
    else:
        conn1 = prestodb.dbapi.connect(
            host='52.68.176.156',
            port=8080,
            user='yam',
            catalog='hive',
            schema='tera_report_' + country,
        )
        conn2 = prestodb.dbapi.connect(
            host='52.68.176.156',
            port=8080,
            user='yam',
            catalog='hive',
            schema='tera_dw_' + country,
        )    
    cur = conn1.cursor()
    cur2 = conn2.cursor()        
    return cur, cur2


    