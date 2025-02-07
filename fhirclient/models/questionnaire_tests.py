#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-07-29.
#  2019, SMART Health IT.


import os
import io
import unittest
import json
from . import questionnaire
from .fhirdate import FHIRDate


class QuestionnaireTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Questionnaire", js["resourceType"])
        return questionnaire.Questionnaire(js)
    
    def testQuestionnaire1(self):
        inst = self.instantiate_from("questionnaire-cqf-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire1(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire1(inst2)
    
    def implQuestionnaire1(self, inst):
        self.assertEqual(inst.code[0].code, "44249-1")
        self.assertEqual(inst.code[0].display, "PHQ-9 quick depression assessment panel:-:Pt:^Patient:-:Report.PHQ-9")
        self.assertEqual(inst.code[0].system, "http://loinc.org")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/cqf-library")
        self.assertEqual(inst.extension[0].valueCanonical, "Library/phq-9-logic")
        self.assertEqual(inst.id, "phq-9-questionnaire")
        self.assertEqual(inst.identifier[0].use, "official")
        self.assertEqual(inst.identifier[0].value, "phq-9")
        self.assertEqual(inst.item[0].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[0].code[0].code, "44250-9")
        self.assertEqual(inst.item[0].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].linkId, "LittleInterest")
        self.assertTrue(inst.item[0].required)
        self.assertEqual(inst.item[0].text, "Little interest or pleasure in doing things")
        self.assertEqual(inst.item[0].type, "choice")
        self.assertEqual(inst.item[1].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[1].code[0].code, "44255-8")
        self.assertEqual(inst.item[1].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[1].linkId, "FeelingDown")
        self.assertTrue(inst.item[1].required)
        self.assertEqual(inst.item[1].text, "Feeling down, depressed, or hopeless")
        self.assertEqual(inst.item[1].type, "choice")
        self.assertEqual(inst.item[2].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[2].code[0].code, "44259-0")
        self.assertEqual(inst.item[2].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[2].linkId, "TroubleSleeping")
        self.assertTrue(inst.item[2].required)
        self.assertEqual(inst.item[2].text, "Trouble falling or staying asleep")
        self.assertEqual(inst.item[2].type, "choice")
        self.assertEqual(inst.item[3].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[3].code[0].code, "44254-1")
        self.assertEqual(inst.item[3].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[3].linkId, "FeelingTired")
        self.assertTrue(inst.item[3].required)
        self.assertEqual(inst.item[3].text, "Feeling tired or having little energy")
        self.assertEqual(inst.item[3].type, "choice")
        self.assertEqual(inst.item[4].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[4].code[0].code, "44251-7")
        self.assertEqual(inst.item[4].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[4].linkId, "BadAppetite")
        self.assertTrue(inst.item[4].required)
        self.assertEqual(inst.item[4].text, "Poor appetite or overeating")
        self.assertEqual(inst.item[4].type, "choice")
        self.assertEqual(inst.item[5].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[5].code[0].code, "44258-2")
        self.assertEqual(inst.item[5].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[5].linkId, "FeelingBadAboutSelf")
        self.assertTrue(inst.item[5].required)
        self.assertEqual(inst.item[5].text, "Feeling bad about yourself - or that you are a failure or have let yourself or your family down")
        self.assertEqual(inst.item[5].type, "choice")
        self.assertEqual(inst.item[6].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[6].code[0].code, "44252-5")
        self.assertEqual(inst.item[6].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[6].linkId, "TroubleConcentrating")
        self.assertTrue(inst.item[6].required)
        self.assertEqual(inst.item[6].text, "Trouble concentrating on things, such as reading the newspaper or watching television")
        self.assertEqual(inst.item[6].type, "choice")
        self.assertEqual(inst.item[7].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[7].code[0].code, "44253-3")
        self.assertEqual(inst.item[7].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[7].linkId, "MovingSpeaking")
        self.assertTrue(inst.item[7].required)
        self.assertEqual(inst.item[7].text, "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual")
        self.assertEqual(inst.item[7].type, "choice")
        self.assertEqual(inst.item[8].code[0].code, "44261-6")
        self.assertEqual(inst.item[8].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[8].extension[0].url, "http://hl7.org/fhir/StructureDefinition/cqf-expression")
        self.assertEqual(inst.item[8].extension[0].valueExpression.expression, "CalculateTotalScore")
        self.assertEqual(inst.item[8].extension[0].valueExpression.language, "text/cql")
        self.assertEqual(inst.item[8].linkId, "TotalScore")
        self.assertTrue(inst.item[8].required)
        self.assertEqual(inst.item[8].text, "Total score")
        self.assertEqual(inst.item[8].type, "integer")
        self.assertEqual(inst.item[9].answerValueSet, "http://loinc.org/vs/LL358-3")
        self.assertEqual(inst.item[9].code[0].code, "44256-6")
        self.assertEqual(inst.item[9].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[9].linkId, "Difficulty")
        self.assertTrue(inst.item[9].required)
        self.assertEqual(inst.item[9].text, "If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people")
        self.assertEqual(inst.item[9].type, "choice")
        self.assertEqual(inst.meta.profile[0], "http://hl7.org/fhir/StructureDefinition/cqf-questionnaire")
        self.assertEqual(inst.meta.tag[0].code, "HTEST")
        self.assertEqual(inst.meta.tag[0].display, "test health data")
        self.assertEqual(inst.meta.tag[0].system, "http://terminology.hl7.org/CodeSystem/v3-ActReason")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">PHQ-9 Questionnaire with dynamic logic</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Patient Health Questionnaire (PHQ-9)")
        self.assertEqual(inst.version, "1.0.0")
    
    def testQuestionnaire2(self):
        inst = self.instantiate_from("questionnaire-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire2(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire2(inst2)
    
    def implQuestionnaire2(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2012-01").date)
        self.assertEqual(inst.date.as_json(), "2012-01")
        self.assertEqual(inst.id, "3141")
        self.assertEqual(inst.item[0].code[0].code, "COMORBIDITY")
        self.assertEqual(inst.item[0].code[0].system, "http://example.org/system/code/sections")
        self.assertEqual(inst.item[0].item[0].answerValueSet, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.item[0].item[0].code[0].code, "COMORB")
        self.assertEqual(inst.item[0].item[0].code[0].system, "http://example.org/system/code/questions")
        self.assertEqual(inst.item[0].item[0].item[0].code[0].code, "CARDIAL")
        self.assertEqual(inst.item[0].item[0].item[0].code[0].system, "http://example.org/system/code/sections")
        self.assertEqual(inst.item[0].item[0].item[0].enableWhen[0].answerCoding.code, "Y")
        self.assertEqual(inst.item[0].item[0].item[0].enableWhen[0].answerCoding.system, "http://terminology.hl7.org/CodeSystem/v2-0136")
        self.assertEqual(inst.item[0].item[0].item[0].enableWhen[0].operator, "=")
        self.assertEqual(inst.item[0].item[0].item[0].enableWhen[0].question, "1.1")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].answerValueSet, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].code[0].code, "COMORBCAR")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].code[0].system, "http://example.org/system/code/questions")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].answerValueSet, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[0].code, "COMCAR00")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[0].display, "Angina Pectoris")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[0].system, "http://example.org/system/code/questions")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[1].code, "194828000")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[1].display, "Angina (disorder)")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].code[1].system, "http://snomed.info/sct")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].linkId, "1.1.1.1.1")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].prefix, "1.1.1")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[0].type, "choice")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].answerValueSet, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].code[0].code, "22298006")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].code[0].display, "Myocardial infarction (disorder)")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].code[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].linkId, "1.1.1.1.2")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].prefix, "1.1.2")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].item[1].type, "choice")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].linkId, "1.1.1.1")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].prefix, "1.1")
        self.assertEqual(inst.item[0].item[0].item[0].item[0].type, "choice")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].answerValueSet, "http://hl7.org/fhir/ValueSet/yesnodontknow")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].code[0].code, "COMORBVAS")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].code[0].system, "http://example.org/system/code/questions")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].linkId, "1.1.1.2")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].prefix, "1.2")
        self.assertEqual(inst.item[0].item[0].item[0].item[1].type, "choice")
        self.assertEqual(inst.item[0].item[0].item[0].linkId, "1.1.1")
        self.assertEqual(inst.item[0].item[0].item[0].type, "group")
        self.assertEqual(inst.item[0].item[0].linkId, "1.1")
        self.assertEqual(inst.item[0].item[0].prefix, "1")
        self.assertEqual(inst.item[0].item[0].type, "choice")
        self.assertEqual(inst.item[0].linkId, "1")
        self.assertEqual(inst.item[0].type, "group")
        self.assertEqual(inst.item[1].code[0].code, "HISTOPATHOLOGY")
        self.assertEqual(inst.item[1].code[0].system, "http://example.org/system/code/sections")
        self.assertEqual(inst.item[1].item[0].code[0].code, "ABDOMINAL")
        self.assertEqual(inst.item[1].item[0].code[0].system, "http://example.org/system/code/sections")
        self.assertEqual(inst.item[1].item[0].item[0].code[0].code, "STADPT")
        self.assertEqual(inst.item[1].item[0].item[0].code[0].display, "pT category")
        self.assertEqual(inst.item[1].item[0].item[0].code[0].system, "http://example.org/system/code/questions")
        self.assertEqual(inst.item[1].item[0].item[0].linkId, "2.1.2")
        self.assertEqual(inst.item[1].item[0].item[0].type, "choice")
        self.assertEqual(inst.item[1].item[0].linkId, "2.1")
        self.assertEqual(inst.item[1].item[0].type, "group")
        self.assertEqual(inst.item[1].linkId, "2")
        self.assertEqual(inst.item[1].type, "group")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Cancer Quality Forum Questionnaire 2012")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Questionnaire/3141")
    
    def testQuestionnaire3(self):
        inst = self.instantiate_from("questionnaire-example-f201-lifelines.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire3(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire3(inst2)
    
    def implQuestionnaire3(self, inst):
        self.assertEqual(inst.code[0].code, "VL 1-1, 18-65_1.2.2")
        self.assertEqual(inst.code[0].display, "Lifelines Questionnaire 1 part 1")
        self.assertEqual(inst.code[0].system, "http://example.org/system/code/lifelines/nl")
        self.assertEqual(inst.date.date, FHIRDate("2010").date)
        self.assertEqual(inst.date.as_json(), "2010")
        self.assertEqual(inst.id, "f201")
        self.assertEqual(inst.item[0].linkId, "1")
        self.assertEqual(inst.item[0].text, "Do you have allergies?")
        self.assertEqual(inst.item[0].type, "boolean")
        self.assertEqual(inst.item[1].item[0].linkId, "2.1")
        self.assertEqual(inst.item[1].item[0].text, "What is your gender?")
        self.assertEqual(inst.item[1].item[0].type, "string")
        self.assertEqual(inst.item[1].item[1].linkId, "2.2")
        self.assertEqual(inst.item[1].item[1].text, "What is your date of birth?")
        self.assertEqual(inst.item[1].item[1].type, "date")
        self.assertEqual(inst.item[1].item[2].linkId, "2.3")
        self.assertEqual(inst.item[1].item[2].text, "What is your country of birth?")
        self.assertEqual(inst.item[1].item[2].type, "string")
        self.assertEqual(inst.item[1].item[3].linkId, "2.4")
        self.assertEqual(inst.item[1].item[3].text, "What is your marital status?")
        self.assertEqual(inst.item[1].item[3].type, "string")
        self.assertEqual(inst.item[1].linkId, "2")
        self.assertEqual(inst.item[1].text, "General questions")
        self.assertEqual(inst.item[1].type, "group")
        self.assertEqual(inst.item[2].item[0].linkId, "3.1")
        self.assertEqual(inst.item[2].item[0].text, "Do you smoke?")
        self.assertEqual(inst.item[2].item[0].type, "boolean")
        self.assertEqual(inst.item[2].item[1].linkId, "3.2")
        self.assertEqual(inst.item[2].item[1].text, "Do you drink alchohol?")
        self.assertEqual(inst.item[2].item[1].type, "boolean")
        self.assertEqual(inst.item[2].linkId, "3")
        self.assertEqual(inst.item[2].text, "Intoxications")
        self.assertEqual(inst.item[2].type, "group")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Questionnaire/f201")
    
    def testQuestionnaire4(self):
        inst = self.instantiate_from("questionnaire-example-gcs.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire4(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire4(inst2)
    
    def implQuestionnaire4(self, inst):
        self.assertEqual(inst.code[0].code, "9269-2")
        self.assertEqual(inst.code[0].system, "http://loinc.org")
        self.assertEqual(inst.contained[0].id, "motor")
        self.assertEqual(inst.contained[1].id, "verbal")
        self.assertEqual(inst.contained[2].id, "eye")
        self.assertEqual(inst.date.date, FHIRDate("2015-08-03").date)
        self.assertEqual(inst.date.as_json(), "2015-08-03")
        self.assertEqual(inst.id, "gcs")
        self.assertEqual(inst.item[0].answerValueSet, "#verbal")
        self.assertEqual(inst.item[0].code[0].code, "9270-0")
        self.assertEqual(inst.item[0].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[0].linkId, "1.1")
        self.assertEqual(inst.item[0].type, "choice")
        self.assertEqual(inst.item[1].answerValueSet, "#motor")
        self.assertEqual(inst.item[1].code[0].code, "9268-4")
        self.assertEqual(inst.item[1].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[1].linkId, "1.2")
        self.assertEqual(inst.item[1].type, "choice")
        self.assertEqual(inst.item[2].answerValueSet, "#eye")
        self.assertEqual(inst.item[2].code[0].code, "9267-6")
        self.assertEqual(inst.item[2].code[0].system, "http://loinc.org")
        self.assertEqual(inst.item[2].linkId, "1.3")
        self.assertEqual(inst.item[2].type, "choice")
        self.assertEqual(inst.publisher, "FHIR Project team")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "Glasgow Coma Score")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Questionnaire/gcs")
    
    def testQuestionnaire5(self):
        inst = self.instantiate_from("questionnaire-example-bluebook.json")
        self.assertIsNotNone(inst, "Must have instantiated a Questionnaire instance")
        self.implQuestionnaire5(inst)
        
        js = inst.as_json()
        self.assertEqual("Questionnaire", js["resourceType"])
        inst2 = questionnaire.Questionnaire(js)
        self.implQuestionnaire5(inst2)
    
    def implQuestionnaire5(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2013-02-19").date)
        self.assertEqual(inst.date.as_json(), "2013-02-19")
        self.assertEqual(inst.id, "bb")
        self.assertEqual(inst.item[0].item[0].item[0].linkId, "nameOfChild")
        self.assertEqual(inst.item[0].item[0].item[0].text, "Name of child")
        self.assertEqual(inst.item[0].item[0].item[0].type, "string")
        self.assertEqual(inst.item[0].item[0].item[1].answerOption[0].valueCoding.code, "F")
        self.assertEqual(inst.item[0].item[0].item[1].answerOption[1].valueCoding.code, "M")
        self.assertEqual(inst.item[0].item[0].item[1].linkId, "sex")
        self.assertEqual(inst.item[0].item[0].item[1].text, "Sex")
        self.assertEqual(inst.item[0].item[0].item[1].type, "choice")
        self.assertEqual(inst.item[0].item[0].linkId, "group")
        self.assertEqual(inst.item[0].item[0].type, "group")
        self.assertEqual(inst.item[0].item[1].item[0].linkId, "birthWeight")
        self.assertEqual(inst.item[0].item[1].item[0].text, "Birth weight (kg)")
        self.assertEqual(inst.item[0].item[1].item[0].type, "decimal")
        self.assertEqual(inst.item[0].item[1].item[1].linkId, "birthLength")
        self.assertEqual(inst.item[0].item[1].item[1].text, "Birth length (cm)")
        self.assertEqual(inst.item[0].item[1].item[1].type, "decimal")
        self.assertEqual(inst.item[0].item[1].item[2].answerOption[0].valueCoding.code, "INJECTION")
        self.assertEqual(inst.item[0].item[1].item[2].answerOption[1].valueCoding.code, "INTRAVENOUS")
        self.assertEqual(inst.item[0].item[1].item[2].answerOption[2].valueCoding.code, "ORAL")
        self.assertTrue(inst.item[0].item[1].item[2].item[0].enableWhen[0].answerBoolean)
        self.assertEqual(inst.item[0].item[1].item[2].item[0].enableWhen[0].operator, "exists")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].enableWhen[0].question, "vitaminKgiven")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[0].linkId, "vitaminiKDose1")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[0].text, "1st dose")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[0].type, "dateTime")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[1].linkId, "vitaminiKDose2")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[1].text, "2nd dose")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].item[1].type, "dateTime")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].linkId, "vitaminKgivenDoses")
        self.assertEqual(inst.item[0].item[1].item[2].item[0].type, "group")
        self.assertEqual(inst.item[0].item[1].item[2].linkId, "vitaminKgiven")
        self.assertEqual(inst.item[0].item[1].item[2].text, "Vitamin K given")
        self.assertEqual(inst.item[0].item[1].item[2].type, "choice")
        self.assertEqual(inst.item[0].item[1].item[3].item[0].linkId, "hepBgivenDate")
        self.assertEqual(inst.item[0].item[1].item[3].item[0].text, "Date given")
        self.assertEqual(inst.item[0].item[1].item[3].item[0].type, "date")
        self.assertEqual(inst.item[0].item[1].item[3].linkId, "hepBgiven")
        self.assertEqual(inst.item[0].item[1].item[3].text, "Hep B given y / n")
        self.assertEqual(inst.item[0].item[1].item[3].type, "boolean")
        self.assertEqual(inst.item[0].item[1].item[4].linkId, "abnormalitiesAtBirth")
        self.assertEqual(inst.item[0].item[1].item[4].text, "Abnormalities noted at birth")
        self.assertEqual(inst.item[0].item[1].item[4].type, "string")
        self.assertEqual(inst.item[0].item[1].linkId, "neonatalInformation")
        self.assertEqual(inst.item[0].item[1].text, "Neonatal Information")
        self.assertEqual(inst.item[0].item[1].type, "group")
        self.assertEqual(inst.item[0].linkId, "birthDetails")
        self.assertEqual(inst.item[0].text, "Birth details - To be completed by health professional")
        self.assertEqual(inst.item[0].type, "group")
        self.assertEqual(inst.jurisdiction[0].coding[0].code, "AU")
        self.assertEqual(inst.jurisdiction[0].coding[0].system, "urn:iso:std:iso:3166")
        self.assertEqual(inst.publisher, "New South Wales Department of Health")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.subjectType[0], "Patient")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.title, "NSW Government My Personal Health Record")
        self.assertEqual(inst.url, "http://hl7.org/fhir/Questionnaire/bb")

