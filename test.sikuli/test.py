import subprocess

ADB = r"C:\LDPlayer\LDPlayer9\adb.exe"

# 1. installa
def installa():
    result = subprocess.Popen(
        [ADB, "-s", "127.0.0.1:5555", "install", "-r", 
         r"C:\percorso\SilentMockGPS-v1.2.apk"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = result.communicate()
    print(">>> [install] " + str(out).strip())

# 2. avvia servizio (solo prima volta)
def avvia_servizio():
    result = subprocess.Popen(
        [ADB, "-s", "127.0.0.1:5555", "shell",
         "am start -n com.garsal.silentmockgps/.MainActivity"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = result.communicate()
    print(">>> [start] " + str(out).strip())

# 3. imposta posizione
def set_fake_gps(lat, lon):
    cmd = (
        "am broadcast -a com.garsal.silentmockgps.SET_LOCATION "
        "--es lat \"{0}\" --es lon \"{1}\""
    ).format(lat, lon)
    result = subprocess.Popen(
        [ADB, "-s", "127.0.0.1:5555", "shell", cmd],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = result.communicate()
    print(">>> [GPS] " + str(out).strip())


set_fake_gps(41.9028, 12.4964)



