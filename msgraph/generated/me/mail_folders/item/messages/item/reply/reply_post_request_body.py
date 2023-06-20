from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import message

@dataclass
class ReplyPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The Comment property
    comment: Optional[str] = None
    # The Message property
    message: Optional[message.Message] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReplyPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReplyPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReplyPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import message

        from .......models import message

        fields: Dict[str, Callable[[Any], None]] = {
            "Comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "Message": lambda n : setattr(self, 'message', n.get_object_value(message.Message)),
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
        writer.write_str_value("Comment", self.comment)
        writer.write_object_value("Message", self.message)
        writer.write_additional_data_value(self.additional_data)
    

