#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.1.0-0931132380 (http://hl7.org/fhir/StructureDefinition/AppointmentResponse) on 2019-08-26.
#  2019, SMART Health IT.

import sys
from dataclasses import dataclass, field
from typing import ClassVar, Optional, List
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier


@dataclass
class AppointmentResponse(DomainResource):
    """ A reply to an appointment request for a patient and/or practitioner(s),
    such as a confirmation or rejection.
    """
    resource_type: ClassVar[str] = "AppointmentResponse"

    identifier: Optional[List[Identifier]] = None
    appointment: FHIRReference = None
    start: Optional[FHIRDate] = None
    end: Optional[FHIRDate] = None
    participantType: Optional[List[CodeableConcept]] = None
    actor: Optional[FHIRReference] = None
    participantStatus: str = None
    comment: Optional[str] = None