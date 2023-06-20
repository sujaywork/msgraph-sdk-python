from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import details_info, identity

from . import identity

@dataclass
class ProvisionedIdentity(identity.Identity):
    odata_type = "#microsoft.graph.provisionedIdentity"
    # Details of the identity.
    details: Optional[details_info.DetailsInfo] = None
    # Type of identity that has been provisioned, such as 'user' or 'group'.
    identity_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisionedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionedIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ProvisionedIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import details_info, identity

        from . import details_info, identity

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(details_info.DetailsInfo)),
            "identityType": lambda n : setattr(self, 'identity_type', n.get_str_value()),
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
        writer.write_object_value("details", self.details)
        writer.write_str_value("identityType", self.identity_type)
    

