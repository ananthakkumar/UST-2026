summary:
A network/security engineer needs to monitor system logs to detect potential malware or suspicious activity. Logs are collected from remote systems via an API and may contain metadata such as IP addresses, timestamps, actions, and status codes. Unusual patterns—like excessive requests from a single IP within a short time window—can indicate bot activity, brute-force attacks, or compromised hosts. The task is to automatically analyze these logs and flag suspicious IPs for further investigation.


the phases/workflow of the project. 


1. Collect Logs
Retrieve log data from remote servers using an API (or local files), containing metadata such as timestamp, IP address, action, and status.

2️. Preprocess & Organize Data
Parse the logs, clean invalid entries, and group events by IP address and time for structured analysis.

3️. Analyze Activity Patterns
Check for abnormal behavior, such as too many requests from the same IP within a short time window or repeated failed actions.

4️. Detect Suspicious Entities
Compare activity against predefined thresholds to identify potentially malicious IPs or events.

5️. Generate Alerts / Report
Output flagged IP addresses with details (request count, time range) for security teams to review and respond.

6️. Optional Response Actions
Trigger automated actions such as notifications, blocking the IP, or escalating the incident for further investigation.

