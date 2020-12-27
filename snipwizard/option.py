#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Any

from snipwizard.singleton import Singleton


class Option:
    """
    A python class that provides similar functionalities as the Option/Option class
    in scala. It's very useful in some cases to avoid the "check null" boilerplates.

    An example:
    Assuming you want to read from a nested json dict and some expected keys may not exist.
    instead of doing the `is in` check, you can write directly as follows:
    ```python
    d = {
        "person": {
            "name": "sam",
            "age": 20,
        },
        "company": {
            "name": "veepee",
        }
    }
    d = Option(d)
    print(f'd["address"]: {d["address"]}')
    print(f'd["person"]["name"]: {d["person"]["name"]}')
    print(f'd["person"]["role"]: {d["person"]["role"]}')
    print(f'd["person"]["age"].getOrElse(0): {d["person"]["age"].getOrElse(20)}'))

    """
    def __init__(self, var: Any) -> None:
        self._var = var

    def __getattr__(self, name: str) -> Option:
        if self._var is None:
            return Nothing()
        try:
            return Option(getattr(self._var, name))
        except Exception:
            return Nothing()

    def __call__(self, *args, **kwargs) -> Option:
        if self._var is None:
            return Nothing()
        try:
            return Option(self._var(*args, **kwargs))
        except Exception:
            return Nothing()

    def __getitem__(self, key) -> Option:
        if self._var is None:
            return Nothing()
        try:
            return Option(self._var[key])
        except Exception:
            return Nothing()

    def getOrElse(self, default: Any) -> Any:
        if self._var is None:
            return default
        return self._var

    def map(self, func) -> Option:
        if self._var is None:
            return Nothing()
        try:
            return Option(func(self._var))
        except Exception:
            return Nothing()

    def __expr__(self) ->str :
        return "Option({})".format(str(self._var))

    def __str__(self) -> str:
        return "Option({})".format(str(self._var))

    def __format__(self, specs) -> str:
        return str(self)

    def __eq__(self, op: Option) -> bool:
        if id(op) == id(Nothing()) and id(self) == id(Nothing()):
            return True
        elif id(op) == id(Nothing()) or id(self) == id(Nothing()):
            return False
        else:
            return self._obj == op._obj


class Nothing(Option, metaclass=Singleton):
    def __init__(self) -> None:
        super().__init__(None)
