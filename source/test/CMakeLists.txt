# Copyright (C) 2024 Aresys S.r.l.

if(WIN32)
    set(TEST_DRIVER_COMMAND "${CMAKE_SOURCE_DIR}/test/tools/test_driver.ps1")
    set(TEST_DRIVER_COMMAND_OPTION_EXEC "-Exec")
    set(TEST_DRIVER_COMMAND_OPTION_REFERENCE "-Reference")
    set(TEST_DRIVER_COMMAND_OPTION_DIFFERENCE "-Difference")
else()
    set(TEST_DRIVER_COMMAND "${CMAKE_SOURCE_DIR}/test/tools/test_driver.sh")
    set(TEST_DRIVER_COMMAND_OPTION_EXEC "--exec")
    set(TEST_DRIVER_COMMAND_OPTION_REFERENCE "--reference")
    set(TEST_DRIVER_COMMAND_OPTION_DIFFERENCE "--difference")
endif()

add_subdirectory(core)
