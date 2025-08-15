# Set the minimum required version of CMake
cmake_minimum_required(VERSION 3.10)

# Set the project name
project(BlackholeSim)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find the SFML package
# It will find the libraries for system, window, graphics, network, and audio
find_package(SFML 2.5 COMPONENTS graphics window system REQUIRED)

# Create the executable
add_executable(BlackholeSim src/main.cpp src/BlackHole.cpp src/Particle.cpp)

# Link SFML libraries to the executable
target_link_libraries(BlackholeSim sfml-graphics sfml-window sfml-system)
