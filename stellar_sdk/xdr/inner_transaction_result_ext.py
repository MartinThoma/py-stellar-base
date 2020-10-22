# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from xdrlib import Packer, Unpacker

from .base import *

__all__ = ["InnerTransactionResultExt"]


class InnerTransactionResultExt:
    """
    XDR Source Code
    ----------------------------------------------------------------
    union switch (int v)
        {
        case 0:
            void;
        }
    ----------------------------------------------------------------
    """

    def __init__(self, v: int,) -> None:
        self.v = v

    def pack(self, packer: Packer) -> None:
        Integer(self.v).pack(packer)
        if self.v == 0:
            return

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "InnerTransactionResultExt":
        v = Integer.unpack(unpacker)
        if v == 0:
            return cls(v)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "InnerTransactionResultExt":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "InnerTransactionResultExt":
        xdr = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.v == other.v

    def __str__(self):
        out = []
        out.append(f"v={self.v}")
        return f"<InnerTransactionResultExt {[', '.join(out)]}>"