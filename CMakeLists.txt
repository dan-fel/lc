cmake_minimum_required(VERSION 3.10)


project(lcode)

set(DBUILD_SHARED_LIBS=ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_subdirectory(external/googletest)
add_subdirectory(ds)