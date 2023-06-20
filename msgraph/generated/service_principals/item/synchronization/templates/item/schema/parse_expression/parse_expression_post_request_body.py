from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import attribute_definition, expression_input_object

@dataclass
class ParseExpressionPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The expression property
    expression: Optional[str] = None
    # The targetAttributeDefinition property
    target_attribute_definition: Optional[attribute_definition.AttributeDefinition] = None
    # The testInputObject property
    test_input_object: Optional[expression_input_object.ExpressionInputObject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParseExpressionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParseExpressionPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ParseExpressionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import attribute_definition, expression_input_object

        from ........models import attribute_definition, expression_input_object

        fields: Dict[str, Callable[[Any], None]] = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "targetAttributeDefinition": lambda n : setattr(self, 'target_attribute_definition', n.get_object_value(attribute_definition.AttributeDefinition)),
            "testInputObject": lambda n : setattr(self, 'test_input_object', n.get_object_value(expression_input_object.ExpressionInputObject)),
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
        writer.write_str_value("expression", self.expression)
        writer.write_object_value("targetAttributeDefinition", self.target_attribute_definition)
        writer.write_object_value("testInputObject", self.test_input_object)
        writer.write_additional_data_value(self.additional_data)
    

