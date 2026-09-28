print("====================================")
print(" SECURITY LOG MONITORING SYSTEM")
print("====================================")

logs = [
    "10:10 harshh success 192.168.1.5",
    "10:15 itachi failed 192.168.1.8",
    "10:16 itachi failed 192.168.1.8",
    "10:17 itachi failed 192.168.1.8",
    "10:25 ishantt success 192.168.1.12",
    "10:30 pranjal failed 192.168.1.20",
    "10:31 pranjal success 192.168.1.20",
    "10:40 unknown failed 45.67.89.10",
    "10:41 unknown failed 45.67.89.10",
    "10:50 harshh success 192.168.1.5"
]

failed = {}
alert = []

print()
print("Checking logs...")
print()

# checking the logs one by one
for log in logs:

    data = log.split()

    time = data[0]
    user = data[1]
    status = data[2]
    ip = data[3]

    if status == "failed":

        if user in failed:
            failed[user] = failed[user] + 1
        else:
            failed[user] = 1

        if failed[user] >= 3:
            alert.append(log)

        if user == "unknown":
            alert.append(log)


print("------------------------------------")
print("ALL SECURITY LOGS")
print("------------------------------------")

for log in logs:
    print(log)


print()
print("------------------------------------")
print("FAILED LOGIN ATTEMPTS")
print("------------------------------------")

if len(failed) == 0:
    print("No failed login attempts")

else:
    for user in failed:
        print(user, ":", failed[user], "attempts")


print()
print("------------------------------------")
print("SUSPICIOUS ACTIVITY")
print("------------------------------------")

if len(alert) == 0:
    print("No suspicious activity found")

else:
    for log in alert:
        print("WARNING:", log)


print()
print("------------------------------------")
print("SECURITY STATUS")
print("------------------------------------")

if len(alert) > 0:
    print("ALERT - Suspicious activity found")
else:
    print("SAFE - No suspicious activity")


print()
print("------------------------------------")
print("CREATING REPORT")
print("------------------------------------")

file = open("security_report.txt", "w")

file.write("SECURITY LOG REPORT\n")
file.write("-------------------\n")

file.write("Total logs checked: " + str(len(logs)) + "\n\n")

file.write("Failed Login Attempts:\n")

for user in failed:
    file.write(user + " : " + str(failed[user]) + "\n")

file.write("\nSuspicious Activities:\n")

if len(alert) == 0:
    file.write("No suspicious activity found\n")
else:
    for log in alert:
        file.write(log + "\n")

file.write("\nSecurity Status: ")

if len(alert) > 0:
    file.write("ALERT")
else:
    file.write("SAFE")

file.close()

print("Report saved successfully.")
print("File name: security_report.txt")
print()
print("Program finished.")