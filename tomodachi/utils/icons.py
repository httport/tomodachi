from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional, DefaultDict
from collections import defaultdict
from discord import Emoji, PartialEmoji

if TYPE_CHECKING:
    StoreItem = Union[Emoji, PartialEmoji]

__all__ = ["i"]


class IconMeta(type):
    def __call__(cls, arg: str) -> Optional[StoreItem]:
        return cls.store[arg.lower()]

    def __getitem__(cls, item: str) -> Optional[StoreItem]:
        return cls.store[item.lower()]

    def __format__(cls, format_spec: str) -> str:
        return f"{cls.store[format_spec.lower()]}"


class i(metaclass=IconMeta):  # noqa
    store: DefaultDict[str, StoreItem] = defaultdict(lambda: PartialEmoji(name="\N{WHITE QUESTION MARK ORNAMENT}"))

    @classmethod
    async def setup(cls, emojis: Iterable[StoreItem]):
        cls.store.clear()

        for e in emojis:
            cls.store[e.name.lower()] = e