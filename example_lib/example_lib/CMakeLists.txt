set(HEADER_FILES
    include/example_lib/example_lib.h
)

set(SOURCE_FILES
    src/example_lib.c
)

set(INLINE_FILES
)

add_library(${PROJECT_NAME} ${HEADER_FILES} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC include)
target_include_directories(${PROJECT_NAME} PRIVATE inline)

