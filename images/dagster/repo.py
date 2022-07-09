from dagster import job, op, repository, schedule

@op
def hello4():
    return 1


@job
def my_job4():
    hello4()


@schedule(cron_schedule="* * * * *", job=my_job4, execution_timezone="US/Central")
def my_schedule4(_context):
    return {}


@repository
def deploy_docker_repository3():
    return [my_job4, my_schedule4]
