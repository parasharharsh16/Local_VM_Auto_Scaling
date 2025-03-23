import psutil
import time
import json
from google.cloud import compute_v1
from google.auth import default

def loadJsonConfig():
    with open('config.json', 'r') as file:
        configData = json.load(file)
    return configData

def checkCpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def scaleUp(configInfo):
    credentials, project = default()
    manager = compute_v1.InstanceGroupManagersClient(credentials=credentials)

    theGroup = manager.get(
        project=configInfo["PROJECT_ID"],
        zone=configInfo["ZONE"],
        instance_group_manager=configInfo["INSTANCE_GROUP_NAME"],
    )

    newSize = theGroup.target_size + configInfo["INCREMENT_VM_COUNT"]

    print(f"Scaling up group '{configInfo['INSTANCE_GROUP_NAME']}' to {newSize} instances...")

    if newSize <= configInfo["MAX_VM_COUNT"]:
        manager.resize(
            project=configInfo["PROJECT_ID"],
            zone=configInfo["ZONE"],
            instance_group_manager=configInfo["INSTANCE_GROUP_NAME"],
            size=newSize,
        )

        print("Scaling up complete.")
    else:
        print(f"Max scale reached. Already at max VM count: {configInfo['MAX_VM_COUNT']}")

def monitorAndScale(configInfo):
    while True:
        cpuVal = checkCpu()

        print(f"CPU usage right now: {cpuVal}%")

        if cpuVal > configInfo["CPU_THRESHOLD"]:
            print(f"CPU is too high! It's at {cpuVal}% which is over {configInfo['CPU_THRESHOLD']}% threshold. Time to scale up.")
            scaleUp(configInfo)

            time.sleep(configInfo["COOLDOWN_PERIOD"])
        else:
            time.sleep(10)

if __name__ == "__main__":
    configInfo = loadJsonConfig()
    print("Starting to watch CPU for scaling up...")
    monitorAndScale(configInfo)