cmake_minimum_required(VERSION 3.16)
project(soc_fgo_paper2 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(GTSAM REQUIRED)

add_executable(soc_fgo_nonlinear src/main_nonlinear.cpp)
target_include_directories(soc_fgo_nonlinear PRIVATE include)
target_link_libraries(soc_fgo_nonlinear PRIVATE gtsam)

