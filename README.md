# SafeDex 
There has been a set of published known malicious drivers being used in attacks on Windows machines. While drivers known to be bad were supposed to be prevented from installation via a blocklist, researchers discovered these ![bad_drivers](https://www.bleepingcomputer.com/news/microsoft/microsoft-fixes-windows-vulnerable-driver-blocklist-sync-issue/) were actually not being blocked as the list was not being updated/applied correctly. 

Microsoft says they've "fixed" the syncing of this blocklist, but I figure because it seems like such a simple task why not start to make a script to do so automatically if they ever forget to update the list again. 

