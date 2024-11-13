import random

class EventDispatcher:
    """
    A simple event dispatcher class that allows objects to listen for events and dispatch them.

    """
    def __init__(self):
        """
            Initialize the event dispatcher.
        """
        # Dictionary to hold event names and their associated listeners
        self._listeners = {}

    def add_listener(self, event_name, listener):
        """
            Add a listener for a specific event.

            Args:
                event_name: str
                    The name of the event.
                listener: function
                    The listener function to be called when the event is dispatched.

            Returns:
                None
        """
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)

    def remove_listener(self, event_name, listener):
        """
            Remove a listener for a specific event.

            Args:
                event_name: str
                    The name of the event.
                listener: function
                    The listener function to be removed.

            Returns:
                None
        """
        if event_name in self._listeners:
            self._listeners[event_name].remove(listener)
            # Clean up if there are no listeners left for the event
            if not self._listeners[event_name]:
                del self._listeners[event_name]

    def dispatch(self, event_name, *args, **kwargs):
        """
            Dispatch an event to all listeners.

            Args:
                event_name: str
                    The name of the event.
                *args: list
                    The arguments to be passed to the listeners.
                **kwargs: dict
                    The keyword arguments to be passed to the listeners.

            Returns:
                None
        """
        # Dispatch the event to all listeners
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                listener(*args, **kwargs)

# Generate a random number between the given range
def get_probability():
    """
        The function is used to generate a random number between 0 and 1.

        Returns:
            random_number: float
                The random number between 0 and 1.
    """
    return random.random()