#!/bin/sh

echo "Hello!"
/usr/bin/crontab /cron/cron/del_accs.txt
/usr/sbin/crond -f -l 8