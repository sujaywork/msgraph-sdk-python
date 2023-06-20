from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import advanced_config_state, feature_target

@dataclass
class AuthenticationMethodFeatureConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A single entity that is excluded from this feature.
    exclude_target: Optional[feature_target.FeatureTarget] = None
    # A single entity that is included in this feature.
    include_target: Optional[feature_target.FeatureTarget] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Enable or disable the feature. Possible values are: default, enabled, disabled, unknownFutureValue. The default value is used when the configuration hasn't been explicitly set and uses the default behavior of Azure AD for the setting. The default value is disabled.
    state: Optional[advanced_config_state.AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodFeatureConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodFeatureConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodFeatureConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import advanced_config_state, feature_target

        from . import advanced_config_state, feature_target

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeTarget": lambda n : setattr(self, 'exclude_target', n.get_object_value(feature_target.FeatureTarget)),
            "includeTarget": lambda n : setattr(self, 'include_target', n.get_object_value(feature_target.FeatureTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(advanced_config_state.AdvancedConfigState)),
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
        writer.write_object_value("excludeTarget", self.exclude_target)
        writer.write_object_value("includeTarget", self.include_target)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

