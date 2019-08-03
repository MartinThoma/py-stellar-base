from .stellarxdr import Xdr


class TimeBounds:
    """TimeBounds represents the time interval that a transaction is valid.

    The UNIX timestamp (in seconds), determined by ledger time,
    of a lower and upper bound of when this transaction will be valid.
    If a transaction is submitted too early or too late,
    it will fail to make it into the transaction set.
    **max_time** equal 0 means that it’s not set.

    See `Stellar's documentation on Transactions
    <https://www.stellar.org/developers/guides/concepts/transactions.html#time-bounds>`__
    for more information on how TimeBounds are used within transactions.


    :param min_time: the UNIX timestamp (in seconds)
    :param max_time: the UNIX timestamp (in seconds)
    """

    def __init__(self, min_time: int, max_time: int) -> None:
        if 0 < max_time <= min_time:
            raise ValueError("max_time must be >= min_time.")

        self.min_time = min_time
        self.max_time = max_time

    def to_xdr_object(self) -> Xdr.types.TimeBounds:
        """Returns the xdr object for this TimeBounds object.

        :return: XDR TimeBounds object
        """
        return Xdr.types.TimeBounds(minTime=self.min_time, maxTime=self.max_time)

    @classmethod
    def from_xdr_object(cls, time_bounds_xdr_object: Xdr.types.TimeBounds) -> 'TimeBounds':
        """Create a :class:`TimeBounds` from an XDR TimeBounds object.

        :param time_bounds_xdr_object: The XDR TimeBounds object.
        :return: A new :class:`TimeBounds` object from the given XDR TimeBounds object.
        """
        return cls(min_time=time_bounds_xdr_object.minTime, max_time=time_bounds_xdr_object.maxTime)

    def __eq__(self, other: 'TimeBounds'):
        if not isinstance(other, TimeBounds):
            return False
        return self.min_time == other.min_time and self.max_time == other.max_time
