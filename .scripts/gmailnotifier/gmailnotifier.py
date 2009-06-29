#!/usr/bin/python
"""
gmailnotifier.py - A python script to pop an OSD notification for any new
mail messages in your gmail account every minute. You can change this interval
if you, want by changing the assignment to the variable 'timeout' in line 
49 below. By Default, it is 60 seconds.

Few points to note:

1. Here is 'new' from the script's perspective. 

For example, let us say at the first iteration, your inbox had 3 new
mails. So you would get a pop up first time saying '3 new messages'.
In the next iteration however you would NOT get any notification.

But now suppose you get another new mail. In the subsequent iteration
you would get a pop up saying '1 New message'. I hope you get the point.

2. This script does NOT update the read-flag in your actual gmail inbox.
For example, in the above example, if you really log in using the browser
you would find 4 new mails waiting in your inbox.


3. And above all, enjoy this nifty piece of python code! ;-)


Copyright (C) 2009 seemanta@gmail.com , inspired by the command line 
script to check gmail by Baishampayan Ghose <b.ghose@ubuntu.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation. And as usual without any
sort of warranty.

"""

import os                 # For os related stuff
import sys                # For system related stuff
import urllib             # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
import pynotify           # For notifications
import glib               # For glib functions
import ConfigParser       # For parsing configuration file

# Defining global variables to hold our mail information
prev_mails = []
curr_mails = []

#timeout = get_timeout_from_conf_file ()
#img_uri = get_img_uri_from_conf_file ()

timeout = 60  # default is 60 seconds 
img_uri = "file:///usr/share/pixmaps/gmail_logo.png"  # default location
username = ""
pwd = ""



def read_config_file():
   global timeout, img_uri, username, pwd
   config = ConfigParser.RawConfigParser()
   config.read(sys.argv[1])
   if config.has_option('Main','check_interval'):
       s_timeout = config.get('Main', 'check_interval');
       # Converting the timeout from string to int
       timeout = int(s_timeout)
   if config.has_option('Main','img_uri'):
       img_uri = config.get('Main', 'img_uri')
   if config.has_option('Main', 'username'):
       username = config.get('Main', 'username')
   if config.has_option('Main', 'password'):
       pwd = config.get('Main', 'password')
    
def timer_cb():
    if __name__ == "__main__":
        f = auth()  # Do auth and then get the feed
        readmail(f) # Let the feed be chewed by feedparser
        return True;

_URL = "https://mail.google.com/gmail/feed/atom"

# I am inheriting from FancyURLopener class because I want to provide my
# own username and password for checking my mail.
class MyFancyURLopener(urllib.FancyURLopener):
    def prompt_user_passwd(self, host, realm):
        """Overriding this as mentioned in the urllib environment """
        global username, pwd
        try:
            user = username
            passwd = pwd
            return user,passwd
        except KeyboardInterrupt:
            print()
            return None, None


def auth():
    '''The method to do HTTPBasicAuthentication'''
    opener = MyFancyURLopener()
    f = opener.open(_URL)
    feed = f.read()
    return feed

def readmail(feed):
    '''Parse the Atom feed and get our information'''

    # declare our global variables to hold the mail info
    global prev_mails, curr_mails
    # this is a local variable
    new_mails = 0;
    # parse the feed
    atom = feedparser.parse(feed)
    #print "You have %s new mails" % len(atom.entries)

    # Update the curr_mails list with all the subjects 
    for i in xrange(len(atom.entries)):
        curr_mails.append(atom.entries[i].summary+atom.entries[i].updated)

    for mail in curr_mails:
        if not mail in prev_mails:
            new_mails += 1
  
    if new_mails != 0:
        if new_mails == 1 :
            # Uncomment for debugging
            #print "You have %s new mail" % new_mails 
            msg = str(new_mails) + " New mail"
        else:
            # Uncomment for debugging
            #print "You have %s new mails" % new_mails 
            msg = str(new_mails) + " New mails"

        # Now pop up the message, finally
        pynotify.init("Gmail Inbox")
        notification = pynotify.Notification("Gmail Alert!",msg, img_uri)
        notification.show()
        # There are 0 messages, no need to do anything

    # curr_mails becomes prev_mails in next iteration and zeroing out curr_mails
    prev_mails = curr_mails
    curr_mails = []
   

if __name__ == "__main__":
 
    read_config_file()
   
    # create a glib main loop instance
    mainloop = glib.MainLoop()

    # register callbacks
    glib.timeout_add_seconds(timeout, timer_cb)

    # run the mainloop, and continue ad infinitum
    mainloop.run()

