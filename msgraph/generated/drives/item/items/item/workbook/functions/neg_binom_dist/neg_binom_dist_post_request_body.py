from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class NegBinom_DistPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The cumulative property
    cumulative: Optional[json.Json] = None
    # The numberF property
    number_f: Optional[json.Json] = None
    # The numberS property
    number_s: Optional[json.Json] = None
    # The probabilityS property
    probability_s: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NegBinom_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NegBinom_DistPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return NegBinom_DistPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(json.Json)),
            "numberF": lambda n : setattr(self, 'number_f', n.get_object_value(json.Json)),
            "numberS": lambda n : setattr(self, 'number_s', n.get_object_value(json.Json)),
            "probabilityS": lambda n : setattr(self, 'probability_s', n.get_object_value(json.Json)),
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
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("numberF", self.number_f)
        writer.write_object_value("numberS", self.number_s)
        writer.write_object_value("probabilityS", self.probability_s)
        writer.write_additional_data_value(self.additional_data)
    

