#!/usr/bin/env python
# refer to: https://pypi.python.org/pypi/python-crontab

from crontab import CronTab
cron = CronTab('root')
job = cron.new(command='/foo/bar',comment='bar')
job.minute.during(5,50).every(5)  # 5-50/5 * * * * /foo/bar # bar
cron.write()
