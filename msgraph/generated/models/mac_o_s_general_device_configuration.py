from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_list_item, app_list_type, device_configuration, required_password_type

from . import device_configuration

@dataclass
class MacOSGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.macOSGeneralDeviceConfiguration"
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[app_list_type.AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
    # An email address lacking a suffix that matches any of these strings will be considered out-of-domain.
    email_in_domain_suffixes: Optional[List[str]] = None
    # Block simple passwords.
    password_block_simple: Optional[bool] = None
    # Number of days before the password expires.
    password_expiration_days: Optional[int] = None
    # Number of character sets a password must contain. Valid values 0 to 4
    password_minimum_character_set_count: Optional[int] = None
    # Minimum length of passwords.
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity required before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Minutes of inactivity required before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passwords to block.
    password_previous_password_block_count: Optional[int] = None
    # Whether or not to require a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[required_password_type.RequiredPasswordType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSGeneralDeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOSGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_list_item, app_list_type, device_configuration, required_password_type

        from . import app_list_item, app_list_type, device_configuration, required_password_type

        fields: Dict[str, Callable[[Any], None]] = {
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "emailInDomainSuffixes": lambda n : setattr(self, 'email_in_domain_suffixes', n.get_collection_of_primitive_values(str)),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
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
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_collection_of_primitive_values("emailInDomainSuffixes", self.email_in_domain_suffixes)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
    

