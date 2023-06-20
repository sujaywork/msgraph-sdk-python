from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import broadcast_meeting_audience, broadcast_meeting_caption_settings

@dataclass
class BroadcastMeetingSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Defines who can join the Teams live event. Possible values are listed in the following table.
    allowed_audience: Optional[broadcast_meeting_audience.BroadcastMeetingAudience] = None
    # Caption settings of a Teams live event.
    captions: Optional[broadcast_meeting_caption_settings.BroadcastMeetingCaptionSettings] = None
    # Indicates whether attendee report is enabled for this Teams live event. Default value is false.
    is_attendee_report_enabled: Optional[bool] = None
    # Indicates whether Q&A is enabled for this Teams live event. Default value is false.
    is_question_and_answer_enabled: Optional[bool] = None
    # Indicates whether recording is enabled for this Teams live event. Default value is false.
    is_recording_enabled: Optional[bool] = None
    # Indicates whether video on demand is enabled for this Teams live event. Default value is false.
    is_video_on_demand_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BroadcastMeetingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BroadcastMeetingSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BroadcastMeetingSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import broadcast_meeting_audience, broadcast_meeting_caption_settings

        from . import broadcast_meeting_audience, broadcast_meeting_caption_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedAudience": lambda n : setattr(self, 'allowed_audience', n.get_enum_value(broadcast_meeting_audience.BroadcastMeetingAudience)),
            "captions": lambda n : setattr(self, 'captions', n.get_object_value(broadcast_meeting_caption_settings.BroadcastMeetingCaptionSettings)),
            "isAttendeeReportEnabled": lambda n : setattr(self, 'is_attendee_report_enabled', n.get_bool_value()),
            "isQuestionAndAnswerEnabled": lambda n : setattr(self, 'is_question_and_answer_enabled', n.get_bool_value()),
            "isRecordingEnabled": lambda n : setattr(self, 'is_recording_enabled', n.get_bool_value()),
            "isVideoOnDemandEnabled": lambda n : setattr(self, 'is_video_on_demand_enabled', n.get_bool_value()),
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
        writer.write_enum_value("allowedAudience", self.allowed_audience)
        writer.write_object_value("captions", self.captions)
        writer.write_bool_value("isAttendeeReportEnabled", self.is_attendee_report_enabled)
        writer.write_bool_value("isQuestionAndAnswerEnabled", self.is_question_and_answer_enabled)
        writer.write_bool_value("isRecordingEnabled", self.is_recording_enabled)
        writer.write_bool_value("isVideoOnDemandEnabled", self.is_video_on_demand_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

