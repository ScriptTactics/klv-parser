from .uas_datalink_local_set import UasDatalinkLocalSet
from ...logger.log_config import logger
import inspect

_OUT_OF_RANGE_STR = "Out of Range"


class Metadata:
    def __init__(self, data, length, id):
        self.data = data
        self.length = length
        self.id = id
        self.key_type = UasDatalinkLocalSet

    def format_data(self):
        if self.key_type in {}:
            raise NotImplementedError(
                "Each UasDatalinkLocalSet must implement its own format_data() function"
            )
        return self.data_to_signed_int(self.data)

    def data_to_signed_int(self, data):
        return int.from_bytes(data, byteorder="big", signed=True)

    def data_to_unsigned_int(self, data):
        return int.from_bytes(data, byteorder="big", signed=False)

    def data_to_str(self, data):
        return data.decode("utf-8")

    def __str__(self):
        return f"{self.key_type}={self.id}, Length={self.length} Data={self.format_data(self.data)}"


# Item 2
class PrecisionTimestamp(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PRECISION_TIMESTAMP

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 3
class MissionId(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.MISSION_ID


# Item 4
class PlatformTailNumber(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_TAIL_NUMBER


# Item 5
class PlatformHeadingAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_HEADING_ANGLE

    def format_data(self):
        return (360 / 65535) * self.data_to_signed_int(self.data)


# Item 6
class PlatformPitchAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_PITCH_ANGLE

    def format_data(self):
        if self.data.hex() == 8000:
            return _OUT_OF_RANGE_STR
        return 40 / 65534 * self.data_to_signed_int(self.data)


# Item 7
class PlatformRollAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ROLL_ANGLE

    def format_data(self):
        if self.data.hex() == 8000:
            return _OUT_OF_RANGE_STR
        return (1000 / 65534) * self.data_to_signed_int(self.data)


# Item 8
class PlatformTrueAirspeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_TRUE_AIRSPEED

    def format_data(self):
        return self.data_to_signed_int(self.data)


# Item 9
class PlatformIndicatedAirspeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_INDICATED_AIRSPEED

    def format_data(self):
        return self.data_to_signed_int(self.data)


# Item 10
class PlatformDesignation(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_DESIGNATION


# Item 11
class ImageSourceSensor(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.IMAGE_SOURCE_SENSOR


# Item 12
class ImageCoordinateSystem(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.IMAGE_COORDINATE_SYSTEM


# Item 13
class SensorLatitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_LATITUDE

    def format_data(self):
        if self.data.hex() == 80000000:
            return "Reserved"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 14
class SensorLongitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_LONGITUDE

    def format_data(self):
        if self.data.hex() == 80000000:
            return "Reserved"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 15
class SensorTrueAltitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_TRUE_ALTITUDE

    def format_data(self):
        return (199000 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 16
class SensorHorizontalFieldOfView(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_HORIZONTAL_FOV

    def format_data(self):
        return (180 / 65535) * self.data_to_unsigned_int(self.data)


# Item 17
class SensorVerticalFieldOfView(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_VERTICAL_FOV

    def format_data(self):
        return (180 / 65535) * self.data_to_unsigned_int(self.data)


# Item 18
class SensorRelativeAzimuthAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_AZIMUTH_ANGLE

    def format_data(self):
        return (360 / 4294967295) * self.data_to_unsigned_int(self.data)


# Item 19
class SensorRelativeElevationAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_ELEVATION_ANGLE

    def format_data(self):
        if self.data.hex() == 80000000:
            return "Reserved"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 20
class SensorRelativeRollAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_RELATIVE_ROLL_ANGLE

    def format_data(self):
        return (360 / 4294967295) * self.data_to_unsigned_int(self.data)


# Item 21
class SlantRange(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SLANT_RANGE

    def format_data(self):
        return (5000000 / 4294967295) * self.data_to_unsigned_int(self.data)


# Item 22
class TargetWidth(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_WIDTH

    def format_data(self):
        return (10000 / 65535) * self.data_to_unsigned_int(self.data)


# Item 23
class FrameCenterLatitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_LATITUDE

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 24
class FrameCenterLongitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_LONGITUDE

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 25
class FrameCenterElevationConversion(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_ELEVATION_CONVERSION

    # Default LS_dec
    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 26
class OffsetCornerLatitudePoint1Conversion(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_1

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 27
class OffsetCornerLongitudePoint1Conversion(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_1

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 28
class OffsetCornerLatitudePoint2(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_2

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 29
class OffsetCornerLongitudePoint2(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_2

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 30
class OffsetCornerLatitudePoint3(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_3

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 31
class OffsetCornerLongitudePoint3(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_3

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 32
class OffsetCornerLatitudePoint4(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_4

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 33
class OffsetCornerLongitudePoint4(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_4

    def format_data(self):
        if self.data.hex() == 8000:
            return "N/A (Off-Earth)"
        return (0.15 / 65534) * self.data_to_signed_int(self.data)


# Item 34
class IcingDetected(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ICING_DETECTED


# Item 35
class WindDirection(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WIND_DIRECTION

    def format_data(self):
        return (360 / 65535) * self.data_to_unsigned_int(self.data)


# Item 36
class WindSpeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WIND_SPEED

    def format_data(self):
        return (100 / 255) * self.data_to_unsigned_int(self.data)


# Item 37
class StaticPressure(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.STATIC_PRESSURE

    def format_data(self):
        return (5000 / 65535) * self.data_to_unsigned_int(self.data)


# Item 38
class DensityAltitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.DENSITY_ALTITUDE

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 39
class OutsideAirTemperature(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OUTSIDE_AIR_TEMPERATURE

    def format_data(self):
        return self.data_to_signed_int(self.data)


# Item 40
class TargetLocationLatitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_LATITUDE

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 41
class TargetLocationLongitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_LONGITUDE

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 42
class TargetLocationElevation(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_LOCATION_ELEVATION

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 43
class TargetTrackGateWidth(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_TRACK_GATE_WIDTH

    def format_data(self):
        return 2 * self.data_to_unsigned_int(self.data)


# Item 44
class TargetTrackGateHeight(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_TRACK_GATE_HEIGHT

    def format_data(self):
        return 2 * self.data_to_unsigned_int(self.data)


# Item 45
class TargetErrorEstimateCE90(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_CE90

    def format_data(self):
        return (4095 / 65535) * self.data_to_unsigned_int(self.data)


# Item 46
class TargetErrorEstimateLE90(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_LE90

    def format_data(self):
        return (4095 / 65535) * self.data_to_unsigned_int(self.data)


# Item 47
# TODO Setup bit masking
class GenericFlagData(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.GENERIC_FLAG_DATA

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 48
class SecurityLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SECURITY_LOCAL_SET


# TODO See https://sightlineapplications.com/misb-standards/MISB-ST-0102.12.pdf


# Item 49
class DifferentialPressure(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.DIFFERENTIAL_PRESSURE

    def format_data(self):
        return (5000 / 65535) * self.data_to_unsigned_int(self.data)


# Item 50
class PlatformAngleOfAttack(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ANGLE_OF_ATTACK

    def format_data(self):
        if self.data == 8000:
            return _OUT_OF_RANGE_STR
        return (40 / 65534) * self.data_to_signed_int(self.data)


# Item 51
class PlatformVerticalSpeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_VERTICAL_SPEED

    def format_data(self):
        if self.data == 8000:
            return _OUT_OF_RANGE_STR
        return (360 / 65534) * self.data_to_signed_int(self.data)


# Item 52
class PlatformSideslipAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE

    def format_data(self):
        if self.data == 8000:
            return _OUT_OF_RANGE_STR
        return (40 / 65534) * self.data_to_signed_int(self.data)


# Item 53
class AirfieldBarometricPressure(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE

    def format_data(self):
        return (5000 / 65535) * self.data_to_unsigned_int(self.data)


# Item 54
class AirfieldElevation(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.AIRFIELD_ELEVATION

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 55
class RelativeHumidity(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.RELATIVE_HUMIDITY

    def format_data(self):
        return (100 / 255) * self.data_to_signed_int(self.data)


# Item 56
class PlatformGroundSpeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_GROUND_SPEED

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 57
class GroundRange(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.GROUND_RANGE

    def format_data(self):
        return (5000000 / 4294967295) * self.data_to_unsigned_int(self.data)


# Item 58
class PlatformFuelRemaining(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_FUEL_REMAINING

    def format_data(self):
        return (10000 / 65535) * self.data_to_unsigned_int(self.data)


# Item 59
class PlatformCallSign(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_CALL_SIGN


# Item 60
class WeaponLoad(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WEAPON_LOAD

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 61
class WeaponFired(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WEAPON_FIRED


# Item 62
class LaserPRFCode(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.LASER_PRF_CODE

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 63
class SensorFieldOfViewName(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_FIELD_OF_VIEW_NAME

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 64
class PlatformMagneticHeading(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_MAGNETIC_HEADING

    def format_data(self):
        return (360 / 65535) * self.data_to_unsigned_int(self.data)


# Item 65
class UASDatalinkLSVersionNumber(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.UAS_DATALINK_LS_VERSION_NUMBER


# Item 66
class Deprecated(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.DEPRECATED


# Item 67
class AlternatePlatformLatitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_LATITUDE

    def format_data(self):
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 68
class AlternatePlatformLongitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_LONGITUDE

    def format_data(self):
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 69
class AlternatePlatformAltitude(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_ALTITUDE

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 70
class AlternatePlatformName(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_NAME


# Item 71
class AlternatePlatformHeading(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_HEADING

    def format_data(self):
        return (360 / 65535) * self.data_to_signed_int(self.data)


# Item 72
class EventStartTime(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.EVENT_START_TIME

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 73
class RTVLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.RTV_LOCAL_SET


# TODO See MISB ST 0806


# Item 74
class VMTILocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.VMTI_LOCAL_SET


# TODO See MISB ST 0903


# Item 75
class SensorEllipsoidHeight(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_ELLIPSOID_HEIGHT

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 76
class AlternatePlatformEllipsoidHeight(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_ELLIPSOID_HEIGHT

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 77
class OperationalMod(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OPERATIONAL_MODE


# Item 78
class FrameCenterHeightAboveEllipsoid(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.FRAME_CENTER_HEIGHT_ABOVE_ELLIPSOID

    def format_data(self):
        return (19900 / 65535) * self.data_to_unsigned_int(self.data) - 900


# Item 79
class SensorNorthVelocity(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_NORTH_VELOCITY

    def format_data(self):
        if self.data == 8000:
            return _OUT_OF_RANGE_STR
        return (654 / 65534) * self.data_to_signed_int(self.data)


# Item 80
class SensorEastVelocity(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_EAST_VELOCITY

    def format_data(self):
        if self.data == 8000:
            return "Out of Range`"
        return (654 / 65534) * self.data_to_signed_int(self.data)


# Item 81
class ImageHorizonPixelPack(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.IMAGE_HORIZON_PIXEL_PACK


# TODO Read Docs


# Item 82
class CornerLatitudePoint1Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LATITUDE_POINT_1_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 83
class CornerLongitudePoint1Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_1_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 84
class CornerLatitudePoint2Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_2_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 85
class CornerLongitudePoint2Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_2_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 86
class CornerLatitudePoint3Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_3_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 87
class CornerLongitudePoint3Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_3_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 88
class CornerLatitudePoint4Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_4_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 89
class CornerLongitudePoint4Full(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_4_FULL

    def format_data(self):
        if self.data == 80000000:
            return "N/A (Off-Earth)"
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 90
class PlatformPitchAngleFull(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_PITCH_ANGLE_FULL

    def format_data(self):
        if self.data == 80000000:
            return _OUT_OF_RANGE_STR
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 91
class PlatformRollAngleFull(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ROLL_ANGLE_FULL

    def format_data(self):
        if self.data == 80000000:
            return _OUT_OF_RANGE_STR
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 92
class PlatformAngleOfAttackFull(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_ANGLE_OF_ATTACK_FULL

    def format_data(self):
        if self.data == 80000000:
            return _OUT_OF_RANGE_STR
        return (180 / 4294967294) * self.data_to_signed_int(self.data)


# Item 93
class PlatformSideslipAngleFull(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE_FULL

    def format_data(self):
        if self.data == 80000000:
            return _OUT_OF_RANGE_STR
        return (360 / 4294967294) * self.data_to_signed_int(self.data)


# Item 94
class MIISCoreIdentifier(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.MIIS_CORE_IDENTIFIER


# TODO MISB ST 1204


# Item 95
class SARMotionImageryLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SAR_MOTION_IMAGERY_SET


# TODO MISB ST 1206


# Item 96
class TargetWidthExtended(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_WIDTH_EXTENDED


# TODO IMAPB(0,1500000, Length, Soft_val)


# Item 97
class RangeImageLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.RANGE_IMAGE_LOCAL_SET


# TODO MISB ST 1002


# Item 98
class GeoRegistratoinLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.GEO_REGISTRATION_LOCAL_SET


# TODO MISB ST 1601


# Item 99
class CompositeImagingLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.COMPOSITE_IMAGING_LOCAL_SET


# TODO MISB ST 1602


# Item 100
class SegmentLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SEGMENT_LOCAL_SET


# TODO MISB ST 1607


# Item 101
class AmendLocalSet(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.AMEND_LOCAL_SET


# TODO MISB ST 1607


# Item 102
class SDCCFLP(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SDCC_FLP


# TODO MISB ST 1010


# Item 103
class DensityAltitudeExtended(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.DENSITY_ALTITUDE_EXTENDED


# TODO IMAPB(-900,40000, Length, Soft_val)


# Item 104
class SensorEllipsoidHeightExtended(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_ELLIPSOID_HEIGHT_EXTENDED


# TODO IMAPB(-900,40000, Length, Soft_val)


# Item 105
class AlternatePlatformEllipsoidHeightExtended(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTERNATE_PLATFORM_ELLIPSOID_HEIGHT_EXTENDED


# TODO IMAPB(-900,40000, Length, Soft_val)


# Item 106
class StreamDesignator(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.STREAM_DESIGNATOR


# Item 107
class OperationalBase(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.OPERATIONAL_BASE


# Item 108
class BroadcastSource(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.BROADCAST_SOURCE

    def format_data(self):
        return self.data_to_str(data)


# Item 109
class RangeToRecoveryLocation(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.RANGE_TO_RECOVERY_LOCATION


# Item 110
class TimeAirborne(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TIME_AIRBORNE

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 111
class PropulsionUnitSpeed(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PROPULSION_UNIT_SPEED

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 112
class PlatformCourseAngle(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_COURSE_ANGLE


# Item 113
class AltitudeAGL(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ALTITUDE_AGL


# Item 114
class RadarAltimeter(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.RADAR_ALTIMITER


# Item 115
class ControlCommand(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CONTROL_COMMAND


# Item 116
class ControlCommandVerificationList(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CONTROL_COMMAND_VERIFICATION_LIST


# Item 117
class SensorAzimuthRate(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_AZIMUTH_RATE


# Item 118
class SensorElevationRate(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_ELEVATION_RATE


# Item 119
class SensorRollRate(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_ROLL_RATE


# Item 120
class OnBoardMiStoragePercentageFull(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ON_BOARD_MI_STORAGE_PERCENT_FULL


# Item 121
class ActiveWavelengthList(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ACTIVE_WAVELENGTH_LIST


# Item 122
class CountryCodes(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.COUNTRY_CODES


# Item 123
class NumberOfNAVSATSInView(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.NUMBER_OF_NAVSATS_IN_VIEW

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 124
class PositioningMethodSource(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.POSITIONING_METHOD_SOURCE

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 125
class PlatformStatus(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PLATFORM_STATUS

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 126
class SensorControlMode(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_CONTROL_MODE

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 127
class SensorFrameRatePack(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.SENSOR_FRAME_RATE_PACK


# Item 128
class WavelengthsList(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WAVELENGTHS_LIST


# Item 129
class TargetID(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TARGET_ID


# Item 130
class AirbaseLocations(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.AIR_BASE_LOCATIONS


# Item 131
class TakeOffTime(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TAKE_OFF_TIME

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 132
class TransmissionFrequency(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.TRANSMISSION_FREQUENCY


# Item 133
class OnBoardMIStorageCapacity(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ON_BOARD_MI_STORAGE_CAPACITY

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 134
class ZoomPercentage(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ZOOM_PERCENTAGE


# TODO IMAPB(0,100.0, Length, Soft val)


# Item 135
class CommunicationsMethod(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.COMMUNICATIONS_METHOD


# Item 136
class LeapSeconds(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.LEAP_SECONDS

    def format_data(self):
        return self.data_to_signed_int(self.data)


# Item 137
class CorrectionOffset(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CORRECTION_OFFSET

    def format_data(self):
        return self.data_to_unsigned_int(self.data)


# Item 138
class PayloadList(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.PAYLOAD_LIST


# Item 139
class ActivePayloads(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.ACTIVE_PAYLOADS


# Item 140
class WeaponStores(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WEAPON_STORES


# Item 141
class WaypointList(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.WAYPOINT_LIST


# Item 142
class ViewDomain(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.VIEW_DOMAIN


class Checksum(Metadata):
    def __init__(self, data, length, id):
        super().__init__(data, length, id)
        self.key_type = UasDatalinkLocalSet.CHECKSUM


class_map = {
    UasDatalinkLocalSet.CHECKSUM: Checksum,
    UasDatalinkLocalSet.PRECISION_TIMESTAMP: PrecisionTimestamp,
    UasDatalinkLocalSet.MISSION_ID: MissionId,
    UasDatalinkLocalSet.PLATFORM_TAIL_NUMBER: PlatformTailNumber,
    UasDatalinkLocalSet.PLATFORM_HEADING_ANGLE: PlatformHeadingAngle,
    UasDatalinkLocalSet.PLATFORM_PITCH_ANGLE: PlatformPitchAngle,
    UasDatalinkLocalSet.PLATFORM_ROLL_ANGLE: PlatformRollAngle,
    UasDatalinkLocalSet.PLATFORM_TRUE_AIRSPEED: PlatformTrueAirspeed,
    UasDatalinkLocalSet.PLATFORM_INDICATED_AIRSPEED: PlatformIndicatedAirspeed,
    UasDatalinkLocalSet.PLATFORM_DESIGNATION: PlatformDesignation,
    UasDatalinkLocalSet.IMAGE_SOURCE_SENSOR: ImageSourceSensor,
    UasDatalinkLocalSet.IMAGE_COORDINATE_SYSTEM: ImageCoordinateSystem,
    UasDatalinkLocalSet.SENSOR_LATITUDE: SensorLatitude,
    UasDatalinkLocalSet.SENSOR_LONGITUDE: SensorLongitude,
    UasDatalinkLocalSet.SENSOR_TRUE_ALTITUDE: SensorTrueAltitude,
    UasDatalinkLocalSet.SENSOR_HORIZONTAL_FOV: SensorHorizontalFieldOfView,
    UasDatalinkLocalSet.SENSOR_VERTICAL_FOV: SensorVerticalFieldOfView,
    UasDatalinkLocalSet.SENSOR_RELATIVE_AZIMUTH_ANGLE: SensorRelativeAzimuthAngle,
    UasDatalinkLocalSet.SENSOR_RELATIVE_ELEVATION_ANGLE: SensorRelativeElevationAngle,
    UasDatalinkLocalSet.SENSOR_RELATIVE_ROLL_ANGLE: SensorRelativeRollAngle,
    UasDatalinkLocalSet.SLANT_RANGE: SlantRange,
    UasDatalinkLocalSet.TARGET_WIDTH: TargetWidth,
    UasDatalinkLocalSet.FRAME_CENTER_LATITUDE: FrameCenterLatitude,
    UasDatalinkLocalSet.FRAME_CENTER_LONGITUDE: FrameCenterLongitude,
    UasDatalinkLocalSet.FRAME_CENTER_ELEVATION_CONVERSION: FrameCenterElevationConversion,
    UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_1: OffsetCornerLatitudePoint1Conversion,
    UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_1: OffsetCornerLongitudePoint1Conversion,
    UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_2: OffsetCornerLatitudePoint2,
    UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_2: OffsetCornerLongitudePoint2,
    UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_3: OffsetCornerLatitudePoint3,
    UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_3: OffsetCornerLongitudePoint3,
    UasDatalinkLocalSet.OFFSET_CORNER_LATITUDE_POINT_4: OffsetCornerLatitudePoint4,
    UasDatalinkLocalSet.OFFSET_CORNER_LONGITUDE_POINT_4: OffsetCornerLongitudePoint4,
    UasDatalinkLocalSet.ICING_DETECTED: IcingDetected,
    UasDatalinkLocalSet.WIND_DIRECTION: WindDirection,
    UasDatalinkLocalSet.WIND_SPEED: WindSpeed,
    UasDatalinkLocalSet.STATIC_PRESSURE: StaticPressure,
    UasDatalinkLocalSet.DENSITY_ALTITUDE: DensityAltitude,
    UasDatalinkLocalSet.OUTSIDE_AIR_TEMPERATURE: OutsideAirTemperature,
    UasDatalinkLocalSet.TARGET_LOCATION_LATITUDE: TargetLocationLatitude,
    UasDatalinkLocalSet.TARGET_LOCATION_LONGITUDE: TargetLocationLongitude,
    UasDatalinkLocalSet.TARGET_LOCATION_ELEVATION: TargetLocationElevation,
    UasDatalinkLocalSet.TARGET_TRACK_GATE_WIDTH: TargetTrackGateWidth,
    UasDatalinkLocalSet.TARGET_TRACK_GATE_HEIGHT: TargetTrackGateHeight,
    UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_CE90: TargetErrorEstimateCE90,
    UasDatalinkLocalSet.TARGET_ERROR_ESTIMATE_LE90: TargetErrorEstimateLE90,
    UasDatalinkLocalSet.GENERIC_FLAG_DATA: GenericFlagData,
    UasDatalinkLocalSet.SECURITY_LOCAL_SET: SecurityLocalSet,
    UasDatalinkLocalSet.DIFFERENTIAL_PRESSURE: DifferentialPressure,
    UasDatalinkLocalSet.PLATFORM_ANGLE_OF_ATTACK: PlatformAngleOfAttack,
    UasDatalinkLocalSet.PLATFORM_VERTICAL_SPEED: PlatformVerticalSpeed,
    UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE: PlatformSideslipAngle,
    UasDatalinkLocalSet.AIRFIELD_BAROMETRIC_PRESSURE: AirfieldBarometricPressure,
    UasDatalinkLocalSet.AIRFIELD_ELEVATION: AirfieldElevation,
    UasDatalinkLocalSet.RELATIVE_HUMIDITY: RelativeHumidity,
    UasDatalinkLocalSet.PLATFORM_GROUND_SPEED: PlatformGroundSpeed,
    UasDatalinkLocalSet.GROUND_RANGE: GroundRange,
    UasDatalinkLocalSet.PLATFORM_FUEL_REMAINING: PlatformFuelRemaining,
    UasDatalinkLocalSet.PLATFORM_CALL_SIGN: PlatformCallSign,
    UasDatalinkLocalSet.WEAPON_LOAD: WeaponLoad,
    UasDatalinkLocalSet.WEAPON_FIRED: WeaponFired,
    UasDatalinkLocalSet.LASER_PRF_CODE: LaserPRFCode,
    UasDatalinkLocalSet.SENSOR_FIELD_OF_VIEW_NAME: SensorFieldOfViewName,
    UasDatalinkLocalSet.PLATFORM_MAGNETIC_HEADING: PlatformMagneticHeading,
    UasDatalinkLocalSet.UAS_DATALINK_LS_VERSION_NUMBER: UASDatalinkLSVersionNumber,
    UasDatalinkLocalSet.DEPRECATED: Deprecated,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_LATITUDE: AlternatePlatformLatitude,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_LONGITUDE: AlternatePlatformLongitude,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_ALTITUDE: AlternatePlatformAltitude,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_NAME: AlternatePlatformName,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_HEADING: AlternatePlatformHeading,
    UasDatalinkLocalSet.EVENT_START_TIME: EventStartTime,
    UasDatalinkLocalSet.RTV_LOCAL_SET: RTVLocalSet,
    UasDatalinkLocalSet.VMTI_LOCAL_SET: VMTILocalSet,
    UasDatalinkLocalSet.SENSOR_ELLIPSOID_HEIGHT: SensorEllipsoidHeight,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_ELLIPSOID_HEIGHT: AlternatePlatformEllipsoidHeight,
    UasDatalinkLocalSet.OPERATIONAL_MODE: OperationalMod,
    UasDatalinkLocalSet.FRAME_CENTER_HEIGHT_ABOVE_ELLIPSOID: FrameCenterHeightAboveEllipsoid,
    UasDatalinkLocalSet.SENSOR_NORTH_VELOCITY: SensorNorthVelocity,
    UasDatalinkLocalSet.SENSOR_EAST_VELOCITY: SensorEastVelocity,
    UasDatalinkLocalSet.IMAGE_HORIZON_PIXEL_PACK: ImageHorizonPixelPack,
    UasDatalinkLocalSet.CORNER_LATITUDE_POINT_1_FULL: CornerLatitudePoint1Full,
    UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_1_FULL: CornerLongitudePoint1Full,
    UasDatalinkLocalSet.CORNER_LATITUDE_POINT_2_FULL: CornerLatitudePoint2Full,
    UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_2_FULL: CornerLongitudePoint2Full,
    UasDatalinkLocalSet.CORNER_LATITUDE_POINT_3_FULL: CornerLatitudePoint3Full,
    UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_3_FULL: CornerLongitudePoint3Full,
    UasDatalinkLocalSet.CORNER_LATITUDE_POINT_4_FULL: CornerLatitudePoint4Full,
    UasDatalinkLocalSet.CORNER_LONGITUDE_POINT_4_FULL: CornerLongitudePoint4Full,
    UasDatalinkLocalSet.PLATFORM_PITCH_ANGLE_FULL: PlatformPitchAngleFull,
    UasDatalinkLocalSet.PLATFORM_ROLL_ANGLE_FULL: PlatformRollAngleFull,
    UasDatalinkLocalSet.PLATFORM_ANGLE_OF_ATTACK_FULL: PlatformAngleOfAttackFull,
    UasDatalinkLocalSet.PLATFORM_SIDESLIP_ANGLE_FULL: PlatformSideslipAngleFull,
    UasDatalinkLocalSet.MIIS_CORE_IDENTIFIER: MIISCoreIdentifier,
    UasDatalinkLocalSet.SAR_MOTION_IMAGERY_SET: SARMotionImageryLocalSet,
    UasDatalinkLocalSet.TARGET_WIDTH_EXTENDED: TargetWidthExtended,
    UasDatalinkLocalSet.RANGE_IMAGE_LOCAL_SET: RangeImageLocalSet,
    UasDatalinkLocalSet.GEO_REGISTRATION_LOCAL_SET: GeoRegistratoinLocalSet,
    UasDatalinkLocalSet.COMPOSITE_IMAGING_LOCAL_SET: CompositeImagingLocalSet,
    UasDatalinkLocalSet.SEGMENT_LOCAL_SET: SegmentLocalSet,
    UasDatalinkLocalSet.AMEND_LOCAL_SET: AmendLocalSet,
    UasDatalinkLocalSet.SDCC_FLP: SDCCFLP,
    UasDatalinkLocalSet.DENSITY_ALTITUDE_EXTENDED: DensityAltitudeExtended,
    UasDatalinkLocalSet.SENSOR_ELLIPSOID_HEIGHT_EXTENDED: SensorEllipsoidHeightExtended,
    UasDatalinkLocalSet.ALTERNATE_PLATFORM_ELLIPSOID_HEIGHT_EXTENDED: AlternatePlatformEllipsoidHeightExtended,
    UasDatalinkLocalSet.STREAM_DESIGNATOR: StreamDesignator,
    UasDatalinkLocalSet.OPERATIONAL_BASE: OperationalBase,
    UasDatalinkLocalSet.BROADCAST_SOURCE: BroadcastSource,
    UasDatalinkLocalSet.RANGE_TO_RECOVERY_LOCATION: RangeToRecoveryLocation,
    UasDatalinkLocalSet.TIME_AIRBORNE: TimeAirborne,
    UasDatalinkLocalSet.PROPULSION_UNIT_SPEED: PropulsionUnitSpeed,
    UasDatalinkLocalSet.PLATFORM_COURSE_ANGLE: PlatformCourseAngle,
    UasDatalinkLocalSet.ALTITUDE_AGL: AltitudeAGL,
    UasDatalinkLocalSet.RADAR_ALTIMITER: RadarAltimeter,
    UasDatalinkLocalSet.CONTROL_COMMAND: ControlCommand,
    UasDatalinkLocalSet.CONTROL_COMMAND_VERIFICATION_LIST: ControlCommandVerificationList,
    UasDatalinkLocalSet.SENSOR_AZIMUTH_RATE: SensorAzimuthRate,
    UasDatalinkLocalSet.SENSOR_ELEVATION_RATE: SensorElevationRate,
    UasDatalinkLocalSet.SENSOR_ROLL_RATE: SensorRollRate,
    UasDatalinkLocalSet.ON_BOARD_MI_STORAGE_PERCENT_FULL: OnBoardMiStoragePercentageFull,
    UasDatalinkLocalSet.ACTIVE_WAVELENGTH_LIST: ActiveWavelengthList,
    UasDatalinkLocalSet.COUNTRY_CODES: CountryCodes,
    UasDatalinkLocalSet.NUMBER_OF_NAVSATS_IN_VIEW: NumberOfNAVSATSInView,
    UasDatalinkLocalSet.POSITIONING_METHOD_SOURCE: PositioningMethodSource,
    UasDatalinkLocalSet.PLATFORM_STATUS: PlatformStatus,
    UasDatalinkLocalSet.SENSOR_CONTROL_MODE: SensorControlMode,
    UasDatalinkLocalSet.SENSOR_FRAME_RATE_PACK: SensorFrameRatePack,
    UasDatalinkLocalSet.WAVELENGTHS_LIST: WavelengthsList,
    UasDatalinkLocalSet.TARGET_ID: TargetID,
    UasDatalinkLocalSet.AIR_BASE_LOCATIONS: AirbaseLocations,
    UasDatalinkLocalSet.TAKE_OFF_TIME: TakeOffTime,
    UasDatalinkLocalSet.TRANSMISSION_FREQUENCY: TransmissionFrequency,
    UasDatalinkLocalSet.ON_BOARD_MI_STORAGE_CAPACITY: OnBoardMIStorageCapacity,
    UasDatalinkLocalSet.ZOOM_PERCENTAGE: ZoomPercentage,
    UasDatalinkLocalSet.COMMUNICATIONS_METHOD: CommunicationsMethod,
    UasDatalinkLocalSet.LEAP_SECONDS: LeapSeconds,
    UasDatalinkLocalSet.CORRECTION_OFFSET: CorrectionOffset,
    UasDatalinkLocalSet.PAYLOAD_LIST: PayloadList,
    UasDatalinkLocalSet.ACTIVE_PAYLOADS: ActivePayloads,
    UasDatalinkLocalSet.WEAPON_STORES: WeaponStores,
    UasDatalinkLocalSet.WAYPOINT_LIST: WaypointList,
    UasDatalinkLocalSet.VIEW_DOMAIN: ViewDomain,
}
