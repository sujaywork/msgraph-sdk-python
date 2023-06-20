from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_scope, directory_object, entity, unified_role_assignment_schedule, unified_role_definition, unified_role_eligibility_schedule

from . import entity

@dataclass
class UnifiedRoleScheduleBase(entity.Entity):
    # Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
    app_scope: Optional[app_scope.AppScope] = None
    # Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
    app_scope_id: Optional[str] = None
    # When the schedule was created.
    created_date_time: Optional[datetime] = None
    # Identifier of the object through which this schedule was created.
    created_using: Optional[str] = None
    # The directory object that is the scope of the role eligibility or assignment. Read-only.
    directory_scope: Optional[directory_object.DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
    directory_scope_id: Optional[str] = None
    # When the schedule was last modified.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal that's getting a role assignment or that's eligible for a role through the request.
    principal: Optional[directory_object.DirectoryObject] = None
    # Identifier of the principal that has been granted the role assignment or eligibility.
    principal_id: Optional[str] = None
    # Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
    role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
    role_definition_id: Optional[str] = None
    # The status of the role assignment or eligibility request.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleScheduleBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleScheduleBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentSchedule".casefold():
            from . import unified_role_assignment_schedule

            return unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilitySchedule".casefold():
            from . import unified_role_eligibility_schedule

            return unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule()
        return UnifiedRoleScheduleBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_scope, directory_object, entity, unified_role_assignment_schedule, unified_role_definition, unified_role_eligibility_schedule

        from . import app_scope, directory_object, entity, unified_role_assignment_schedule, unified_role_definition, unified_role_eligibility_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "appScope": lambda n : setattr(self, 'app_scope', n.get_object_value(app_scope.AppScope)),
            "appScopeId": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdUsing": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "directoryScope": lambda n : setattr(self, 'directory_scope', n.get_object_value(directory_object.DirectoryObject)),
            "directoryScopeId": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_object_value("appScope", self.app_scope)
        writer.write_str_value("appScopeId", self.app_scope_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("createdUsing", self.created_using)
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("status", self.status)
    

