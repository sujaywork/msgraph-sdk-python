from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_list_item

@dataclass
class IosNetworkUsageRule(AdditionalDataHolder, Parsable):
    """
    Network Usage Rules allow enterprises to specify how managed apps use networks, such as cellular data networks.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # If set to true, corresponding managed apps will not be allowed to use cellular data when roaming.
    cellular_data_block_when_roaming: Optional[bool] = None
    # If set to true, corresponding managed apps will not be allowed to use cellular data at any time.
    cellular_data_blocked: Optional[bool] = None
    # Information about the managed apps that this rule is going to apply to. This collection can contain a maximum of 500 elements.
    managed_apps: Optional[List[app_list_item.AppListItem]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosNetworkUsageRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosNetworkUsageRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosNetworkUsageRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_list_item

        from . import app_list_item

        fields: Dict[str, Callable[[Any], None]] = {
            "cellularDataBlockWhenRoaming": lambda n : setattr(self, 'cellular_data_block_when_roaming', n.get_bool_value()),
            "cellularDataBlocked": lambda n : setattr(self, 'cellular_data_blocked', n.get_bool_value()),
            "managedApps": lambda n : setattr(self, 'managed_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("cellularDataBlockWhenRoaming", self.cellular_data_block_when_roaming)
        writer.write_bool_value("cellularDataBlocked", self.cellular_data_blocked)
        writer.write_collection_of_object_values("managedApps", self.managed_apps)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

