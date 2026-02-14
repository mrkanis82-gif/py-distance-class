from typing import Any


class Distance:
    def __init__(self, distance: int) -> None:
        self.km = distance

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> "Distance":
        if type(other) is int or type(other) is float:
            return Distance(self.km + other)
        else:
            return Distance(self.km + other.km)

    def __iadd__(self, other: Any) -> "Distance":
        if type(other) is int or type(other) is float:
            self.km = self.km + other
            return self
        else:
            self.km = self.km + other.km
            return self

    def __mul__(self, other: Any) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        if type(other) is int or type(other) is float:
            return self.km < other
        else:
            return self.km < other.km

    def __gt__(self, other: Any) -> bool:
        if type(other) is int or type(other) is float:
            return self.km > other
        else:
            return self.km > other.km

    def __eq__(self, other: Any) -> bool:
        if type(other) is int or type(other) is float:
            return self.km == other
        else:
            return self.km == other.km

    def __le__(self, other: Any) -> bool:
        if type(other) is int or type(other) is float:
            return self.km <= other
        else:
            return self.km <= other.km

    def __ge__(self, other: Any) -> bool:
        if type(other) is int or type(other) is float:
            return self.km >= other
        else:
            return self.km >= other.km
