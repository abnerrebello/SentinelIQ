class RuleEngine:

    @staticmethod
    def detect(events):

        alerts = []

        failed = {}

        # -----------------------------
        # Brute Force Detection
        # -----------------------------
        for event in events:

            if event["event_id"] == 4625:

                ip = event["ip"]

                failed[ip] = failed.get(ip, 0) + 1

        for ip, count in failed.items():

            if count >= 5:

                alerts.append({
                    "type": "Brute Force Attack",
                    "severity": "Critical",
                    "ip": ip,
                    "failed_attempts": count,
                    "mitre_id": "T1110",
                    "mitre_name": "Brute Force"
                })

        # -----------------------------
        # PowerShell Execution
        # -----------------------------
        for event in events:

            if event["event_id"] == 4688:

                alerts.append({
                    "type": "PowerShell Execution",
                    "severity": "High",
                    "ip": event["ip"],
                    "failed_attempts": 0,
                    "mitre_id": "T1059.001",
                    "mitre_name": "PowerShell"
                })

        # -----------------------------
        # Privilege Escalation
        # -----------------------------
        for event in events:

            if event["event_id"] == 4672:

                alerts.append({
                    "type": "Privilege Escalation",
                    "severity": "High",
                    "ip": event["ip"],
                    "failed_attempts": 0,
                    "mitre_id": "T1068",
                    "mitre_name": "Exploitation for Privilege Escalation"
                })

        # -----------------------------
        # Suspicious Service Installation
        # -----------------------------
        for event in events:

            if event["event_id"] == 4697:

                alerts.append({
                    "type": "Suspicious Service Installed",
                    "severity": "Medium",
                    "ip": event["ip"],
                    "failed_attempts": 0,
                    "mitre_id": "T1543",
                    "mitre_name": "Create or Modify System Process"
                })

        # -----------------------------
        # Security Log Cleared
        # -----------------------------
        for event in events:

            if event["event_id"] == 1102:

                alerts.append({
                    "type": "Security Log Cleared",
                    "severity": "Critical",
                    "ip": event["ip"],
                    "failed_attempts": 0,
                    "mitre_id": "T1070.001",
                    "mitre_name": "Clear Windows Event Logs"
                })

        return alerts