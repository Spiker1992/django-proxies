from dataclasses import dataclass


@dataclass
class Empty:
    ...

@dataclass
class PostCreated:
    title: str

@dataclass
class PostUpdated:
    content: str
    title: str