cmake_minimum_required(VERSION 3.10)
project(soc_fgo)

set(CMAKE_CXX_STANDARD 14)

find_package(GTSAM REQUIRED)

add_executable(soc_fgo_current main.cpp)
target_link_libraries(soc_fgo_current gtsam)

add_executable(soc_fgo_linear main_clean.cpp)
target_link_libraries(soc_fgo_linear gtsam)

add_executable(soc_fgo_nonlinear main_nonlinear.cpp)
target_link_libraries(soc_fgo_nonlinear gtsam)
