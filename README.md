# Services_Restart_Python_Win
Restart multiple services in Windows Server, one by one with this Python script

How to use it -

Save the script

Open command prompt or Powershell with Elevated priviledges (Open as Admninistrator)

Navigate to the folder where your script is saved

then run -
python YourScriptName.py

The services will first be stopped and then started after 7 secs of wait time
-------------------------------------------------------------------------------
fyi, We use wait times because sometimes services take time to stop and then start, if you give no wait time, the service will stop but will not be able to start

