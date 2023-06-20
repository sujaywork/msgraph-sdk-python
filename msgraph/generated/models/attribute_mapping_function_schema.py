from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping_parameter_schema, entity

from . import entity

@dataclass
class AttributeMappingFunctionSchema(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters property
    parameters: Optional[List[attribute_mapping_parameter_schema.AttributeMappingParameterSchema]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMappingFunctionSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMappingFunctionSchema
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AttributeMappingFunctionSchema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping_parameter_schema, entity

        from . import attribute_mapping_parameter_schema, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(attribute_mapping_parameter_schema.AttributeMappingParameterSchema)),
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
        writer.write_collection_of_object_values("parameters", self.parameters)
    

