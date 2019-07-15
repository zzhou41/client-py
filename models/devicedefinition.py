#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/DeviceDefinition) on 2019-07-03.
#  2019, SMART Health IT.

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import domainresource
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


from . import domainresource

@dataclass
class DeviceDefinition(domainresource.DomainResource):
    """ An instance of a medical-related component of a medical device.

    The characteristics, operational status and capabilities of a medical-
    related component of a medical device.
    """
    resource_type: ClassVar[str] = "DeviceDefinition"
    capability: Optional[List[DeviceDefinitionCapability]] = empty_list()
    contact: Optional[List[contactpoint.ContactPoint]] = empty_list()
    deviceName: Optional[List[DeviceDefinitionDeviceName]] = empty_list()
    identifier: Optional[List[identifier.Identifier]] = empty_list()
    languageCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    manufacturerReference: Optional[fhirreference.FHIRReference] = None
    manufacturerString: Optional[str] = None
    material: Optional[List[DeviceDefinitionMaterial]] = empty_list()
    modelNumber: Optional[str] = None
    note: Optional[List[annotation.Annotation]] = empty_list()
    onlineInformation: Optional[str] = None
    owner: Optional[fhirreference.FHIRReference] = None
    parentDevice: Optional[fhirreference.FHIRReference] = None
    physicalCharacteristics: Optional[prodcharacteristic.ProdCharacteristic] = None
    property: Optional[List[DeviceDefinitionProperty]] = empty_list()
    quantity: Optional[quantity.Quantity] = None
    safety: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    shelfLifeStorage: Optional[List[productshelflife.ProductShelfLife]] = empty_list()
    specialization: Optional[List[DeviceDefinitionSpecialization]] = empty_list()
    type: Optional[codeableconcept.CodeableConcept] = None
    udiDeviceIdentifier: Optional[List[DeviceDefinitionUdiDeviceIdentifier]] = empty_list()
    url: Optional[str] = None
    version: Optional[List[str]] = empty_list()

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
#        self.capability = None
#        """ Device capabilities.
#        List of `DeviceDefinitionCapability` items
#
# (represented as `dict` in JSON). """
#
#
#        self.contact = None
#        """ Details for human/organization for support.
#        List of `ContactPoint` items
#
# (represented as `dict` in JSON). """
#
#
#        self.deviceName = None
#        """ A name given to the device to identify it.
#        List of `DeviceDefinitionDeviceName` items
#
# (represented as `dict` in JSON). """
#
#
#        self.identifier = None
#        """ Instance identifier.
#        List of `Identifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.languageCode = None
#        """ Language code for the human-readable text strings produced by the
        device (all supported).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturerReference = None
#        """ Name of device manufacturer.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.manufacturerString = None
#        """ Name of device manufacturer.
#        Type `str`
#
#. """
#
#
#        self.material = None
#        """ A substance used to create the material(s) of which the device is
        made.
#        List of `DeviceDefinitionMaterial` items
#
# (represented as `dict` in JSON). """
#
#
#        self.modelNumber = None
#        """ The model number for the device.
#        Type `str`
#
#. """
#
#
#        self.note = None
#        """ Device notes and comments.
#        List of `Annotation` items
#
# (represented as `dict` in JSON). """
#
#
#        self.onlineInformation = None
#        """ Access to on-line information.
#        Type `str`
#
#. """
#
#
#        self.owner = None
#        """ Organization responsible for device.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.parentDevice = None
#        """ The parent device it can be part of.
#        Type `FHIRReference`
#
# (represented as `dict` in JSON). """
#
#
#        self.physicalCharacteristics = None
#        """ Dimensions, color etc..
#        Type `ProdCharacteristic`
#
# (represented as `dict` in JSON). """
#
#
#        self.property = None
#        """ The actual configuration settings of a device as it actually
        operates, e.g., regulation status, time properties.
#        List of `DeviceDefinitionProperty` items
#
# (represented as `dict` in JSON). """
#
#
#        self.quantity = None
#        """ The quantity of the device present in the packaging (e.g. the
        number of devices present in a pack, or the number of devices in
        the same package of the medicinal product).
#        Type `Quantity`
#
# (represented as `dict` in JSON). """
#
#
#        self.safety = None
#        """ Safety characteristics of the device.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.shelfLifeStorage = None
#        """ Shelf Life and storage information.
#        List of `ProductShelfLife` items
#
# (represented as `dict` in JSON). """
#
#
#        self.specialization = None
#        """ The capabilities supported on a  device, the standards to which the
        device conforms for a particular purpose, and used for the
        communication.
