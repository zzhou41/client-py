#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/BodyStructure) on 2019-07-29.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .attachment import Attachment
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class BodyStructure(DomainResource):
    """ Specific and identified anatomical structure.

    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """
    resource_type: ClassVar[str] = "BodyStructure"
    identifier: Optional[List[Identifier]] = empty_list()
    active: Optional[bool] = None
    morphology: Optional[CodeableConcept] = None
    location: Optional[CodeableConcept] = None
    locationQualifier: Optional[List[CodeableConcept]] = empty_list()
    description: Optional[str] = None
    image: Optional[List[Attachment]] = empty_list()
    patient: FHIRReference = None

    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend([
            ("identifier", "identifier", Identifier, True, None, False),
            ("active", "active", bool, False, None, False),
            ("morphology", "morphology", CodeableConcept, False, None, False),
            ("location", "location", CodeableConcept, False, None, False),
            ("locationQualifier", "locationQualifier", CodeableConcept, True, None, False),
            ("description", "description", str, False, None, False),
            ("image", "image", Attachment, True, None, False),
            ("patient", "patient", FHIRReference, False, None, True),
        ])
        return js