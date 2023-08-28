from ....shared.domain.events.handlers import event_bus
from ..events.overdue_notification_sent import OverdueNotificationSent
from ..value_objects.address import Address
from datetime import datetime, timedelta

class User:
    def __init__(self, user_id: int, name: str, address: Address):
        if not name:
            raise ValueError("Name cannot be empty")
         
        self.user_id = user_id
        self.name = name
        self.address = address
        self.overdue_notification_sent = False

    def send_overdue_notification(self):
        # Simulate sending an overdue notification
        self.overdue_notification_sent = True
        event = OverdueNotificationSent(user=self, timestamp=datetime.now())
        event_bus.dispatch(event)

    def reset_overdue_notification(self):
        self.overdue_notification_sent = False    