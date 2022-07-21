from apscheduler.schedulers.blocking import BlockingScheduler
# advance python scheduler
import datetime
# interval 특정 주기로 연속 실행할 때 사용
# cron : crontub 형식으로 사용
def fn_interval():
    print('test interval')
    print(datetime.datetime.now())
def fn_cron():
    print('test cron')
    print(datetime.datetime.now())

sched = BlockingScheduler(timezone='Asia/Seoul')
# interval
sched.add_job(fn_interval, 'interval', seconds=5)
# cron
sched.add_job(fn_cron, 'cron', hour='9', minute='24')
sched.start()