import platform
import psutil

def cpu_info():

    return {

        "model": platform.processor(),

        "physical_cores": psutil.cpu_count(logical=False),

        "threads": psutil.cpu_count()

    }
