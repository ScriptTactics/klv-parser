from enum import Enum


class UasDatalinkLocalSet(Enum):
    CHECKSUM = 1
    PRECISION_TIMESTAMP = 2
    MISSION_ID = 3
    PLATFORM_TAIL_NUMBER = 4
    PLATFORM_HEADING_ANGLE = 5
    PLATFORM_PITCH_ANGLE = 6
    PLATFORM_ROLL_ANGLE = 7
    PLATFORM_TRUE_AIRSPEED = 8
    PLATFORM_INDICATED_AIRSPEED = 9
    PLATFORM_DESIGNATION = 10
    IMAGE_SOURCE_SENSOR = 11
    IMAGE_COORDINATE_SYSTEM = 12
    SENSOR_LATITUDE = 13
    SENSOR_LONGITUDE = 14
    SENSOR_TRUE_ALTITUDE = 15
    SENSOR_HORIZONTAL_FOV = 16
    SENSOR_VERTICAL_FOV = 17
    SENSOR_RELATIVE_AZIMUTH_ANGLE = 18
    SENSOR_RELATIVE_ELEVATION_ANGLE = 19
    SENSOR_RELATIVE_ROLL_ANGLE = 20
    SLANT_RANGE = 21
    TARGET_WIDTH = 22
    FRAME_CENTER_LATITUDE = 23
    FRAME_CENTER_LONGITUDE = 24
    FRAME_CENTER_ELEVATION_CONVERSION = 25
    OFFSET_CORNER_LATITUDE_POINT_1 = 26
    OFFSET_CORNER_LONGITUDE_POINT_1 = 27
    OFFSET_CORNER_LATITUDE_POINT_2 = 28
    OFFSET_CORNER_LONGITUDE_POINT_2 = 29
    OFFSET_CORNER_LATITUDE_POINT_3 = 30
    OFFSET_CORNER_LONGITUDE_POINT_3 = 31
    OFFSET_CORNER_LATITUDE_POINT_4 = 32
    OFFSET_CORNER_LONGITUDE_POINT_4 = 33
    ICING_DETECTED = 34
    WIND_DIRECTION = 35
    WIND_SPEED = 36
    STATIC_PRESSURE = 37
    DENSITY_ALTITUDE = 38
    OUTSIDE_AIR_TEMPERATURE = 39
    TARGET_LOCATION_LATITUDE = 40
    TARGET_LOCATION_LONGITUDE = 41
    TARGET_LOCATION_ELEVATION = 42
    TARGET_TRACK_GATE_WIDTH = 43
    TARGET_TRACK_GATE_HEIGHT = 44
    TARGET_ERROR_ESTIMATE_CE90 = 45
    TARGET_ERROR_ESTIMATE_LE90 = 46
    GENERIC_FLAG_DATA = 47
    SECURITY_LOCAL_SET = 48
    DIFFERENTIAL_PRESSURE = 49
    PLATFORM_ANGLE_OF_ATTACK = 50
    PLATFORM_VERTICAL_SPEED = 51
    PLATFORM_SIDESLIP_ANGLE = 52
    AIRFIELD_BAROMETRIC_PRESSURE = 53
    AIRFIELD_ELEVATION = 54
    RELATIVE_HUMIDITY = 55
    PLATFORM_GROUND_SPEED = 56
    GROUND_RANGE = 57
    PLATFORM_FUEL_REMAINING = 58
    PLATFORM_CALL_SIGN = 59
    WEAPON_LOAD = 60
    WEAPON_FIRED = 61
    LASER_PRF_CODE = 62
    SENSOR_FIELD_OF_VIEW_NAME = 63
    PLATFORM_MAGNETIC_HEADING = 64
    UAS_DATALINK_LS_VERSION_NUMBER = 65
    DEPRECATED = 66
    ALTERNATE_PLATFORM_LATITUDE = 67
    ALTERNATE_PLATFORM_LONGITUDE = 68
    ALTERNATE_PLATFORM_ALTITUDE = 69
    ALTERNATE_PLATFORM_NAME = 70
    ALTERNATE_PLATFORM_HEADING = 71
    EVENT_START_TIME = 72
    RTV_LOCAL_SET = 73
    VMTI_LOCAL_SET = 74
    SENSOR_ELLIPSOID_HEIGHT = 75
    ALTERNATE_PLATFORM_ELLIPSOID_HEIGHT = 76
    OPERATIONAL_MODE = 77
    FRAME_CENTER_HEIGHT_ABOVE_ELLIPSOID = 78
    SENSOR_NORTH_VELOCITY = 79
    SENSOR_EAST_VELOCITY = 80
    IMAGE_HORIZON_PIXEL_PACK = 81
    CORNER_LATITUDE_POINT_1_FULL = 82
    CORNER_LONGITUDE_POINT_1_FULL = 83
    CORNER_LATITUDE_POINT_2_FULL = 84
    CORNER_LONGITUDE_POINT_2_FULL = 85
    CORNER_LATITUDE_POINT_3_FULL = 86
    CORNER_LONGITUDE_POINT_3_FULL = 87
    CORNER_LATITUDE_POINT_4_FULL = 88
    CORNER_LONGITUDE_POINT_4_FULL = 89
    PLATFORM_PITCH_ANGLE_FULL = 90
    PLATFORM_ROLL_ANGLE_FULL = 91
    PLATFORM_ANGLE_OF_ATTACK_FULL = 92
    PLATFORM_SIDESLIP_ANGLE_FULL = 93
    MIIS_CORE_IDENTIFIER = 94
    SAR_MOTION_IMAGERY_SET = 95
    TARGET_WIDTH_EXTENDED = 96
    RANGE_IMAGE_LOCAL_SET = 97
    GEO_REGISTRATION_LOCAL_SET = 98
    COMPOSITE_IMAGING_LOCAL_SET = 99
    SEGMENT_LOCAL_SET = 100
    AMEND_LOCAL_SET = 101
    SDCC_FLP = 102
    DENSITY_ALTITUDE_EXTENDED = 103
    SENSOR_ELLIPSOID_HEIGHT_EXTENDED = 104
