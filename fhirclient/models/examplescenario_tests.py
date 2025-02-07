#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-07-29.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import examplescenario
from .fhirdate import FHIRDate


class ExampleScenarioTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ExampleScenario", js["resourceType"])
        return examplescenario.ExampleScenario(js)
    
    def testExampleScenario1(self):
        inst = self.instantiate_from("examplescenario-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ExampleScenario instance")
        self.implExampleScenario1(inst)
        
        js = inst.as_json()
        self.assertEqual("ExampleScenario", js["resourceType"])
        inst2 = examplescenario.ExampleScenario(js)
        self.implExampleScenario1(inst2)
    
    def implExampleScenario1(self, inst):
        self.assertEqual(inst.actor[0].actorId, "Nurse")
        self.assertEqual(inst.actor[0].description, "The Nurse")
        self.assertEqual(inst.actor[0].name, "Nurse")
        self.assertEqual(inst.actor[0].type, "person")
        self.assertEqual(inst.actor[1].actorId, "MAP")
        self.assertEqual(inst.actor[1].description, "The entity that receives the Administration Requests to show the nurse to perform them")
        self.assertEqual(inst.actor[1].name, "Nurse's Tablet")
        self.assertEqual(inst.actor[1].type, "entity")
        self.assertEqual(inst.actor[2].actorId, "OP")
        self.assertEqual(inst.actor[2].description, "The Medication Administration Order Placer")
        self.assertEqual(inst.actor[2].name, "MAR / Scheduler")
        self.assertEqual(inst.actor[2].type, "entity")
        self.assertEqual(inst.actor[3].actorId, "MAC")
        self.assertEqual(inst.actor[3].description, "The entity that receives the Medication Administration reports")
        self.assertEqual(inst.actor[3].name, "MAR / EHR")
        self.assertEqual(inst.actor[3].type, "entity")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.instance[0].description, "The initial prescription which describes \"medication X, 3 times per day\" - the exact scheduling is not   in the initial prescription (it is left for the care teams to decide on the schedule).")
        self.assertEqual(inst.instance[0].name, "Initial Prescription")
        self.assertEqual(inst.instance[0].resourceId, "iherx001")
        self.assertEqual(inst.instance[1].description, "The administration request for day 1, morning")
        self.assertEqual(inst.instance[1].name, "Request for day 1, morning")
        self.assertEqual(inst.instance[1].resourceId, "iherx001.001")
        self.assertEqual(inst.instance[2].description, "The administration request for day 1, lunch")
        self.assertEqual(inst.instance[2].name, "Request for day 1, lunch")
        self.assertEqual(inst.instance[2].resourceId, "iherx001.002")
        self.assertEqual(inst.instance[3].description, "The administration request for day 1, evening")
        self.assertEqual(inst.instance[3].name, "Request for day 1, evening")
        self.assertEqual(inst.instance[3].resourceId, "iherx001.003")
        self.assertEqual(inst.instance[4].description, "The administration request for day 2, morning")
        self.assertEqual(inst.instance[4].name, "Request for day 2, morning")
        self.assertEqual(inst.instance[4].resourceId, "iherx001.004")
        self.assertEqual(inst.instance[5].description, "The administration request for day 2, lunch")
        self.assertEqual(inst.instance[5].name, "Request for day 2, lunch")
        self.assertEqual(inst.instance[5].resourceId, "iherx001.005")
        self.assertEqual(inst.instance[6].description, "The administration request for day 2, evening")
        self.assertEqual(inst.instance[6].name, "Request for day 2, evening")
        self.assertEqual(inst.instance[6].resourceId, "iherx001.006")
        self.assertEqual(inst.instance[7].description, "Administration report for day 1, morning: Taken")
        self.assertEqual(inst.instance[7].name, "Morning meds - taken")
        self.assertEqual(inst.instance[7].resourceId, "iheadm001a")
        self.assertEqual(inst.instance[8].description, "Administration report for day 1, morning: NOT Taken")
        self.assertEqual(inst.instance[8].name, "Morning meds - not taken")
        self.assertEqual(inst.instance[8].resourceId, "iheadm001b")
        self.assertEqual(inst.instance[9].containedInstance[0].resourceId, "iherx001.001")
        self.assertEqual(inst.instance[9].containedInstance[1].resourceId, "iherx001.002")
        self.assertEqual(inst.instance[9].containedInstance[2].resourceId, "iherx001.003")
        self.assertEqual(inst.instance[9].containedInstance[3].resourceId, "iherx001.004")
        self.assertEqual(inst.instance[9].containedInstance[4].resourceId, "iherx001.005")
        self.assertEqual(inst.instance[9].containedInstance[5].resourceId, "iherx001.006")
        self.assertEqual(inst.instance[9].description, "All the medication Requests for Day 1")
        self.assertEqual(inst.instance[9].name, "Bundle of Medication Requests")
        self.assertEqual(inst.instance[9].resourceId, "iherx001bundle")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.process[0].postConditions, "Medication administration Reports are submitted, EHR is updated.")
        self.assertEqual(inst.process[0].preConditions, "Medication administration requests are in the EHR / MAR, scheduled for each individual intake.")
        self.assertEqual(inst.process[0].step[0].operation.initiator, "Nurse")
        self.assertEqual(inst.process[0].step[0].operation.name, "1. Get today's schedule")
        self.assertEqual(inst.process[0].step[0].operation.number, "1")
        self.assertEqual(inst.process[0].step[0].operation.receiver, "MAP")
        self.assertEqual(inst.process[0].step[1].process[0].description, "Query for medication administration orders,\\n- For today's shifts\\n- For today's patients")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.initiator, "MAP")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.name, "2.Query for medication administration orders,\\n- For today's shifts\\n- For today's patients")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.number, "2")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.receiver, "OP")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.request.resourceId, "iherxqry")
        self.assertEqual(inst.process[0].step[1].process[0].step[0].operation.response.resourceId, "iherx001bundle")
        self.assertEqual(inst.process[0].step[1].process[0].title, "P1. Query Administration Requests")
        self.assertTrue(inst.process[0].step[2].pause)
        self.assertEqual(inst.process[0].step[3].operation.initiator, "MAP")
        self.assertEqual(inst.process[0].step[3].operation.name, "Notify (alert)")
        self.assertEqual(inst.process[0].step[3].operation.number, "4")
        self.assertEqual(inst.process[0].step[3].operation.receiver, "Nurse")
        self.assertEqual(inst.process[0].step[4].operation.initiator, "Nurse")
        self.assertEqual(inst.process[0].step[4].operation.name, "Read orders")
        self.assertEqual(inst.process[0].step[4].operation.number, "5")
        self.assertEqual(inst.process[0].step[4].operation.receiver, "MAP")
        self.assertTrue(inst.process[0].step[5].pause)
        self.assertEqual(inst.process[0].step[6].operation.initiator, "Nurse")
        self.assertEqual(inst.process[0].step[6].operation.name, "Ask if patient took meds")
        self.assertEqual(inst.process[0].step[6].operation.number, "5")
        self.assertEqual(inst.process[0].step[6].operation.receiver, "Nurse")
        self.assertEqual(inst.process[0].step[7].alternative[0].description, "Invoke if patient took medications")
        self.assertEqual(inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.initiator, "Nurse")
        self.assertTrue(inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.initiatorActive)
        self.assertEqual(inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.name, "Register Meds taken")
        self.assertEqual(inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.number, "1a")
        self.assertEqual(inst.process[0].step[7].alternative[0].step[0].process[0].step[0].operation.receiver, "MAP")
        self.assertEqual(inst.process[0].step[7].alternative[0].step[0].process[0].title, "Register Meds taken")
        self.assertEqual(inst.process[0].step[7].alternative[0].title, "Patient took drugs")
        self.assertEqual(inst.process[0].step[7].alternative[1].description, "No, patient did not take drugs")
        self.assertEqual(inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.initiator, "Nurse")
        self.assertTrue(inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.initiatorActive)
        self.assertEqual(inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.name, "Register Meds NOT taken")
        self.assertEqual(inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.number, "1b")
        self.assertEqual(inst.process[0].step[7].alternative[1].step[0].process[0].step[0].operation.receiver, "MAP")
        self.assertEqual(inst.process[0].step[7].alternative[1].step[0].process[0].title, "Register Meds NOT taken")
        self.assertEqual(inst.process[0].step[7].alternative[1].title, "No drugs")
        self.assertEqual(inst.process[0].step[7].alternative[2].description, "Unknown whether patient took medications or not")
        self.assertTrue(inst.process[0].step[7].alternative[2].step[0].pause)
        self.assertEqual(inst.process[0].step[7].alternative[2].title, "Not clear")
        self.assertTrue(inst.process[0].step[8].pause)
        self.assertEqual(inst.process[0].step[9].operation.initiator, "Nurse")
        self.assertEqual(inst.process[0].step[9].operation.name, "Administer drug")
        self.assertEqual(inst.process[0].step[9].operation.number, "6")
        self.assertEqual(inst.process[0].step[9].operation.receiver, "Nurse")
        self.assertEqual(inst.process[0].title, "Mobile Medication Administration")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")

