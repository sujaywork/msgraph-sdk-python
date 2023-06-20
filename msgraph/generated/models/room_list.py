from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import place, room

from . import place

@dataclass
class RoomList(place.Place):
    odata_type = "#microsoft.graph.roomList"
    # The email address of the room list.
    email_address: Optional[str] = None
    # The rooms property
    rooms: Optional[List[room.Room]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoomList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoomList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RoomList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import place, room

        from . import place, room

        fields: Dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "rooms": lambda n : setattr(self, 'rooms', n.get_collection_of_object_values(room.Room)),
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
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("rooms", self.rooms)
    

