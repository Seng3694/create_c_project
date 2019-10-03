set(HEADER_FILES
)

set(SOURCE_FILES
    src/Main.c
)

include_directories(include)
add_executable(${PROJECT_NAME}_tests ${HEADER_FILES} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME}_tests ${PROJECT_NAME})

