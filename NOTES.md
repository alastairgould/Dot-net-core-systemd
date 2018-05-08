Show systemd as PID 1
Show /sbin/init and others  called by the kernel init
Show symlink from /sbin/init to systemd

Show an example service file
Show and explain targets, briefly mention mount points, and timers

Explain sample app
Walk through service file
explain the Wantedby tag in the spec file

Do a manual copy of service file and and app
Run the app via systemctl start
Show app status using systemctl status, point out memory limit 

Remove manual copy

Show spec file, create rpm and install, run, and show status in systemctl .
Explain and dicuss package manager
Show app running

Show webapplication process id using  ps -e
kill the app
Show new restarted process id with ps -e to show systemd restarted it

Show the folder /etc/systemd/system/multi-user+target.wantedby
Enable the application permently using systemctl enable
show the symlink in the wanted by folder
Disable the app using systemctl disable
Show the symlink has disappeared

Questions?
