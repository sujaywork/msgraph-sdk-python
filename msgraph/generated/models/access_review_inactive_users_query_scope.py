from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_query_scope

from . import access_review_query_scope

@dataclass
class AccessReviewInactiveUsersQueryScope(access_review_query_scope.AccessReviewQueryScope):
    odata_type = "#microsoft.graph.accessReviewInactiveUsersQueryScope"
    # Defines the duration of inactivity. Inactivity is based on the last sign in date of the user compared to the access review instance's start date. If this property is not specified, it's assigned the default value PT0S.
    inactive_duration: Optional[timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInactiveUsersQueryScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInactiveUsersQueryScope
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInactiveUsersQueryScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_query_scope

        from . import access_review_query_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "inactiveDuration": lambda n : setattr(self, 'inactive_duration', n.get_timedelta_value()),
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
        writer.write_timedelta_value("inactiveDuration", self.inactive_duration)
    

