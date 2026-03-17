import psutil

def network_info():

    return list(psutil.net_if_addrs().keys())
