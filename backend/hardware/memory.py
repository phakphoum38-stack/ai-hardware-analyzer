import psutil

def memory_info():

    m = psutil.virtual_memory()

    return {

        "total_gb": round(m.total/(1024**3),2),

        "used_percent": m.percent

    }
