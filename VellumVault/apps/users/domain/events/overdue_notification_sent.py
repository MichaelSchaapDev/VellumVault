from datetime import datetime

class OverdueNotificationSent:
    def __init__(self, user, timestamp: datetime):
        self.user = user
        self.timestamp = timestamp