from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration, oma_setting

from . import device_configuration

@dataclass
class AndroidWorkProfileCustomConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.androidWorkProfileCustomConfiguration"
    # OMA settings. This collection can contain a maximum of 500 elements.
    oma_settings: Optional[List[oma_setting.OmaSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidWorkProfileCustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileCustomConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidWorkProfileCustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration, oma_setting

        from . import device_configuration, oma_setting

        fields: Dict[str, Callable[[Any], None]] = {
            "omaSettings": lambda n : setattr(self, 'oma_settings', n.get_collection_of_object_values(oma_setting.OmaSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("omaSettings", self.oma_settings)
    

