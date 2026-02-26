import requests
from collections import defaultdict
from datetime import datetime

# ------------------------------
# CONFIGURATION
# ------------------------------
API_URL = "https://example.com/api/logs"  # Replace with real API
REQUEST_THRESHOLD = 5        # Max requests allowed
TIME_WINDOW_SECONDS = 60     # Within 1 minute


# ------------------------------
# STEP 1: DOWNLOAD LOGS FROM API
# ------------------------------
def fetch_logs():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()  # Expecting JSON logs
    except Exception as e:
        print("Error fetching logs:", e)
        return []


# ------------------------------
# STEP 2: ANALYZE LOGS
# ------------------------------
def detect_suspicious_activity(logs):

    ip_activity = defaultdict(list)

    # Group timestamps by IP
    for log in logs:
        ip = log["ip"]
        timestamp = datetime.fromisoformat(log["timestamp"])
        ip_activity[ip].append(timestamp)

    suspicious_ips = []

    # Analyze activity per IP
    for ip, times in ip_activity.items():
        times.sort()

        for i in range(len(times)):
            count = 1

            for j in range(i + 1, len(times)):
                diff = (times[j] - times[i]).total_seconds()

                if diff <= TIME_WINDOW_SECONDS:
                    count += 1
                else:
                    break

            if count >= REQUEST_THRESHOLD:
                suspicious_ips.append((ip, count))
                break

    return suspicious_ips


# ------------------------------
# STEP 3: MAIN PROGRAM
# ------------------------------
def main():

    logs = fetch_logs()

    if not logs:
        print("No logs available.")
        return

    suspicious = detect_suspicious_activity(logs)

    if suspicious:
        print("\n⚠️ Suspicious IP Activity Detected:")
        for ip, count in suspicious:
            print(f"IP: {ip} | Requests in short time: {count}")
    else:
        print("\n✅ No suspicious activity found.")


if __name__ == "__main__":
    main()
