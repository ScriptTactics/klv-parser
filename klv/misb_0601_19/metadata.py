from uas_datalink_local_set import UasDatalinkLocalSet


class Metadata:
    def __init__(self, data):
        self.data = data
        self.key_type = UasDatalinkLocalSet
        self.key_id = 0
        self.length = 0

    def format_data(self, data):
        if self.key_type not in {}:
            raise NotImplementedError(
                "Each UasDatalinkLocalSet must implement its own format_data() function"
            )
        return self.data_to_signed_int(data)

    def data_to_signed_int(self, data):
        return int.from_bytes(data, byteorder="big", signed=True)

    def data_to_unsigned_int(self, data):
        return int.from_bytes(data, byteorder="big", signed=False)

    def __str__(self):
        return f"{self.key_type}={self.key_id}, Length={self.length}, Data={self.format_data(self.data)}"


# Item 2
class PrecisionTimestamp(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.PRECISION_TIMESTAMP

    def format_data(self, data):
        return self.data_to_unsigned_int(data)


# Item 3
class MissionId(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.MISSION_ID


# Item 4
class PlatformTailNumber(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_TAIL_NUMBER


# Item 5
class PlatformHeadingAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_HEADING_ANGLE

    def format_data(self, data):
        return (360 / 65535) * self.data_to_signed_int(data)


# Item 6
class PlatformPitchAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_PITCH_ANGLE

    def format_data(self, data):
        if data.hex() == 8000:
            return "Out of Range"
        return 40 / 65534 * self.data_to_signed_int(data)


# Item 7
class PlatformRollAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ROLL_ANGLE

    def format_data(self, data):
        if data.hex() == 8000:
            return "Out of Range"
        return (1000 / 65534) * self.data_to_signed_int(data)


# Item 8
class PlatformTrueAirspeed(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_TRUE_AIRSPEED

    def format_data(self, data):
        return self.data_to_signed_int(data)


# Item 9
class PlatformIndicatedAirspeed(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_INDICATED_AIRSPEED

    def format_data(self, data):
        return self.data_to_signed_int(data)


# Item 10
class PlatformDesignation(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_DESIGNATION


# Item 11
class ImageSourceSensor(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.IMAGE_SOURCE_SENSOR


# Item 12
class ImageCoordinateSystem(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.IMAGE_COORDINATE_SYSTEM


# Item 13
class SensorLatitude(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_LATITUDE

    def format_data(self, data):
        if data.hex() == 80000000:
            return "Reserved"
        return (180 / 4294967294) * self.data_to_signed_int(data)


# Item 14
class SensorLongitude(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_LONGITUDE

    def format_data(self, data):
        if data.hex() == 80000000:
            return "Reserved"
        return (306 / 4294967294) * self.data_to_signed_int(data)


# Item 15
class SensorTrueAltitude(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_TRUE_ALTITUDE

    def format_data(self, data):
        return (199000 / 65535) * self.data_to_unsigned_int(data) - 900


# Item 16
class SensorHorizontalFieldOfView(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_HORIZONTAL_FOV

    def format_data(self, data):
        return (180 / 65535) * self.data_to_unsigned_int(data)


# Item 17
class SensorVerticalFieldOfView(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_VERTICAL_FOV

    def format_data(self, data):
        return (180 / 65535) * self.data_to_unsigned_int(data)


# Item 18
class SensorRelativeAzimuthAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_AZIMUTH_ANGLE

    def format_data(self, data):
        return (360 / 4294967295) * self.data_to_unsigned_int(data)


# Item 19
class SensorRelativeElevationAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_ELEVATION_ANGLE

    def format_data(self, data):
        if data.hex() == 80000000:
            return "Reserved"
        return (360 / 4294967294) * self.data_to_signed_int(data)


# Item 20
class SensorRelativeRollAngle(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_ROLL_ANGLE

    def format_data(self, data):
        return (360 / 4294967295) * self.data_to_unsigned_int(data)


# Item 21
class SlantRange(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.SLANT_RANGE

    def format_data(self, data):
        return (5000000 / 4294967295) * self.data_to_unsigned_int(data)


# Item 22
class TargetWidth(Metadata):
    def __init__(self, data):
        super.__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_WIDTH

    def format_data(self, data):
        return (10000 / 65535) * self.data_to_unsigned_int(data)


# Item 23
class FrameCenterLatitude(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_LATITUDE

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(data)


# Item 24
class FrameCenterLongitude(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_LONGITUDE

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(data)


# Item 25
class FrameCenterElevationConversion(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_ELEVATION_CONVERSION

    # Default LS_dec
    def format_data(self, data):
        return (19900 / 65535) * self.data_to_unsigned_int(data) - 900


# Item 26
class OffsetCornerLatitudePoint1Conversion(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_1

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 27
class OffsetCornerLongitudePoint1Conversion(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_1

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 28
class OffsetCornerLatitudePoint2(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_2

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 29
class OffsetCornerLongitudePoint2(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_2

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 30
class OffsetCornerLatitudePoint3(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_3

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 31
class OffsetCornerLongitudePoint3(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_3

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 32
class OffsetCornerLatitudePoint4(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_4

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 33
class OffsetCornerLongitudePoint4(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_4

    def format_data(self, data):
        if data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(data)


# Item 34
class IcingDetected(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.ICING_DETECTED


# Item 35
class WindDirection(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.WIND_DIRECTION

    def format_data(self, data):
        return (360 / 65535) * self.data_to_unsigned_int(data)


# Item 36
class WindSpeed(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.WIND_SPEED

    def format_data(self, data):
        return (100 / 255) * self.data_to_unsigned_int(data)


# Item 37
class StaticPressure(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.STATIC_PRESSURE

    def format_data(self, data):
        return (5000 / 65535) * self.data_to_unsigned_int(data)


# Item 38
class DensityAltitude(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.DENSITY_ALTITUDE

    def format_data(self, data):
        return (19900 / 65535) * self.data_to_unsigned_int(data) - 900


# Item 39
class OutsideAirTemperature(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.OUTSIDE_AIR_TEMPERATURE

    def format_data(self, data):
        return self.data_to_signed_int(data)


# Item 40
class TargetLocationLatitude(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_LATITUDE

    def format_data(self, data):
        if data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(data)


# Item 41
class TargetLocationLongitude(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_LONGITUDE

    def format_data(self, data):
        if data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(data)


# Item 42
class TargetLocationElevation(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_ELEVATION

    def format_data(self, data):
        return (19900 / 65535) * self.data_to_unsigned_int(data) - 900


# Item 43
class TargetTrackGateWidth(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_TRACK_GATE_WIDTH

    def format_data(self, data):
        return 2 * self.data_to_unsigned_int(data)


# Item 44
class TargetTrackGateHeight(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_TRACK_GATE_HEIGHT

    def format_data(self, data):
        return 2 * self.data_to_unsigned_int(data)


# Item 45
class TargetErrorEstimateCE90(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_CE90

    def format_data(self, data):
        return (4095 / 65535) * self.data_to_unsigned_int(data)


# Item 46
class TargetErrorEstimateLE90(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_LE90

    def format_data(self, data):
        return (4095 / 65535) * self.data_to_unsigned_int(data)


# Item 47
# TODO Setup bit masking
class GenericFlagData(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.GENERIC_FLAG_DATA

    def format_data(self, data):
        return self.data_to_unsigned_int(data)


# Item 48
class SecurityLocalSet(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.SECURITY_LOCAL_SET


# TODO See https://sightlineapplications.com/misb-standards/MISB-ST-0102.12.pdf


# Item 49
class DifferentialPressure(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.DIFFERENTIAL_PRESSURE

    def format_data(self, data):
        return (5000 / 65535) * self.data_to_unsigned_int(data)


# Item 50
class PlatformAngleOfAttack(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ANGLE_OF_ATTACK

    def format_data(self, data):
        if data == 8000:
            return "Out of Range"
        return (40 / 65534) * self.data_to_signed_int(data)


# Item 51
class PlatformVerticalSpeed(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_VERTICAL_SPEED

    def format_data(self, data):
        if data == 8000:
            return "Out of Range"
        return (360 / 65534) * self.data_to_signed_int(data)


# Item 52
class PlatformSideslipAngle(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE

    def format_data(self, data):
        if data == 8000:
            return "Out of Range"
        return (40 / 65534) * self.data_to_signed_int(data)


# Item 53
class AirfieldBarometricPressure(Metadata):
    def __init__(self, data):
        super().__init__(data)
        self.key_type = UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE

    def format_data(self, data):
        return (5000 / 65535) * self.data_to_unsigned_int(data)
