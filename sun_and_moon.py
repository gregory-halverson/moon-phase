from datetime import datetime
from moon_phase import get_status

print(get_status(datetime.now().astimezone().date()))