#        List of `DeviceDefinitionSpecialization` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ What kind of device or device system this is.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.udiDeviceIdentifier = None
#        """ Unique Device Identifier (UDI) Barcode string.
#        List of `DeviceDefinitionUdiDeviceIdentifier` items
#
# (represented as `dict` in JSON). """
#
#
#        self.url = None
#        """ Network address to contact device.
#        Type `str`
#
#. """
#
#
#        self.version = None
#        """ Available versions.
#        List of `str` items
#
#. """
#

#        super(DeviceDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinition, self).elementProperties()
        js.extend([
            ("capability", "capability", DeviceDefinitionCapability, {  # #}True, None, {  # #}False),
            ("contact", "contact", contactpoint.ContactPoint, {  # #}True, None, {  # #}False),
            ("deviceName", "deviceName", DeviceDefinitionDeviceName, {  # #}True, None, {  # #}False),
            ("identifier", "identifier", identifier.Identifier, {  # #}True, None, {  # #}False),
            ("languageCode", "languageCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("manufacturerReference", "manufacturerReference", fhirreference.FHIRReference, {  # #}False, "manufacturer", {  # #}False),
            ("manufacturerString", "manufacturerString", str, {  # #}False, "manufacturer", {  # #}False),
            ("material", "material", DeviceDefinitionMaterial, {  # #}True, None, {  # #}False),
            ("modelNumber", "modelNumber", str, {  # #}False, None, {  # #}False),
            ("note", "note", annotation.Annotation, {  # #}True, None, {  # #}False),
            ("onlineInformation", "onlineInformation", str, {  # #}False, None, {  # #}False),
            ("owner", "owner", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("parentDevice", "parentDevice", fhirreference.FHIRReference, {  # #}False, None, {  # #}False),
            ("physicalCharacteristics", "physicalCharacteristics", prodcharacteristic.ProdCharacteristic, {  # #}False, None, {  # #}False),
            ("property", "property", DeviceDefinitionProperty, {  # #}True, None, {  # #}False),
            ("quantity", "quantity", quantity.Quantity, {  # #}False, None, {  # #}False),
            ("safety", "safety", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("shelfLifeStorage", "shelfLifeStorage", productshelflife.ProductShelfLife, {  # #}True, None, {  # #}False),
            ("specialization", "specialization", DeviceDefinitionSpecialization, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}False),
            ("udiDeviceIdentifier", "udiDeviceIdentifier", DeviceDefinitionUdiDeviceIdentifier, {  # #}True, None, {  # #}False),
            ("url", "url", str, {  # #}False, None, {  # #}False),
            ("version", "version", str, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import backboneelement
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


from . import backboneelement

@dataclass
class DeviceDefinitionCapability(backboneelement.BackboneElement):
    """ Device capabilities.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionCapability"
    description: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    type:codeableconcept.CodeableConcept = None

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
#        self.description = None
#        """ Description of capability.
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.type = None
#        """ Type of capability.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(DeviceDefinitionCapability, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionCapability, self).elementProperties()
        js.extend([
            ("description", "description", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


@dataclass
class DeviceDefinitionDeviceName(backboneelement.BackboneElement):
    """ A name given to the device to identify it.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionDeviceName"
    name: str = None
    type: str = None

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
#        self.name = None
#        """ The name of the device.
#        Type `str`
#
#. """
#
#
#        self.type = None
#        """ udi-label-name | user-friendly-name | patient-reported-name |
        manufacturer-name | model-name | other.
#        Type `str`
#
#. """
#

#        super(DeviceDefinitionDeviceName, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionDeviceName, self).elementProperties()
        js.extend([
            ("name", "name", str, {  # #}False, None, {  # #}True),
            ("type", "type", str, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


@dataclass
class DeviceDefinitionMaterial(backboneelement.BackboneElement):
    """ A substance used to create the material(s) of which the device is made.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionMaterial"
    allergenicIndicator: Optional[bool] = None
    alternate: Optional[bool] = None
    substance:codeableconcept.CodeableConcept = None

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
#        self.allergenicIndicator = None
#        """ Whether the substance is a known or suspected allergen.
#        Type `bool`
#
#. """
#
#
#        self.alternate = None
#        """ Indicates an alternative material of the device.
#        Type `bool`
#
#. """
#
#
#        self.substance = None
#        """ The substance.
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#

#        super(DeviceDefinitionMaterial, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionMaterial, self).elementProperties()
        js.extend([
            ("allergenicIndicator", "allergenicIndicator", bool, {  # #}False, None, {  # #}False),
            ("alternate", "alternate", bool, {  # #}False, None, {  # #}False),
            ("substance", "substance", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


@dataclass
class DeviceDefinitionProperty(backboneelement.BackboneElement):
    """ The actual configuration settings of a device as it actually operates,
    e.g., regulation status, time properties.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionProperty"
    type:codeableconcept.CodeableConcept = None
    valueCode: Optional[List[codeableconcept.CodeableConcept]] = empty_list()
    valueQuantity: Optional[List[quantity.Quantity]] = empty_list()

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
#        self.type = None
#        """ Code that specifies the property DeviceDefinitionPropetyCode
        (Extensible).
#        Type `CodeableConcept`
#
# (represented as `dict` in JSON). """
#
#
#        self.valueCode = None
#        """ Property value as a code, e.g., NTP4 (synced to NTP).
#        List of `CodeableConcept` items
#
# (represented as `dict` in JSON). """
#
#
#        self.valueQuantity = None
#        """ Property value as a quantity.
#        List of `Quantity` items
#
# (represented as `dict` in JSON). """
#

#        super(DeviceDefinitionProperty, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionProperty, self).elementProperties()
        js.extend([
            ("type", "type", codeableconcept.CodeableConcept, {  # #}False, None, {  # #}True),
            ("valueCode", "valueCode", codeableconcept.CodeableConcept, {  # #}True, None, {  # #}False),
            ("valueQuantity", "valueQuantity", quantity.Quantity, {  # #}True, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


@dataclass
class DeviceDefinitionSpecialization(backboneelement.BackboneElement):
    """ The capabilities supported on a  device, the standards to which the device
    conforms for a particular purpose, and used for the communication.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionSpecialization"
    systemType: str = None
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
#        self.systemType = None
#        """ The standard that is used to operate and communicate.
#        Type `str`
#
#. """
#
#
#        self.version = None
#        """ The version of the standard that is used to operate and communicate.
#        Type `str`
#
#. """
#

#        super(DeviceDefinitionSpecialization, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionSpecialization, self).elementProperties()
        js.extend([
            ("systemType", "systemType", str, {  # #}False, None, {  # #}True),
            ("version", "version", str, {  # #}False, None, {  # #}False),
        ])
        return js

from dataclasses import dataclass, InitVar
from typing import ClassVar, Optional, List
from models import fhirabstractbase
from .fhirabstractbase import *


from . import annotation
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
from . import prodcharacteristic
from . import productshelflife
from . import quantity


@dataclass
class DeviceDefinitionUdiDeviceIdentifier(backboneelement.BackboneElement):
    """ Unique Device Identifier (UDI) Barcode string.

    Unique device identifier (UDI) assigned to device label or package.  Note
    that the Device may include multiple udiCarriers as it either may include
    just the udiCarrier for the jurisdiction it is sold, or for multiple
    jurisdictions it could have been sold.
    """
    resource_type: ClassVar[str] = "DeviceDefinitionUdiDeviceIdentifier"
    deviceIdentifier: str = None
    issuer: str = None
    jurisdiction: str = None

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
#        self.deviceIdentifier = None
#        """ The identifier that is to be associated with every Device that
        references this DeviceDefintiion for the issuer and jurisdication
        porvided in the DeviceDefinition.udiDeviceIdentifier.
#        Type `str`
#
#. """
#
#
#        self.issuer = None
#        """ The organization that assigns the identifier algorithm.
#        Type `str`
#
#. """
#
#
#        self.jurisdiction = None
#        """ The jurisdiction to which the deviceIdentifier applies.
#        Type `str`
#
#. """
#

#        super(DeviceDefinitionUdiDeviceIdentifier, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceDefinitionUdiDeviceIdentifier, self).elementProperties()
        js.extend([
            ("deviceIdentifier", "deviceIdentifier", str, {  # #}False, None, {  # #}True),
            ("issuer", "issuer", str, {  # #}False, None, {  # #}True),
            ("jurisdiction", "jurisdiction", str, {  # #}False, None, {  # #}True),
        ])
        return js