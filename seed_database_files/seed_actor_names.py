# download files from ftp://ftp.funet.fi/pub/mirrors/ftp.imdb.com/pub/
# - save both actors and actresses

import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from model import db, connect_to_db, Actor

import gzip
import re

def seed_actors():
    with gzip.open('../raw_actors_list/actors.list.gz', 'rb') as f:
        count = 0
        for line in f:
            count += 1
            # starts at 240
            if count > 240:
                if line[0]!='\t' and line[0]!='\n':
                    print "actor count is", count
                    line = re.sub(r"\t.*","",line)
                    names = line.split(", ")
                    try:
                        name = unicode(line)
                    except UnicodeError:
                        name = line.decode("utf-8")
                    # try:
                    #     name = unicode(line.encode('utf-8'))
                    # except:
                    #     name = unicode(line)
                    if len(names) == 2:
                        last_name = names[0]
                        first_name = names[1]
                    else:
                        last_name = None
                        first_name = names[0]

                    new_entry = Actor(name=name, last_name=last_name, first_name=first_name)
                    db.session.add(new_entry)
        
                    db.session.commit()

def seed_actresses():
    with gzip.open('../raw_actors_list/actresses.list.gz', 'rb') as f:
        count = 0
        for line in f:
            count += 1
            # starts at 240
            if count > 240:
                if line[0]!='\t' and line[0]!='\n':
                    print "actress count is", count
                    line = re.sub(r"\t.*","",line)
                    names = line.split(", ")
                    try:
                      name = unicode(line)
                    except UnicodeError:
                      name = line.decode("utf-8")
                    if len(names) == 2:
                        last_name = names[0]
                        first_name = names[1]
                    else:
                        last_name = None
                        first_name = names[0]

                    new_entry = Actor(name=name, last_name=last_name, first_name=first_name)
                    db.session.add(new_entry)
        
                    db.session.commit()

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()
    seed_actors()
    seed_actresses()