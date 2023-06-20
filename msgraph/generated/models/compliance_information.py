from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import certification_control

@dataclass
class ComplianceInformation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Collection of the certification controls associated with certification
    certification_controls: Optional[List[certification_control.CertificationControl]] = None
    # Compliance certification name (for example, ISO 27018:2014, GDPR, FedRAMP, NIST 800-171)
    certification_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComplianceInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ComplianceInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import certification_control

        from . import certification_control

        fields: Dict[str, Callable[[Any], None]] = {
            "certificationControls": lambda n : setattr(self, 'certification_controls', n.get_collection_of_object_values(certification_control.CertificationControl)),
            "certificationName": lambda n : setattr(self, 'certification_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("certificationControls", self.certification_controls)
        writer.write_str_value("certificationName", self.certification_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

