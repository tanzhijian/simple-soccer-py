from typing import Any


class Telegram:
    """
    This defines a telegram. A telegram is a data structure
    that records information required to dispatch messages.
    Messages are used by game agents to communicate with each other.

    51
    """

    def __init__(
        self,
        sender: int,
        receiver: int,
        msg: int,
        dispatch_time: float,
        *extra_info: Any,
    ) -> None:
        """
        Args:
            sender: the entity that sent this telegram
            receiver: the entity that is to receive this telegram
            msg: the message itself.
                These are all enumerated in the file
            dispatch_time: messages can be dispatched immediately
                or delayed for a specified amount of time.
                If a delay is necessary this field is stamped with the time
                the message should be dispatched.
            extra_info: any additional information that may accompany the message
        """
        self.sender = sender
        self.receiver = receiver
        self.msg = msg
        self.dispatch_time = dispatch_time
        self.extra_info = extra_info
