# Copyright (C) 2024 Aresys S.r.l.

add_executable(solid_test
    solid_test.cpp)

target_include_directories(solid_test
    PRIVATE
    $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include>)

target_link_libraries(solid_test
    PRIVATE
    solid)

add_test(NAME solid_test
    COMMAND ${TEST_DRIVER_COMMAND}
        "${TEST_DRIVER_COMMAND_OPTION_EXEC}=$<TARGET_FILE:solid_test>"
        "${TEST_DRIVER_COMMAND_OPTION_REFERENCE}=${CMAKE_SOURCE_DIR}/test/refs/solid_test.out"
        "${TEST_DRIVER_COMMAND_OPTION_DIFFERENCE}=${CMAKE_CURRENT_BINARY_DIR}/solid_test.out")
