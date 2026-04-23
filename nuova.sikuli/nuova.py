def avvia_silentmock():
    subprocess.call([ADB, "connect", ADB_PORT],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    result = subprocess.Popen(
        [ADB, "-s", ADB_PORT, "shell",
         "am start -n com.garsal.silentmockgps/.MainActivity"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    out, err = result.communicate()
    print(">>> [silentmock] " + str(out).strip())

avvia_silentmock()