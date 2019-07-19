#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .attachment import Attachment
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period


@dataclass
class CommunicationRequestPayload(BackboneElement):
    """ Message payload.

    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    resource_type: ClassVar[str] = "CommunicationRequestPayload"
    contentAttachment: Attachment = None
    contentReference: FHIRReference = None
    contentString: str = None

    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", Attachment, False, "content", True),
            ("contentReference", "contentReference", FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


@dataclass
class CommunicationRequest(DomainResource):
    """ A request for information to be sent to a receiver.

    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    resource_type: ClassVar[str] = "CommunicationRequest"
    about: Optional[List[FHIRReference]] = empty_list()
    authoredOn: Optional[FHIRDate] = None
    basedOn: Optional[List[FHIRReference]] = empty_list()
    category: Optional[List[CodeableConcept]] = empty_list()
    doNotPerform: Optional[bool] = None
    encounter: Optional[FHIRReference] = None
    groupIdentifier: Optional[Identifier] = None
    identifier: Optional[List[Identifier]] = empty_list()
    medium: Optional[List[CodeableConcept]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    occurrenceDateTime: Optional[FHIRDate] = None
    occurrencePeriod: Optional[Period] = None
    payload: Optional[List[CommunicationRequestPayload]] = empty_list()
    priority: Optional[str] = None
    reasonCode: Optional[List[CodeableConcept]] = empty_list()
    reasonReference: Optional[List[FHIRReference]] = empty_list()
    recipient: Optional[List[FHIRReference]] = empty_list()
    replaces: Optional[List[FHIRReference]] = empty_list()
    requester: Optional[FHIRReference] = None
    sender: Optional[FHIRReference] = None
    status: str = None
    statusReason: Optional[CodeableConcept] = None
    subject: Optional[FHIRReference] = None

    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("about", "about", FHIRReference, True, None, False),
            ("authoredOn", "authoredOn", FHIRDate, False, None, False),
            ("basedOn", "basedOn", FHIRReference, True, None, False),
            ("category", "category", CodeableConcept, True, None, False),
            ("doNotPerform", "doNotPerform", bool, False, None, False),
            ("encounter", "encounter", FHIRReference, False, None, False),
            ("groupIdentifier", "groupIdentifier", Identifier, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("medium", "medium", CodeableConcept, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("occurrenceDateTime", "occurrenceDateTime", FHIRDate, False, "occurrence", False),
            ("occurrencePeriod", "occurrencePeriod", Period, False, "occurrence", False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", str, False, None, False),
            ("reasonCode", "reasonCode", CodeableConcept, True, None, False),
            ("reasonReference", "reasonReference", FHIRReference, True, None, False),
            ("recipient", "recipient", FHIRReference, True, None, False),
            ("replaces", "replaces", FHIRReference, True, None, False),
            ("requester", "requester", FHIRReference, False, None, False),
            ("sender", "sender", FHIRReference, False, None, False),
            ("status", "status", str, False, None, True),
            ("statusReason", "statusReason", CodeableConcept, False, None, False),
            ("subject", "subject", FHIRReference, False, None, False),
        ])
        return js