import csv


class CSVParser:

    @staticmethod
    def parse(filepath: str):

        events = []

        encodings = [
            "utf-8",
            "utf-8-sig",
            "cp1252",
            "latin-1"
        ]

        for encoding in encodings:

            try:

                with open(
                    filepath,
                    newline="",
                    encoding=encoding
                ) as file:

                    reader = csv.DictReader(file)

                    for row in reader:

                        events.append({

                            "timestamp": row["timestamp"],

                            "username": row["username"],

                            "ip": row["ip"],

                            "event_id": int(row["event_id"]),

                            "message": row["message"]

                        })

                return events

            except UnicodeDecodeError:

                events = []

                continue

        raise ValueError("Unsupported file encoding.")