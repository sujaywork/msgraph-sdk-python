from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import directory_object

from . import directory_object

@dataclass
class AppRoleAssignment(directory_object.DirectoryObject):
    odata_type = "#microsoft.graph.appRoleAssignment"
    # The identifier (id) for the app role which is assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application has not declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
    app_role_id: Optional[UUID] = None
    # The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime] = None
    # The display name of the user, group, or service principal that was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
    principal_display_name: Optional[str] = None
    # The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
    principal_id: Optional[UUID] = None
    # The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
    principal_type: Optional[str] = None
    # The display name of the resource app's service principal to which the assignment is made.
    resource_display_name: Optional[str] = None
    # The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
    resource_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppRoleAssignment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AppRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_object

        from . import directory_object

        fields: Dict[str, Callable[[Any], None]] = {
            "appRoleId": lambda n : setattr(self, 'app_role_id', n.get_uuid_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "principalDisplayName": lambda n : setattr(self, 'principal_display_name', n.get_str_value()),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_uuid_value()),
            "principalType": lambda n : setattr(self, 'principal_type', n.get_str_value()),
            "resourceDisplayName": lambda n : setattr(self, 'resource_display_name', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_uuid_value()),
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
        writer.write_uuid_value("appRoleId", self.app_role_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("principalDisplayName", self.principal_display_name)
        writer.write_uuid_value("principalId", self.principal_id)
        writer.write_str_value("principalType", self.principal_type)
        writer.write_str_value("resourceDisplayName", self.resource_display_name)
        writer.write_uuid_value("resourceId", self.resource_id)
    

