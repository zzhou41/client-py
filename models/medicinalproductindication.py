#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import domainresource
from . import fhirreference
from . import population
from . import quantity


from . import domainresource

@dataclass
class MedicinalProductIndication(domainresource.DomainResource):
    """ MedicinalProductIndication.

    Indication for the Medicinal Product.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndication"
    comorbidity: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    diseaseStatus: Optional[codeableconcept.CodeableConcept] = None
    diseaseSymptomProcedure: Optional[codeableconcept.CodeableConcept] = None
    duration: Optional[quantity.Quantity] = None
    intendedEffect: Optional[codeableconcept.CodeableConcept] = None
    otherTherapy: Optional[List[MedicinalProductIndicationOtherTherapy]] = empty_list()
    population: Optional[List[population.Population]] = empty_list()
    subject: Optional[List[fhirreference.FHIRReference]] = empty_list()
    undesirableEffect: Optional[List[fhirreference.FHIRReference]] = empty_list()

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
#        self.comorbidity = None
#        """ Comorbidity (concurrent condition) or co-infection as part of the
        indication.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.diseaseStatus = None
#        """ The status of the disease or symptom for which the indication
        applies.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.diseaseSymptomProcedure = None
#        """ The disease, symptom or procedure that is the indication for
        treatment.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.duration = None
#        """ Timing or duration information as part of the indication.
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.intendedEffect = None
#        """ The intended effect, aim or strategy to be achieved by the
        indication.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.otherTherapy = None
#        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the indication.
#        List of `MedicinalProductIndicationOtherTherapy` items
#
# (represented as `dict` in JSON). """
#
#
#        self.population = None
#        """ The population group to which this applies.
#        List of `Population` items
#
# (represented as `dict` in JSON). """
#
#
#        self.subject = None
#        """ The medication for which this is an indication.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.undesirableEffect = None
#        """ Describe the undesirable effects of the medicinal product.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIndication, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIndication, self).elementProperties()
        js.extend([
            ("comorbidity", "comorbidity", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("diseaseStatus", "diseaseStatus", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("diseaseSymptomProcedure", "diseaseSymptomProcedure", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("duration", "duration", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("intendedEffect", "intendedEffect", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("otherTherapy", "otherTherapy", MedicinalProductIndicationOtherTherapy, {  # #}True, None, {  # #}False),
            ("population", "population", population.Population, {  # #}True, None, {  # #}False),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("undesirableEffect", "undesirableEffect", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import backboneelement
from . import codeableconcept
from . import fhirreference
from . import population
from . import quantity


from . import backboneelement

@dataclass
class MedicinalProductIndicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """
    resource_type: ClassVar[str] = "MedicinalProductIndicationOtherTherapy"
    medicationCodeableConcept:codeableconcept.CodeableConcept = None
    medicationReference:fhirreference.FHIRReference = None
    therapyRelationshipType:codeableconcept.CodeableConcept = None

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
#        self.medicationCodeableConcept = None
#        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.medicationReference = None
#        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.therapyRelationshipType = None
#        """ The type of relationship between the medicinal product indication
        or contraindication and another therapy.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(MedicinalProductIndicationOtherTherapy, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductIndicationOtherTherapy, self).elementProperties()
        js.extend([
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, {  # #}False, "medication", {  # #}True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, {  # #}False, "medication", {  # #}True),
            ("therapyRelationshipType", "therapyRelationshipType", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js