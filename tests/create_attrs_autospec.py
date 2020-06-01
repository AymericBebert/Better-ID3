from typing import Any, Type
from unittest.mock import create_autospec

_ATTRS_ATTRIBUTE = "__attrs_attrs__"


def create_attrs_autospec(spec: Type, spec_set: bool = True) -> Any:
    """Creates a mock of an attr class (creates mocks recursively on all attributes).

    :param spec: the spec to mock
    :param spec_set: if True, AttributeError will be raised if an attribute that is not in the spec is set.
    """

    if not hasattr(spec, _ATTRS_ATTRIBUTE):
        raise TypeError(f"{spec!r} is not an attrs class")
    mock = create_autospec(spec, spec_set=spec_set)
    for attribute in getattr(spec, _ATTRS_ATTRIBUTE):
        if hasattr(attribute.type, _ATTRS_ATTRIBUTE):
            mock_attribute = create_attrs_autospec(attribute.type, spec_set)
        else:
            mock_attribute = create_autospec(attribute.type, spec_set=spec_set)
        object.__setattr__(mock, attribute.name, mock_attribute)
    return mock
