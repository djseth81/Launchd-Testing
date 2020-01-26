import sys
import os
import launchd
import time

def install(label, plist):
    '''
    Utility function to store a new .plist file and load it

    :param label: job label
    :param plist: a property list dictionary
    '''
    fname = launchd.plist.write(label, plist)
    launchd.load(fname)


def uninstall(label):
    '''
    Utility function to remove a .plist file and unload it

    :param label: job label
    '''
    if launchd.LaunchdJob(label).exists():
        fname = launchd.plist.discover_filename(label)
        launchd.unload(fname)
        os.unlink(fname)


myplist = dict(
              Label = "com.example.launched.datewriter",
              Disabled = False,
              KeepAlive = True,
              RunAtLoad = True,
              Program = __file__ ,
              ProgramArguments = ["/bin/bash", "-c", "python3", __file__ ],
              ServiceDescription = "Test for launchd",
              SartInterval = 10
              )
label = myplist['Label']
job = launchd.LaunchdJob(label)
if not job.exists():
    print("'%s' is not loaded in launchd. Installing..." % (label))
    install(label, myplist)
else:
    if job.pid is None:
        print("'%s' is loaded but not currently running" % (job.label))
    else:
        print("'%s' is loaded and currently running: PID = %s" % (job.label, job.pid))
choice = input("Uninstall? [y/n]: ")
if choice == "y":
    print("Uninstalling...")
    uninstall(label)

#Reads back queued launchd jobs
for job in launchd.jobs():
    print(job.label,':',job.pid)