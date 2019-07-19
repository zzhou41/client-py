#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DataRequirement) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .codeableconcept import CodeableConcept
from .coding import Coding
from .duration import Duration
from .element import Element
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .period import Period


@dataclass
class DataRequirementSort(Element):
    """ Order of the results.

    Specifies the order of the results to be returned.
    """
    resource_type: ClassVar[str] = "DataRequirementSort"
    direction: str = None
    path: str = None

    def elementProperties(self):
        js = super(DataRequirementSort, self).elementProperties()
        js.extend([
            ("direction", "direction", str, False, None, True),
            ("path", "path", str, False, None, True),
        ])
        return js


@dataclass
class DataRequirementDateFilter(Element):
    """ What dates/date ranges are expected.

    Date filters specify additional constraints on the data in terms of the
    applicable date range for specific elements. Each date filter specifies an
    additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementDateFilter"
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueDateTime: Optional[FHIRDate] = None
    valueDuration: Optional[Duration] = None
    valuePeriod: Optional[Period] = None

    def elementProperties(self):
        js = super(DataRequirementDateFilter, self).elementProperties()
        js.extend([
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueDateTime", "valueDateTime", FHIRDate, False, "value", False),
            ("valueDuration", "valueDuration", Duration, False, "value", False),
            ("valuePeriod", "valuePeriod", Period, False, "value", False),
        ])
        return js


@dataclass
class DataRequirementCodeFilter(Element):
    """ What codes are expected.

    Code filters specify additional constraints on the data, specifying the
    value set of interest for a particular element of the data. Each code
    filter defines an additional constraint on the data, i.e. code filters are
    AND'ed, not OR'ed.
    """
    resource_type: ClassVar[str] = "DataRequirementCodeFilter"
    code: Optional[List[Coding]] = empty_list()
    path: Optional[str] = None
    searchParam: Optional[str] = None
    valueSet: Optional[str] = None

    def elementProperties(self):
        js = super(DataRequirementCodeFilter, self).elementProperties()
        js.extend([
            ("code", "code", Coding, True, None, False),
            ("path", "path", str, False, None, False),
            ("searchParam", "searchParam", str, False, None, False),
            ("valueSet", "valueSet", str, False, None, False),
        ])
        return js


@dataclass
class DataRequirement(Element):
    """ Describes a required data item.

    Describes a required data item for evaluation in terms of the type of data,
    and optional code or date-based filters of the data.
    """
    resource_type: ClassVar[str] = "DataRequirement"
    codeFilter: Optional[List[DataRequirementCodeFilter]] = empty_list()
    dateFilter: Optional[List[DataRequirementDateFilter]] = empty_list()
    limit: Optional[int] = None
    mustSupport: Optional[List[str]] = empty_list()
    profile: Optional[List[str]] = empty_list()
    sort: Optional[List[DataRequirementSort]] = empty_list()
    subjectCodeableConcept: Optional[CodeableConcept] = None
    subjectReference: Optional[FHIRReference] = None
    type: str = None

    def elementProperties(self):
        js = super(DataRequirement, self).elementProperties()
        js.extend([
            ("codeFilter", "codeFilter", DataRequirementCodeFilter, True, None, False),
            ("dateFilter", "dateFilter", DataRequirementDateFilter, True, None, False),
            ("limit", "limit", int, False, None, False),
            ("mustSupport", "mustSupport", str, True, None, False),
            ("profile", "profile", str, True, None, False),
            ("sort", "sort", DataRequirementSort, True, None, False),
            ("subjectCodeableConcept", "subjectCodeableConcept", CodeableConcept, False, "subject", False),
            ("subjectReference", "subjectReference", FHIRReference, False, "subject", False),
            ("type", "type", str, False, None, True),
        ])
        return js