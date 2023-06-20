from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_condition_set, conditional_access_grant_controls, conditional_access_session_controls

@dataclass
class ConditionalAccessPolicyDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The conditions property
    conditions: Optional[conditional_access_condition_set.ConditionalAccessConditionSet] = None
    # Represents grant controls that must be fulfilled for the policy.
    grant_controls: Optional[conditional_access_grant_controls.ConditionalAccessGrantControls] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a complex type of session controls that is enforced after sign-in.
    session_controls: Optional[conditional_access_session_controls.ConditionalAccessSessionControls] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessPolicyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessPolicyDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessPolicyDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_condition_set, conditional_access_grant_controls, conditional_access_session_controls

        from . import conditional_access_condition_set, conditional_access_grant_controls, conditional_access_session_controls

        fields: Dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(conditional_access_condition_set.ConditionalAccessConditionSet)),
            "grantControls": lambda n : setattr(self, 'grant_controls', n.get_object_value(conditional_access_grant_controls.ConditionalAccessGrantControls)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sessionControls": lambda n : setattr(self, 'session_controls', n.get_object_value(conditional_access_session_controls.ConditionalAccessSessionControls)),
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
        writer.write_object_value("conditions", self.conditions)
        writer.write_object_value("grantControls", self.grant_controls)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("sessionControls", self.session_controls)
        writer.write_additional_data_value(self.additional_data)
    

