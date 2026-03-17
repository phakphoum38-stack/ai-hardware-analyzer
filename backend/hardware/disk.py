import psutil

def disk_info():

    disks = []

    for d in psutil.disk_partitions():

        disks.append({

            "device": d.device,

            "mount": d.mountpoint

        })

    return disks
