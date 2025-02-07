#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition) on 2019-07-29.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .money import Money
from .period import Period
from .usagecontext import UsageContext


@dataclass
class ChargeItemDefinitionPropertyGroupPriceComponent(BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice of how the prices have been calculated.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroupPriceComponent"
    type: str = None
    code: Optional[CodeableConcept] = None
    factor: Optional[float] = None
    amount: Optional[Money] = None

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroupPriceComponent, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("code", "code", CodeableConcept, False, None, False),
            ("factor", "factor", float, False, None, False),
            ("amount", "amount", Money, False, None, False),
        ])
        return js


@dataclass
class ChargeItemDefinitionApplicability(BackboneElement):
    """ Whether or not the billing code is applicable.

    Expressions that describe applicability criteria for the billing code.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionApplicability"
    description: Optional[str] = None
    language: Optional[str] = None
    expression: Optional[str] = None

    def elementProperties(self):
        js = super(ChargeItemDefinitionApplicability, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("language", "language", str, False, None, False),
            ("expression", "expression", str, False, None, False),
        ])
        return js


@dataclass
class ChargeItemDefinitionPropertyGroup(BackboneElement):
    """ Group of properties which are applicable under the same conditions.

    Group of properties which are applicable under the same conditions. If no
    applicability rules are established for the group, then all properties
    always apply.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinitionPropertyGroup"
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = empty_list()
    priceComponent: Optional[List[ChargeItemDefinitionPropertyGroupPriceComponent]] = empty_list()

    def elementProperties(self):
        js = super(ChargeItemDefinitionPropertyGroup, self).elementProperties()
        js.extend([
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("priceComponent", "priceComponent", ChargeItemDefinitionPropertyGroupPriceComponent, True, None, False),
        ])
        return js


@dataclass
class ChargeItemDefinition(DomainResource):
    """ Definition of properties and rules about how the price and the
    applicability of a ChargeItem can be determined.

    The ChargeItemDefinition resource provides the properties that apply to the
    (billing) codes necessary to calculate costs and prices. The properties may
    differ largely depending on type and realm, therefore this resource gives
    only a rough structure and requires profiling for each type of billing code
    system.
    """
    resource_type: ClassVar[str] = "ChargeItemDefinition"
    url: str = None
    identifier: Optional[List[Identifier]] = empty_list()
    version: Optional[str] = None
    title: Optional[str] = None
    derivedFromUri: Optional[List[str]] = empty_list()
    partOf: Optional[List[str]] = empty_list()
    replaces: Optional[List[str]] = empty_list()
    status: str = None
    experimental: Optional[bool] = None
    date: Optional[FHIRDate] = None
    publisher: Optional[str] = None
    contact: Optional[List[ContactDetail]] = empty_list()
    description: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    copyright: Optional[str] = None
    approvalDate: Optional[FHIRDate] = None
    lastReviewDate: Optional[FHIRDate] = None
    effectivePeriod: Optional[Period] = None
    code: Optional[CodeableConcept] = None
    instance: Optional[List[FHIRReference]] = empty_list()
    applicability: Optional[List[ChargeItemDefinitionApplicability]] = empty_list()
    propertyGroup: Optional[List[ChargeItemDefinitionPropertyGroup]] = empty_list()

    def elementProperties(self):
        js = super(ChargeItemDefinition, self).elementProperties()
        js.extend([
            ("url", "url", str, False, None, True),
            ("identifier", "identifier", Identifier, True, None, False),
            ("version", "version", str, False, None, False),
            ("title", "title", str, False, None, False),
            ("derivedFromUri", "derivedFromUri", str, True, None, False),
            ("partOf", "partOf", str, True, None, False),
            ("replaces", "replaces", str, True, None, False),
            ("status", "status", str, False, None, True),
            ("experimental", "experimental", bool, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("description", "description", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("code", "code", CodeableConcept, False, None, False),
            ("instance", "instance", FHIRReference, True, None, False),
            ("applicability", "applicability", ChargeItemDefinitionApplicability, True, None, False),
            ("propertyGroup", "propertyGroup", ChargeItemDefinitionPropertyGroup, True, None, False),
        ])
        return js