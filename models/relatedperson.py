#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RelatedPerson) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


from . import domainresource

@dataclass
class RelatedPerson(domainresource.DomainResource):
    """ A person that is related to a patient, but who is not a direct target of
    care.

    Information about a person that is involved in the care for a patient, but
    who is not the target of healthcare, nor has a formal responsibility in the
    care process.
    """
    resource_type: ClassVar[str] = "RelatedPerson"
    active: Optional[bool] = None
    address: Optional[List[address.Address]] = empty_list()
    birthDate: Optional[fhirdate.FHIRDate] = None
    communication: Optional[List[RelatedPersonCommunication]] = empty_list()
    gender: Optional[str] = None
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    name: Optional[List[humanname.HumanName]] = empty_list()
    patient:fhirreference.FHIRReference = None
    period: Optional[period.Period] = None
    photo: Optional[List[attachment.Attachment]] = empty_list()
    relationship: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    telecom: Optional[List[contactpoint.ContactPoint]] = empty_list()

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.active = None
#        """ Whether this related person's record is in active use.
#        Type `bool`
#
#. """
#
#
#        self.address = None
#        """ Address where the related person can be contacted or visited.
#        List of `Address` items
#
# (represented as `dict` in JSON). """
#
#
#        self.birthDate = None
#        """ The date on which the related person was born.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.communication = None
#        """ A language which may be used to communicate with about the
        patient's health.
#        List of `RelatedPersonCommunication` items
#
# (represented as `dict` in JSON). """
#
#
#        self.gender = None
#        """ male | female | other | unknown.
#        Type `str`
#
#. """
#
#
#        self.identifier = None
#        """ A human identifier for this person.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ A name associated with the person.
#        List of `HumanName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.patient = None
#        """ The patient this person is related to.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.period = None
#        """ Period of time that this relationship is considered valid.
#        Type `Period`
#
# (represented as `dict` in JSON). """
#
#
#        self.photo = None
#        """ Image of the person.
#        List of `Attachment` items
#
# (represented as `dict` in JSON). """
#
#
#        self.relationship = None
#        """ The nature of the relationship.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.telecom = None
#        """ A contact detail for the person.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#

#        super(RelatedPerson, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RelatedPerson, self).elementProperties()
        js.extend([
            ("active", "active", bool, {  # #}False, None, {  # #}False),
            ("address", "address", address.Address, {  # #}True, None, {  # #}False),
            ("birthDate", "birthDate", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("communication", "communication", RelatedPersonCommunication, {  # #}True, None, {  # #}False),
            ("gender", "gender", str, {  # #}False, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("name", "name", humanname.HumanName, {  # #}True, None, {  # #}False),
            ("patient", "patient", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("period", "period", period.Period, {  # #}False, None, {  # #}False),
            ("photo", "photo", attachment.Attachment, {  # #}True, None, {  # #}False),
            ("relationship", "relationship", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("telecom", "telecom", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import address
from . import attachment
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import humanname
from . import identifier
from . import period


from . import backboneelement

@dataclass
class RelatedPersonCommunication(backboneelement.BackboneElement):
    """ A language which may be used to communicate with about the patient's health.
    """
    resource_type: ClassVar[str] = "RelatedPersonCommunication"
    language:codeableconcept.CodeableConcept = None
    preferred: Optional[bool] = None

    jsondict: InitVar[Optional[dict]] = None
    strict: InitVar[bool] = True

    def __post_init__(self, jsondict, strict) -> None:
        fhirabstractbase.FHIRAbstractBase(jsondict, strict)

#    def __init__(self, jsondict=None, strict=True):
#        """ Initialize all valid properties.
#
#        :raises: FHIRValidationError on validation errors, unless strict is False
#        :param dict jsondict: A JSON dictionary to use for initialization
#        :param bool strict: If True (the default), invalid variables will raise a TypeError
#        """
#
#
#        self.language = None
#        """ The language which can be used to communicate with the patient
        about his or her health.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.preferred = None
#        """ Language preference indicator.
#        Type `bool`
#
#. """
#

#        super(RelatedPersonCommunication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(RelatedPersonCommunication, self).elementProperties()
        js.extend([
            ("language", "language", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("preferred", "preferred", bool, {  # #}False, None, {  # #}False),
        ])
        return js