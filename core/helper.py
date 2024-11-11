import random

class EventDispatcher:
    def __init__(self):
        # Dictionary to hold event names and their associated listeners
        self._listeners = {}

    def add_listener(self, event_name, listener):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)

    def remove_listener(self, event_name, listener):
        if event_name in self._listeners:
            self._listeners[event_name].remove(listener)
            # Clean up if there are no listeners left for the event
            if not self._listeners[event_name]:
                del self._listeners[event_name]

    def dispatch(self, event_name, *args, **kwargs):
        # Dispatch the event to all listeners
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                listener(*args, **kwargs)

# Generate a random number between the given range
def get_probability():
    return random.random()