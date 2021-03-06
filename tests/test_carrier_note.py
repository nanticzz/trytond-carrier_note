# This file is part of the carrier_note module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CarrierNoteTestCase(ModuleTestCase):
    'Test Carrier Note module'
    module = 'carrier_note'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CarrierNoteTestCase))
    return suite