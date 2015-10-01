from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

def printMyName():
    print "Niranjan"
printMyName()
scheduler.add_job(printMyName(), 'interval', minutes=2, id='my_job_id')
#scheduler.remove_job('my_job_id')
