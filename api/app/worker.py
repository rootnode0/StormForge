from celery import Celery
from app.chaos import chaos_task
from app.logger import log_message
from celery.schedules import schedule

celery = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=2, retry_kwargs={"max_retries": 3})
def run_mission(self, mission_id):
    log_message(mission_id, "Started mission")

    try:
        result = chaos_task(mission_id)
        log_message(mission_id, result)
    except Exception as e:
        log_message(mission_id, f"Error: {str(e)}")
        raise


celery.conf.beat_schedule = {
    "internal-chaos": {
        "task": "app.worker.run_mission",
        "schedule": 5.0,
        "args": ("internal-" ,)
    }
}
