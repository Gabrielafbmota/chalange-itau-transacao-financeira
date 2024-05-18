from dataclasses import dataclass


@dataclass
class Account:
    number: int
    balance: float = 0.0
