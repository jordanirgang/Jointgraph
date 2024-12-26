cmake_minimum_required(VERSION 3.0)
project(JOINTGRAPH)

add_executable(TESTGRAPH test.cpp jointGraph.cpp )
target_link_libraries(TESTGRAPH jointGraph.h)


