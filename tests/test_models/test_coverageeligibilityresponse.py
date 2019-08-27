#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 on 2019-08-26.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from fhirclient.models import coverageeligibilityresponse
from fhirclient.models.fhirdate import FHIRDate


class CoverageEligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or \
                  os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'fhir-parser', 'downloads'))
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        return coverageeligibilityresponse.CoverageEligibilityResponse(js)
    
    def testCoverageEligibilityResponse1(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse1(inst2)
    
    def implCoverageEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse2(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse2(inst2)
    
    def implCoverageEligibilityResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Eligibiliy request could not be processed, please address errors before submitting.")
        self.assertEqual(inst.error[0].code.coding[0].code, "a001")
        self.assertEqual(inst.error[0].code.coding[0].system, "http://terminology.hl7.org/CodeSystem/adjudication-error")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2503")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812343")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "error")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse3(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-benefits-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse3(inst2)
    
    def implCoverageEligibilityResponse3(self, inst):
        self.assertEqual(inst.contained[0].id, "coverage-1")
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2502")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812342")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].usedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].usedMoney.value, 3748.0)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].item[0].benefit[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].item[1].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.currency, "USD")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].item[2].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[3].description, "Vision products and services such as exams, glasses and contact lenses.")
        self.assertTrue(inst.insurance[0].item[3].excluded)
        self.assertEqual(inst.insurance[0].item[3].name, "Vision")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.purpose[1], "benefits")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testCoverageEligibilityResponse4(self):
        inst = self.instantiate_from("coverageeligibilityresponse-example-benefits.json")
        self.assertIsNotNone(inst, "Must have instantiated a CoverageEligibilityResponse instance")
        self.implCoverageEligibilityResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("CoverageEligibilityResponse", js["resourceType"])
        inst2 = coverageeligibilityresponse.CoverageEligibilityResponse(js)
        self.implCoverageEligibilityResponse4(inst2)
    
    def implCoverageEligibilityResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2501")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/coverageeligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.insurance[0].inforce)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[0].benefit[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].item[0].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[0].benefit[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].item[0].benefit[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].item[0].benefit[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].item[0].benefit[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].item[0].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[0].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[0].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[0].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[1].benefit[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].item[1].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].item[1].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[1].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[1].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[1].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[2].benefit[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].item[2].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].item[2].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[2].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[2].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[2].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[3].benefit[0].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[3].benefit[0].allowedMoney.value, 400)
        self.assertEqual(inst.insurance[0].item[3].benefit[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].item[3].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[3].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[3].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[3].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].item[3].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[3].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[3].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.insurance[0].item[4].benefit[0].allowedString, "shared")
        self.assertEqual(inst.insurance[0].item[4].benefit[0].type.coding[0].code, "room")
        self.assertEqual(inst.insurance[0].item[4].benefit[1].allowedMoney.currency, "SAR")
        self.assertEqual(inst.insurance[0].item[4].benefit[1].allowedMoney.value, 600)
        self.assertEqual(inst.insurance[0].item[4].benefit[1].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].code, "49")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].display, "Hospital Room and Board")
        self.assertEqual(inst.insurance[0].item[4].category.coding[0].system, "http://terminology.hl7.org/CodeSystem/ex-benefitcategory")
        self.assertEqual(inst.insurance[0].item[4].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].item[4].network.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-network")
        self.assertEqual(inst.insurance[0].item[4].term.coding[0].code, "day")
        self.assertEqual(inst.insurance[0].item[4].term.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-term")
        self.assertEqual(inst.insurance[0].item[4].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].item[4].unit.coding[0].system, "http://terminology.hl7.org/CodeSystem/benefit-unit")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.outcome, "complete")
        self.assertEqual(inst.purpose[0], "validation")
        self.assertEqual(inst.purpose[1], "benefits")
        self.assertEqual(inst.servicedDate.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.servicedDate.as_json(), "2014-09-17")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the CoverageEligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")

if __name__ == '__main__':
    unittest.main()