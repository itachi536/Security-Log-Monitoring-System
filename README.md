# Security Log Monitoring & Suspicious Activity Detection System

## Project Overview

This is a simple beginner-level Python project that checks login logs and finds suspicious activity.

The program counts failed login attempts. If a user has three or more failed attempts, it gives a warning. It also detects login attempts from an unknown user.

## Objective

To create a basic Python program that can monitor sample security logs and identify suspicious login activity.

## Features

- Checks sample security logs
- Counts failed login attempts
- Detects repeated failed logins
- Detects unknown users
- Displays warnings
- Creates a security report

## Technologies Used

- Python 3
- VS Code / IDLE
- GitHub

No external Python libraries are required.

## Python Concepts Used

- Lists
- Dictionaries
- Variables
- For loops
- If-else statements
- String split()
- File handling

## Project Files

```text
security_log.py
README.md
statement.md
project_report.pdf
security_report.txt
```

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code or another Python editor.
3. Run:

```text
python security_log.py
```

4. The program will display the logs, failed attempts and suspicious activity.
5. It will create `security_report.txt`.

## Testing

The sample data should show:

- itachi with 3 failed attempts
- unknown user activity
- suspicious activity warnings
- an ALERT security status
- a generated security report

## Limitations

This is an educational project. It uses sample logs and does not monitor a real computer or network.

## Future Scope

The project could later be improved with real log files, real-time monitoring, a graphical interface or automatic notifications.

## Conclusion

This project shows how basic Python programming can be used for a small cybersecurity-related application.
