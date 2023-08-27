#!/usr/bin/python3

from dataWrapper import DatabaseRecorder as dr


dbName = "futureIndex.db"
db = dr(dbName)
db.read_db()

