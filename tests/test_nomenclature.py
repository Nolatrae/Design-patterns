import pytest
from src.contracts.implements.nomenclature import Nomenclature

def test_other_uuid_for_instances():
    n1 = Nomenclature()
    n2 = Nomenclature()
    assert n1.uuid != n2.uuid

def test_base_equals_different_names():
    n1 = Nomenclature("one")
    n2 = Nomenclature("two")
    assert n1 != n2

def test_base_equals_same_names():
    n1 = Nomenclature("one")
    n2 = Nomenclature("one")
    assert n1 == n2
