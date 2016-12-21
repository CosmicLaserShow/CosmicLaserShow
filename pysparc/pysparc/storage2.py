import logging
import os
import sqlite3

import pysparc.events

logger = logging.getLogger(__name__)

class CosmicLaserShowStorageManager(object):
    def __init__(self, path):
        logger.info("Connecting to {}".format(path))
        self.path = path
        existed = os.path.isfile(path)
        if not existed:
            conn = sqlite3.connect(path)
            c = conn.cursor()
            c.execute('''CREATE TABLE Hits(GPSTime int, Nanoseconds int, ID int, Timing int)''')
            conn.commit()
            conn.close()

    def store_event(self, event):
        if (isinstance(event, pysparc.events.ConfigEvent)):
            return

        if event.t1 is None or event.t2 is None:
            return

        device_id = event.device_id
        #logging.info("Storing event {}".format(event))
        conn = sqlite3.connect(self.path)
        c = conn.cursor()
        c.execute('''INSERT INTO Hits VALUES (?, ?, ?, ?)''', (event.timestamp, event.nanoseconds, 0 + 2 * device_id, event.t1))
        c.execute('''INSERT INTO Hits VALUES (?, ?, ?, ?)''', (event.timestamp, event.nanoseconds, 1 + 2 * device_id, event.t2))
        conn.commit()
        conn.close()

    def close(self):
        pass
