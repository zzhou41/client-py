#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis) on 2019-07-18.
#  2019, SMART Health IT.
import sys
from dataclasses import dataclass
from typing import ClassVar, Optional, List
from .fhirabstractbase import empty_list

from .annotation import Annotation
from .backboneelement import BackboneElement
from .codeableconcept import CodeableConcept
from .contactdetail import ContactDetail
from .domainresource import DomainResource
from .fhirdate import FHIRDate
from .fhirreference import FHIRReference
from .identifier import Identifier
from .period import Period
from .relatedartifact import RelatedArtifact
from .usagecontext import UsageContext


@dataclass
class RiskEvidenceSynthesisSampleSize(BackboneElement):
    """ What sample size was involved?.

    A description of the size of the sample involved in the synthesis.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisSampleSize"
    description: Optional[str] = None
    numberOfParticipants: Optional[int] = None
    numberOfStudies: Optional[int] = None

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisSampleSize, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("numberOfParticipants", "numberOfParticipants", int, False, None, False),
            ("numberOfStudies", "numberOfStudies", int, False, None, False),
        ])
        return js


@dataclass
class RiskEvidenceSynthesisRiskEstimatePrecisionEstimate(BackboneElement):
    """ How precise the estimate is.

    A description of the precision of the estimate for the effect.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimatePrecisionEstimate"
    from_fhir: Optional[float] = None
    level: Optional[float] = None
    to: Optional[float] = None
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, self).elementProperties()
        js.extend([
            ("from_fhir", "from", float, False, None, False),
            ("level", "level", float, False, None, False),
            ("to", "to", float, False, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class RiskEvidenceSynthesisRiskEstimate(BackboneElement):
    """ What was the estimated risk.

    The estimated risk of the outcome.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisRiskEstimate"
    denominatorCount: Optional[int] = None
    description: Optional[str] = None
    numeratorCount: Optional[int] = None
    precisionEstimate: Optional[List[RiskEvidenceSynthesisRiskEstimatePrecisionEstimate]] = empty_list()
    type: Optional[CodeableConcept] = None
    unitOfMeasure: Optional[CodeableConcept] = None
    value: Optional[float] = None

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisRiskEstimate, self).elementProperties()
        js.extend([
            ("denominatorCount", "denominatorCount", int, False, None, False),
            ("description", "description", str, False, None, False),
            ("numeratorCount", "numeratorCount", int, False, None, False),
            ("precisionEstimate", "precisionEstimate", RiskEvidenceSynthesisRiskEstimatePrecisionEstimate, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
            ("unitOfMeasure", "unitOfMeasure", CodeableConcept, False, None, False),
            ("value", "value", float, False, None, False),
        ])
        return js


@dataclass
class RiskEvidenceSynthesisCertaintyCertaintySubcomponent(BackboneElement):
    """ A component that contributes to the overall certainty.

    A description of a component of the overall certainty.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertaintyCertaintySubcomponent"
    note: Optional[List[Annotation]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()
    type: Optional[CodeableConcept] = None

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertaintyCertaintySubcomponent, self).elementProperties()
        js.extend([
            ("note", "note", Annotation, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
            ("type", "type", CodeableConcept, False, None, False),
        ])
        return js


@dataclass
class RiskEvidenceSynthesisCertainty(BackboneElement):
    """ How certain is the risk.

    A description of the certainty of the risk estimate.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesisCertainty"
    certaintySubcomponent: Optional[List[RiskEvidenceSynthesisCertaintyCertaintySubcomponent]] = empty_list()
    note: Optional[List[Annotation]] = empty_list()
    rating: Optional[List[CodeableConcept]] = empty_list()

    def elementProperties(self):
        js = super(RiskEvidenceSynthesisCertainty, self).elementProperties()
        js.extend([
            ("certaintySubcomponent", "certaintySubcomponent", RiskEvidenceSynthesisCertaintyCertaintySubcomponent, True, None, False),
            ("note", "note", Annotation, True, None, False),
            ("rating", "rating", CodeableConcept, True, None, False),
        ])
        return js


@dataclass
class RiskEvidenceSynthesis(DomainResource):
    """ A quantified estimate of risk based on a body of evidence.

    The RiskEvidenceSynthesis resource describes the likelihood of an outcome
    in a population plus exposure state where the risk estimate is derived from
    a combination of research studies.
    """
    resource_type: ClassVar[str] = "RiskEvidenceSynthesis"
    approvalDate: Optional[FHIRDate] = None
    author: Optional[List[ContactDetail]] = empty_list()
    certainty: Optional[List[RiskEvidenceSynthesisCertainty]] = empty_list()
    contact: Optional[List[ContactDetail]] = empty_list()
    copyright: Optional[str] = None
    date: Optional[FHIRDate] = None
    description: Optional[str] = None
    editor: Optional[List[ContactDetail]] = empty_list()
    effectivePeriod: Optional[Period] = None
    endorser: Optional[List[ContactDetail]] = empty_list()
    exposure: Optional[FHIRReference] = None
    identifier: Optional[List[Identifier]] = empty_list()
    jurisdiction: Optional[List[CodeableConcept]] = empty_list()
    lastReviewDate: Optional[FHIRDate] = None
    name: Optional[str] = None
    note: Optional[List[Annotation]] = empty_list()
    outcome: FHIRReference = None
    population: FHIRReference = None
    publisher: Optional[str] = None
    relatedArtifact: Optional[List[RelatedArtifact]] = empty_list()
    reviewer: Optional[List[ContactDetail]] = empty_list()
    riskEstimate: Optional[RiskEvidenceSynthesisRiskEstimate] = None
    sampleSize: Optional[RiskEvidenceSynthesisSampleSize] = None
    status: str = None
    studyType: Optional[CodeableConcept] = None
    synthesisType: Optional[CodeableConcept] = None
    title: Optional[str] = None
    topic: Optional[List[CodeableConcept]] = empty_list()
    url: Optional[str] = None
    useContext: Optional[List[UsageContext]] = empty_list()
    version: Optional[str] = None

    def elementProperties(self):
        js = super(RiskEvidenceSynthesis, self).elementProperties()
        js.extend([
            ("approvalDate", "approvalDate", FHIRDate, False, None, False),
            ("author", "author", ContactDetail, True, None, False),
            ("certainty", "certainty", RiskEvidenceSynthesisCertainty, True, None, False),
            ("contact", "contact", ContactDetail, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("editor", "editor", ContactDetail, True, None, False),
            ("effectivePeriod", "effectivePeriod", Period, False, None, False),
            ("endorser", "endorser", ContactDetail, True, None, False),
            ("exposure", "exposure", FHIRReference, False, None, False),
            ("identifier", "identifier", Identifier, True, None, False),
            ("jurisdiction", "jurisdiction", CodeableConcept, True, None, False),
            ("lastReviewDate", "lastReviewDate", FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", Annotation, True, None, False),
            ("outcome", "outcome", FHIRReference, False, None, True),
            ("population", "population", FHIRReference, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("relatedArtifact", "relatedArtifact", RelatedArtifact, True, None, False),
            ("reviewer", "reviewer", ContactDetail, True, None, False),
            ("riskEstimate", "riskEstimate", RiskEvidenceSynthesisRiskEstimate, False, None, False),
            ("sampleSize", "sampleSize", RiskEvidenceSynthesisSampleSize, False, None, False),
            ("status", "status", str, False, None, True),
            ("studyType", "studyType", CodeableConcept, False, None, False),
            ("synthesisType", "synthesisType", CodeableConcept, False, None, False),
            ("title", "title", str, False, None, False),
            ("topic", "topic", CodeableConcept, True, None, False),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", UsageContext, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js