#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/ImagingStudy) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import coding
from . import domainresource
from . import fhirdate
from . import fhirreference
from . import identifier


from . import domainresource

@dataclass
class ImagingStudy(domainresource.DomainResource):
    """ A set of images produced in single study (one or more series of references
    images).

    Representation of the content produced in a DICOM imaging study. A study
    comprises a set of series, each of which includes a set of Service-Object
    Pair Instances (SOP Instances - images or other data) acquired or produced
    in a common context.  A series is of only one modality (e.g. X-ray, CT, MR,
    ultrasound), but a study may have multiple series of different modalities.
    """
    resource_type: ClassVar[str] = "ImagingStudy"
    basedOn: Optional[List[fhirreference.FHIRReference]] = empty_list()
    description: Optional[str] = None
    encounter: Optional[fhirreference.FHIRReference] = None
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    interpreter: Optional[List[fhirreference.FHIRReference]] = empty_list()
    location: Optional[fhirreference.FHIRReference] = None
    modality: Optional[List[coding.Coding]] = empty_list()
    note: Optional[List[annotation.Annotation]] = empty_list()
    numberOfInstances: Optional[int] = None
    numberOfSeries: Optional[int] = None
    procedureCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    procedureReference: Optional[fhirreference.FHIRReference] = None
    reasonCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    reasonReference: Optional[List[fhirreference.FHIRReference]] = empty_list()
    referrer: Optional[fhirreference.FHIRReference] = None
    series: Optional[List[ImagingStudySeries]] = empty_list()
    started: Optional[fhirdate.FHIRDate] = None
    status: str = None
    subject:fhirreference.FHIRReference = None

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
#        self.basedOn = None
#        """ Request fulfilled.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ Institution-generated description.
#        Type `str`
#
#. """
#
#
#        self.encounter = None
#        """ Encounter with which this imaging study is associated.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.endpoint = None
#        """ Study access endpoint.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Identifiers for the whole study.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.interpreter = None
#        """ Who interpreted images.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.location = None
#        """ Where ImagingStudy occurred.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.modality = None
#        """ All series modality if actual acquisition modalities.
#        List of `Coding` items
#
# (represented as `dict` in JSON). """
#
#
#        self.note = None
#        """ User-defined comments.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.numberOfInstances = None
#        """ Number of Study Related Instances.
#        Type `int`
#
#. """
#
#
#        self.numberOfSeries = None
#        """ Number of Study Related Series.
#        Type `int`
#
#. """
#
#
#        self.procedureCode = None
#        """ The performed procedure code.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.procedureReference = None
#        """ The performed Procedure reference.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonCode = None
#        """ Why the study was requested.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.reasonReference = None
#        """ Why was study performed.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.referrer = None
#        """ Referring physician.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.series = None
#        """ Each study has one or more series of instances.
#        List of `ImagingStudySeries` items
#
# (represented as `dict` in JSON). """
#
#
#        self.started = None
#        """ When the study was started.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.status = None
#        """ registered | available | cancelled | entered-in-error | unknown.
#        Type `str`
#
#. """
#
#
#        self.subject = None
#        """ Who or what is the subject of the study.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#

