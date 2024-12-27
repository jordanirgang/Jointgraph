cmake_minimum_required(VERSION 3.0)
project(JOINTGRAPHLIB)
add_library(JOINTGRAPHJOINTS jointGraph.cpp jointGraph.h)
add_executable(TESTGRAPH test.cpp)
target_link_libraries(TESTGRAPH PUBLIC JOINTGRAPHLIB)


