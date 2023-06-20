from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import onenote_page_preview_links

@dataclass
class OnenotePagePreview(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The links property
    links: Optional[onenote_page_preview_links.OnenotePagePreviewLinks] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The previewText property
    preview_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePagePreview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePagePreview
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnenotePagePreview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import onenote_page_preview_links

        from . import onenote_page_preview_links

        fields: Dict[str, Callable[[Any], None]] = {
            "links": lambda n : setattr(self, 'links', n.get_object_value(onenote_page_preview_links.OnenotePagePreviewLinks)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previewText": lambda n : setattr(self, 'preview_text', n.get_str_value()),
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
        writer.write_object_value("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("previewText", self.preview_text)
        writer.write_additional_data_value(self.additional_data)
    

