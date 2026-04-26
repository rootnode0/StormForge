from celery import Celery
from app.chaos import chaos_task
from app.logger import log_message
from celery.schedules import schedule
from app.chaos import get_chaos_state

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=2, retry_kwargs={"max_retries": 3})
def run_mission(self, mission_id):
    if not get_chaos_state():
        log_message(mission_id, "Skipped (chaos stopped)")
        return
    log_message(mission_id, "Started mission")

    try:
        result = chaos_task(mission_id)
        log_message(mission_id, result)
    except Exception as e:
        log_message(mission_id, f"Error: {str(e)}")
        raise

@celery.task
def scheduled_mission():
    from app.chaos import get_chaos_state

    if not get_chaos_state():
        return

    run_mission.delay("internal-")

celery.conf.beat_schedule = {
    "internal-chaos": {
        "task": "app.worker.scheduled_mission",
        "schedule": 5.0,
    }
}
