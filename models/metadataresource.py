#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MetadataResource) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import codeableconcept
from . import contactdetail
from . import domainresource
from . import fhirdate
from . import usagecontext


from . import domainresource

@dataclass
class MetadataResource(domainresource.DomainResource):
    """ Common Ancestor declaration for definitional resources.

    Common Ancestor declaration for conformance and knowledge artifact
    resources.
    """
    resource_type: ClassVar[str] = "MetadataResource"
    contact: Optional[List[contactdetail.ContactDetail]] = empty_list()
    date: Optional[fhirdate.FHIRDate] = None
    description: Optional[str] = None
    experimental: Optional[bool] = None
    jurisdiction: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    name: Optional[str] = None
    publisher: Optional[str] = None
    status: str = None
    title: Optional[str] = None
    url: Optional[str] = None
    useContext: Optional[List[usagecontext.UsageContext]] = empty_list()
    version: Optional[str] = None

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
#        self.contact = None
#        """ Contact details for the publisher.
#        List of `ContactDetail` items
#
# (represented as `dict` in JSON). """
#
#
#        self.date = None
#        """ Date last changed.
#        Type `FHIRDate`
#
# (represented as `str` in JSON). """
#
#
#        self.description = None
#        """ Natural language description of the metadata resource.
#        Type `str`
#
#. """
#
#
#        self.experimental = None
#        """ For testing purposes, not real usage.
#        Type `bool`
#
#. """
#
#
#        self.jurisdiction = None
#        """ Intended jurisdiction for metadata resource (if applicable).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.name = None
#        """ Name for this metadata resource (computer friendly).
#        Type `str`
#
#. """
#
#
#        self.publisher = None
#        """ Name of the publisher (organization or individual).
#        Type `str`
#
#. """
#
#
#        self.status = None
#        """ draft | active | retired | unknown.
#        Type `str`
#
#. """
#
#
#        self.title = None
#        """ Name for this metadata resource (human friendly).
#        Type `str`
#
#. """
#
#
#        self.url = None
#        """ Canonical identifier for this metadata resource, represented as a
        URI (globally unique).
#        Type `str`
#
#. """
#
#
#        self.useContext = None
#        """ The context that the content is intended to support.
#        List of `UsageContext` items
#
# (represented as `dict` in JSON). """
#
#
#        self.version = None
#        """ Business version of the metadata resource.
#        Type `str`
#
#. """
#

#        super(MetadataResource, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MetadataResource, self).elementProperties()
        js.extend([
            ("contact", "contact", contactdetail.ContactDetail, {  # #}True, None, {  # #}False),
            ("date", "date", fhirdate.FHIRDate, {  # #}False, None, {  # #}False),
            ("description", "description", str, {  # #}False, None, {  # #}False),
            ("experimental", "experimental", bool, {  # #}False, None, {  # #}False),
            ("jurisdiction", "jurisdiction", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("name", "name", str, {  # #}False, None, {  # #}False),
            ("publisher", "publisher", str, {  # #}False, None, {  # #}False),
            ("status", "status", str, {  # #}False, None, {  # #}True),
            ("title", "title", str, {  # #}False, None, {  # #}False),
            ("url", "url", str, {  # #}False, None, {  # #}False),
            ("useContext", "useContext", usagecontext.UsageContext, {  # #}True, None, {  # #}False),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js