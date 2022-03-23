set(TARGET_NAME linked-list-test)

add_executable(${TARGET_NAME} linked_list_test.cpp)
target_link_libraries(${TARGET_NAME} gtest_main)