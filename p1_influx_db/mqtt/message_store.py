class MessageStore:
    def __init__(self):
        self.message_queue = []

    def add_message(self, topic, payload):
        self.message_queue.append((topic, payload))

    def retrieve_messages(self):
        messages_to_send = self.message_queue.copy()
        self.message_queue.clear()
        return messages_to_send

    def has_messages(self):
        return len(self.message_queue) > 0

    def get_message(self):
        if self.message_queue:
            return self.message_queue.pop(0)
        return None