#        super(ImagingStudy, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudy, self).elementProperties()
        js.extend([
            ("basedOn", "basedOn", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("encounter", "encounter", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("interpreter", "interpreter", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("location", "location", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("modality", "modality", coding.Coding, {  # #}True, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("numberOfInstances", "numberOfInstances", int, {  # #}False, None, {  # #}False),
            ("numberOfSeries", "numberOfSeries", int, {  # #}False, None, {  # #}False),
            ("procedureCode", "procedureCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("procedureReference", "procedureReference", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("reasonCode", "reasonCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("referrer", "referrer", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("series", "series", ImagingStudySeries, {  # #}True, None, {  # #}False),
            ("started", "started", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("subject", "subject", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier


from . import backboneelement

@dataclass
class ImagingStudySeries(backboneelement.BackboneElement):
    """ Each study has one or more series of instances.

    Each study has one or more series of images or other content.
    """
    resource_type: ClassVar[str] = "ImagingStudySeries"
    bodySite: Optional[coding.Coding] = None
    description: Optional[str] = None
    endpoint: Optional[List[fhirreference.FHIRReference]] = empty_list()
    instance: Optional[List[ImagingStudySeriesInstance]] = empty_list()
    laterality: Optional[coding.Coding] = None
    modality:coding.Coding = None
    number: Optional[int] = None
    numberOfInstances: Optional[int] = None
    performer: Optional[List[ImagingStudySeriesPerformer]] = empty_list()
    specimen: Optional[List[fhirreference.FHIRReference]] = empty_list()
    started: Optional[fhirdate.FHIRDate] = None
    uid: str = None

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
#        self.bodySite = None
#        """ Body part examined.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.description = None
#        """ A short human readable summary of the series.
#        Type `str`
#
#. """
#
#
#        self.endpoint = None
#        """ Series access endpoint.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.instance = None
#        """ A single SOP instance from the series.
#        List of `ImagingStudySeriesInstance` items
#
# (represented as `dict` in JSON). """
#
#
#        self.laterality = None
#        """ Body part laterality.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.modality = None
#        """ The modality of the instances in the series.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.number = None
#        """ Numeric identifier of this series.
#        Type `int`
#
#. """
#
#
#        self.numberOfInstances = None
#        """ Number of Series Related Instances.
#        Type `int`
#
#. """
#
#
#        self.performer = None
#        """ Who performed the series.
#        List of `ImagingStudySeriesPerformer` items
#
# (represented as `dict` in JSON). """
#
#
#        self.specimen = None
#        """ Specimen imaged.
#        List of `FHIRReference` items
#
# (represented as `dict` in JSON). """
#
#
#        self.started = None
#        """ When the series started.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.uid = None
#        """ DICOM Series Instance UID for the series.
#        Type `str`
#
#. """
#

#        super(ImagingStudySeries, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudySeries, self).elementProperties()
        js.extend([
            ("bodySite", "bodySite", coding.Coding, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("endpoint", "endpoint", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("instance", "instance", ImagingStudySeriesInstance, {  # #}True, None, {  # #}False),
            ("laterality", "laterality", coding.Coding, {  # #}False, None, {  # #}False),
            ("modality", "modality", coding.Coding, {  # #}False, None, {  # #}True),
            ("number", "number", int, {  # #}False, None, {  # #}False),
            ("numberOfInstances", "numberOfInstances", int, {  # #}False, None, {  # #}False),
            ("performer", "performer", ImagingStudySeriesPerformer, {  # #}True, None, {  # #}False),
            ("specimen", "specimen", fhirreference.FHIRReference, {  # #}True, None, {  # #}False),
            ("started", "started", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("uid", "uid", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier


@dataclass
class ImagingStudySeriesInstance(backboneelement.BackboneElement):
    """ A single SOP instance from the series.

    A single SOP instance within the series, e.g. an image, or presentation
    state.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesInstance"
    number: Optional[int] = None
    sopClass:coding.Coding = None
    title: Optional[str] = None
    uid: str = None

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
#        self.number = None
#        """ The number of this instance in the series.
#        Type `int`
#
#. """
#
#
#        self.sopClass = None
#        """ DICOM class type.
#        Type `Coding`
#
# (represented as `dict` in JSON). """
#
#
#        self.title = None
#        """ Description of instance.
#        Type `str`
#
#. """
#
#
#        self.uid = None
#        """ DICOM SOP Instance UID.
#        Type `str`
#
#. """
#

#        super(ImagingStudySeriesInstance, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudySeriesInstance, self).elementProperties()
        js.extend([
            ("number", "number", int, {  # #}False, None, {  # #}False),
            ("sopClass", "sopClass", coding.Coding, {  # #}False, None, {  # #}True),
            ("title", "title", str, {  # #}False, None, {  # #}False),
            ("uid", "uid", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier


@dataclass
class ImagingStudySeriesPerformer(backboneelement.BackboneElement):
    """ Who performed the series.

    Indicates who or what performed the series and how they were involved.
    """
    resource_type: ClassVar[str] = "ImagingStudySeriesPerformer"
    actor:fhirreference.FHIRReference = None
    function: Optional[codeableconcept.CodeableConcept] = None

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
#        self.actor = None
#        """ Who performed the series.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.function = None
#        """ Type of performance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(ImagingStudySeriesPerformer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImagingStudySeriesPerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, {  # #}False, None, {  # #}True),
            ("function", "function", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
        ])
        return js