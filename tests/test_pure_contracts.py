# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

try:
    import contracts
    have_contracts = True
except ImportError:
    have_contracts = False

import pure_contracts

if have_contracts:
    class IPlant(pure_contracts.ContractInterface):
        @contracts.contract(height=float, returns=float)
        def set_height(self, height):
            return None


    class Plant(IPlant, object):
        def set_height(self, height):
            return height


    class TestPureContracts(unittest.TestCase):
        def test_base_class_is_interface(self):
            with self.assertRaises(TypeError):
                IPlant()

        def test_contracts_honoured(self):
            p = Plant()
            with self.assertRaises(contracts.ContractNotRespected):
                p.set_height('hello')

            self.assertEqual(5.0, p.set_height(5.0))

        def test_content_fails(self):
            with self.assertRaises(pure_contracts.InterfaceError):
                class IAnimal(pure_contracts.ContractInterface):
                    @contracts.contract(volume=int, returns=str)
                    def speak(self, volume):
                        if volume > 0:
                            return 'hello' + '!'*volume
else:
    class TestPureContracts(unittest.TestCase):
        def test_pycontracts_exists(self):
            self.fail('PyContracts not found')
