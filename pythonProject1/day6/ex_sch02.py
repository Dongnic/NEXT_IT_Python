# 실행 job 종료
import time

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

sched = BlockingScheduler(timezone='Asia/Seoul')


def job():
    print('ex job')
    print(datetime.datetime.now())
def job2():
    print('ex job2')
    print(datetime.datetime.now())
    job_instance = sched.get_job()
    # id가 job1인 job 종료
    if job_instance:
        sched.remove_job('job1')
sched.add_job(job, 'interval', seconds=1, id='job1')
sched.add_job(job2, 'cron', second='*/3', id='job2')
sched.start()
import time
time.sleep(4)
# 등록된 job list
