
set(TARGET_NAME data-structures)
set(SRC_FILES main.cpp)
add_executable(${TARGET_NAME} ${SRC_FILES})
#target_include_directories(${DS} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory(test)