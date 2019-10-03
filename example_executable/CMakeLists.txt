cmake_minimum_required(VERSION 2.8)

project(example_executable C)

set(HEADER_FILES
)

set(SOURCE_FILES
    src/main.c
)

include_directories(include)
add_executable(${PROJECT_NAME} ${HEADER_FILES} ${SOURCE_FILES})

