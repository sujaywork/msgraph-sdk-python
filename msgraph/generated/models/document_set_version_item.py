from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DocumentSetVersionItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The unique identifier for the item.
    item_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The title of the item.
    title: Optional[str] = None
    # The version ID of the item.
    version_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSetVersionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSetVersionItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DocumentSetVersionItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "itemId": lambda n : setattr(self, 'item_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "versionId": lambda n : setattr(self, 'version_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("itemId", self.item_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_str_value("versionId", self.version_id)
        writer.write_additional_data_value(self.additional_data)
    

