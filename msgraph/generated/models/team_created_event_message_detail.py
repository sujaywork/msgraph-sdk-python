from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set

from . import event_message_detail

@dataclass
class TeamCreatedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.teamCreatedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    # Description for the team.
    team_description: Optional[str] = None
    # Display name of the team.
    team_display_name: Optional[str] = None
    # Unique identifier of the team.
    team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamCreatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamCreatedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamCreatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set

        from . import event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "teamDescription": lambda n : setattr(self, 'team_description', n.get_str_value()),
            "teamDisplayName": lambda n : setattr(self, 'team_display_name', n.get_str_value()),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_str_value("teamDescription", self.team_description)
        writer.write_str_value("teamDisplayName", self.team_display_name)
        writer.write_str_value("teamId", self.team_id)
    

