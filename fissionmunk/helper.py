import random

class EventDispatcher:
    """The class is used to dispatch events to listeners.
    """
    def __init__(self):
        """The constructor of the class.
        """
        # Dictionary to hold event names and their associated listeners
        self._listeners = {}

    def add_listener(self, event_name, listener):
        """The function is used to add a listener for a specific event.

        :param event_name: The name of the event.
        :type event_name: str
        :param listener: The listener function to be added.
        :type listener: function
        :return: None
        :rtype: None
        """

        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(listener)

        return None

    def remove_listener(self, event_name, listener):
        """The function is used to remove a listener for a specific event.

        :param event_name: The name of the event.
        :type event_name: str
        :param listener: The listener function to be removed.
        :type listener: function
        :return: None
        :rtype: None
        """
        if event_name in self._listeners:
            self._listeners[event_name].remove(listener)
            # Clean up if there are no listeners left for the event
            if not self._listeners[event_name]:
                del self._listeners[event_name]

        return None

    def dispatch(self, event_name, *args, **kwargs):
        """The function is used to dispatch an event to all listeners.

        :param event_name: The name of the event.
        :type event_name: str
        :param args: The arguments to be passed to the listeners.
        :type args: tuple
        :param kwargs: The keyword arguments to be passed to the listeners.
        :type kwargs: dict
        :return: None
        :rtype: None
        """
        # Dispatch the event to all listeners
        if event_name in self._listeners:
            for listener in self._listeners[event_name]:
                listener(*args, **kwargs)
        return None
# Generate a random number between the given range
def get_probability():
    """The function is used to generate a random number between 0 and 1.

    :return: A random number between 0 and 1.
    :rtype: float
    """
    return random.random()