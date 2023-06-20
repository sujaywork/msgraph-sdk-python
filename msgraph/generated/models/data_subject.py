from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DataSubject(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Email of the data subject.
    email: Optional[str] = None
    # First name of the data subject.
    first_name: Optional[str] = None
    # Last Name of the data subject.
    last_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The country/region of residency. The residency information is uesed only for internal reporting but not for the content search.
    residency: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSubject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataSubject
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DataSubject()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "residency": lambda n : setattr(self, 'residency', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("residency", self.residency)
        writer.write_additional_data_value(self.additional_data)
    

