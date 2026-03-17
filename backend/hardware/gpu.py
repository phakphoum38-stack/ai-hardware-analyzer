import subprocess

def gpu_info():

    try:

        out = subprocess.check_output("lspci",shell=True).decode()

        gpus = []

        for line in out.split("\n"):

            if "VGA" in line:

                gpus.append(line)

        return gpus

    except:

        return ["GPU detection unavailable"]
