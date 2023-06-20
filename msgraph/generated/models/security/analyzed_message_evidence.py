from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence, email_sender

from . import alert_evidence

@dataclass
class AnalyzedMessageEvidence(alert_evidence.AlertEvidence):
    # Direction of the email relative to your network. The possible values are: inbound, outbound or intraorg.
    anti_spam_direction: Optional[str] = None
    # Number of attachments in the email.
    attachments_count: Optional[int] = None
    # Delivery action of the email. The possible values are: delivered, deliveredAsSpam, junked, blocked, or replaced.
    delivery_action: Optional[str] = None
    # Location where the email was delivered. The possible values are: inbox, external, junkFolder, quarantine, failed, dropped, deletedFolder or forwarded.
    delivery_location: Optional[str] = None
    # Public-facing identifier for the email that is set by the sending email system.
    internet_message_id: Optional[str] = None
    # Detected language of the email content.
    language: Optional[str] = None
    # Unique identifier for the email, generated by Microsoft 365.
    network_message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The P1 sender.
    p1_sender: Optional[email_sender.EmailSender] = None
    # The P2 sender.
    p2_sender: Optional[email_sender.EmailSender] = None
    # Date and time when the email was received.
    received_date_time: Optional[datetime] = None
    # Email address of the recipient, or email address of the recipient after distribution list expansion.
    recipient_email_address: Optional[str] = None
    # IP address of the last detected mail server that relayed the message.
    sender_ip: Optional[str] = None
    # Subject of the email.
    subject: Optional[str] = None
    # Collection of methods used to detect malware, phishing, or other threats found in the email.
    threat_detection_methods: Optional[List[str]] = None
    # Collection of detection names for malware or other threats found.
    threats: Optional[List[str]] = None
    # Number of embedded URLs in the email.
    url_count: Optional[int] = None
    # Collection of the URLs contained in this email.
    urls: Optional[List[str]] = None
    # Uniform resource name (URN) of the automated investigation where the cluster was identified.
    urn: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnalyzedMessageEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedMessageEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedMessageEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence, email_sender

        from . import alert_evidence, email_sender

        fields: Dict[str, Callable[[Any], None]] = {
            "antiSpamDirection": lambda n : setattr(self, 'anti_spam_direction', n.get_str_value()),
            "attachmentsCount": lambda n : setattr(self, 'attachments_count', n.get_int_value()),
            "deliveryAction": lambda n : setattr(self, 'delivery_action', n.get_str_value()),
            "deliveryLocation": lambda n : setattr(self, 'delivery_location', n.get_str_value()),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "networkMessageId": lambda n : setattr(self, 'network_message_id', n.get_str_value()),
            "p1Sender": lambda n : setattr(self, 'p1_sender', n.get_object_value(email_sender.EmailSender)),
            "p2Sender": lambda n : setattr(self, 'p2_sender', n.get_object_value(email_sender.EmailSender)),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipientEmailAddress": lambda n : setattr(self, 'recipient_email_address', n.get_str_value()),
            "senderIp": lambda n : setattr(self, 'sender_ip', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "threatDetectionMethods": lambda n : setattr(self, 'threat_detection_methods', n.get_collection_of_primitive_values(str)),
            "threats": lambda n : setattr(self, 'threats', n.get_collection_of_primitive_values(str)),
            "urlCount": lambda n : setattr(self, 'url_count', n.get_int_value()),
            "urls": lambda n : setattr(self, 'urls', n.get_collection_of_primitive_values(str)),
            "urn": lambda n : setattr(self, 'urn', n.get_str_value()),
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
        writer.write_str_value("antiSpamDirection", self.anti_spam_direction)
        writer.write_int_value("attachmentsCount", self.attachments_count)
        writer.write_str_value("deliveryAction", self.delivery_action)
        writer.write_str_value("deliveryLocation", self.delivery_location)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_str_value("language", self.language)
        writer.write_str_value("networkMessageId", self.network_message_id)
        writer.write_object_value("p1Sender", self.p1_sender)
        writer.write_object_value("p2Sender", self.p2_sender)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_str_value("recipientEmailAddress", self.recipient_email_address)
        writer.write_str_value("senderIp", self.sender_ip)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_primitive_values("threatDetectionMethods", self.threat_detection_methods)
        writer.write_collection_of_primitive_values("threats", self.threats)
        writer.write_int_value("urlCount", self.url_count)
        writer.write_collection_of_primitive_values("urls", self.urls)
        writer.write_str_value("urn", self.urn)
    

