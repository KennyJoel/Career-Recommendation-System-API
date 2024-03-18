from service.JobsService import get_students
import logging


from fastapi import APIRouter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("logs//user.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


router = APIRouter(tags=["Jobs"], prefix="/jobs")

@router.get("/getallstudents")
def getallstudents(careerpath: str = None):
    return get_students(careerpath)