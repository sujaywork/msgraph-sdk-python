from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
    from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

@dataclass
class AccessPackageResourceAttribute(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The destination property
    destination: Optional[AccessPackageResourceAttributeDestination] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The source property
    source: Optional[AccessPackageResourceAttributeSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttribute
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceAttribute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        fields: Dict[str, Callable[[Any], None]] = {
            "destination": lambda n : setattr(self, 'destination', n.get_object_value(AccessPackageResourceAttributeDestination)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(AccessPackageResourceAttributeSource)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("destination", self.destination)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

