from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import browser_shared_cookie, browser_site

@dataclass
class PublishPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The revision property
    revision: Optional[str] = None
    # The sharedCookies property
    shared_cookies: Optional[List[browser_shared_cookie.BrowserSharedCookie]] = None
    # The sites property
    sites: Optional[List[browser_site.BrowserSite]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublishPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PublishPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PublishPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import browser_shared_cookie, browser_site

        from .......models import browser_shared_cookie, browser_site

        fields: Dict[str, Callable[[Any], None]] = {
            "revision": lambda n : setattr(self, 'revision', n.get_str_value()),
            "sharedCookies": lambda n : setattr(self, 'shared_cookies', n.get_collection_of_object_values(browser_shared_cookie.BrowserSharedCookie)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(browser_site.BrowserSite)),
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
        writer.write_str_value("revision", self.revision)
        writer.write_collection_of_object_values("sharedCookies", self.shared_cookies)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_additional_data_value(self.additional_data)
    

