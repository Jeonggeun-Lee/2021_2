# Install script for directory: /home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/dron/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bebop_msgs/msg" TYPE FILE FILES
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3AccessoryStateConnectedAccessories.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3AntiflickeringStateelectricFrequencyChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3AntiflickeringStatemodeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3CameraStateOrientation.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3CameraStateOrientationV2.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3CameraStateVelocityRange.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3CameraStatedefaultCameraOrientation.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3CameraStatedefaultCameraOrientationV2.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3GPSStateHomeTypeAvailabilityChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3GPSStateHomeTypeChosenChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3GPSStateNumberOfSatelliteChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaRecordStatePictureStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaRecordStatePictureStateChangedV2.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaRecordStateVideoResolutionState.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaRecordStateVideoStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaRecordStateVideoStateChangedV2.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaStreamingStateVideoEnableChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3MediaStreamingStateVideoStreamModeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3NetworkStateAllWifiAuthChannelChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3NetworkStateAllWifiScanChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3NetworkStateWifiAuthChannelListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3NetworkStateWifiScanListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PROStateFeatures.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateAirSpeedChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateAlertStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateAltitudeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateAttitudeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateAutoTakeOffModeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateFlatTrimChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateFlyingStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateGpsLocationChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateLandingStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateNavigateHomeStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStatePositionChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStateSpeedChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/Ardrone3PilotingStatemoveToChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonARLibsVersionsStateControllerLibARCommandsVersion.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonARLibsVersionsStateDeviceLibARCommandsVersion.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonARLibsVersionsStateSkyControllerLibARCommandsVersion.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonAccessoryStateAccessoryConfigChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonAccessoryStateAccessoryConfigModificationEnabled.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonAccessoryStateSupportedAccessoriesListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonAnimationsStateList.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonAudioStateAudioStreamingRunning.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCalibrationStateMagnetoCalibrationAxisToCalibrateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCalibrationStateMagnetoCalibrationRequiredState.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCalibrationStateMagnetoCalibrationStartedChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCalibrationStateMagnetoCalibrationStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCalibrationStatePitotCalibrationStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonChargerStateChargingInfo.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonChargerStateCurrentChargeStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonChargerStateLastChargeRateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonChargerStateMaxChargeRateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateAllStatesChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateBatteryStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateCountryListKnown.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateCurrentDateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateCurrentTimeChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateDeprecatedMassStorageContentChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateMassStorageContent.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateMassStorageContentForCurrentRun.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateMassStorageInfoRemainingListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateMassStorageInfoStateListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateMassStorageStateListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateProductModel.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateSensorsStatesListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateVideoRecordingTimestamp.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonCommonStateWifiSignalChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonFlightPlanStateAvailabilityStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonFlightPlanStateComponentStateListChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonFlightPlanStateLockStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonHeadlightsStateintensityChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonMavlinkStateMavlinkFilePlayingStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonMavlinkStateMavlinkPlayErrorStateChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonMavlinkStateMissionItemExecuted.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonOverHeatStateOverHeatChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonOverHeatStateOverHeatRegulationChanged.msg"
    "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/msg/autogenerated/CommonRunStateRunIdChanged.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bebop_msgs/cmake" TYPE FILE FILES "/home/dron/catkin_ws/build/bebop_autonomy/bebop_msgs/catkin_generated/installspace/bebop_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/dron/catkin_ws/devel/include/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/dron/catkin_ws/devel/share/roseus/ros/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/dron/catkin_ws/devel/share/common-lisp/ros/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/dron/catkin_ws/devel/share/gennodejs/ros/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/dron/catkin_ws/devel/lib/python2.7/dist-packages/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/dron/catkin_ws/devel/lib/python2.7/dist-packages/bebop_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/dron/catkin_ws/build/bebop_autonomy/bebop_msgs/catkin_generated/installspace/bebop_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bebop_msgs/cmake" TYPE FILE FILES "/home/dron/catkin_ws/build/bebop_autonomy/bebop_msgs/catkin_generated/installspace/bebop_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bebop_msgs/cmake" TYPE FILE FILES
    "/home/dron/catkin_ws/build/bebop_autonomy/bebop_msgs/catkin_generated/installspace/bebop_msgsConfig.cmake"
    "/home/dron/catkin_ws/build/bebop_autonomy/bebop_msgs/catkin_generated/installspace/bebop_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/bebop_msgs" TYPE FILE FILES "/home/dron/catkin_ws/src/bebop_autonomy/bebop_msgs/package.xml")
endif()

