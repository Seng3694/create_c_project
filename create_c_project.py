import os
import sys
import argparse

#template string for the CMakeLists.txt file required for the exeutable project
cmake_executable_root_file = """cmake_minimum_required(VERSION <CMAKE_VERSION>)

project(<PROJECT_NAME> C)

set(HEADER_FILES
)

set(SOURCE_FILES
    src/main.c
)

include_directories(include)
add_executable(${PROJECT_NAME} ${HEADER_FILES} ${SOURCE_FILES})

"""

#template string for the root CMakeLists.txt file required for the library project
cmake_library_root_file = """cmake_minimum_required(VERSION <CMAKE_VERSION>)

project(<PROJECT_NAME>)

add_subdirectory(<PROJECT_NAME>)
add_subdirectory(test)

"""

#template string for the CMakeLists.txt file required for building the library project
cmake_library_project_file = """set(HEADER_FILES
    include/<PROJECT_NAME>/<PROJECT_NAME>.h
)

set(SOURCE_FILES
    src/<PROJECT_NAME>.c
)

set(INLINE_FILES
)

add_library(${PROJECT_NAME} ${HEADER_FILES} ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME} PUBLIC include)
target_include_directories(${PROJECT_NAME} PRIVATE inline)

"""

#template string for the CMakeLists.txt file required for building the library test executable
cmake_library_test_file = """set(HEADER_FILES
)

set(SOURCE_FILES
    src/main.c
)

include_directories(include)
add_executable(${PROJECT_NAME}_tests ${HEADER_FILES} ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME}_tests ${PROJECT_NAME})

"""

#template string for the empty header file of the library project
library_header_file = """#ifndef <PROJECT_NAME>_H
#define <PROJECT_NAME>_H

#endif

"""

#template string for the empty source file of the library project
library_source_file = """#include "<PROJECT_NAME>/<PROJECT_NAME>.h"

"""

#template string for the source file of the library test executable
library_test_source_file = """#include <<PROJECT_NAME>/<PROJECT_NAME>.h>

int main(void) 
{
    return 0;
}

"""

#template string for the source file of the executable project
executable_source_file = """int main(void)
{
    return 0;
}

"""

def main():
    defaultProjectName = "c_project"
    defaultCMakeVersion = "2.6"

    parser = argparse.ArgumentParser(
        description="Creates a C and CMake project"
    )

    parser.add_argument(
        "-n", 
        "--name",
        type=str,
        help="The project name"
    )

    parser.add_argument(
        "-c",
        "--cmake",
        type=str,
        help="The CMake version"
    )

    parser.add_argument(
        "--lib",
        help="Will create a library project instead of an executable",
        action="store_true"
    )

    args = parser.parse_args()
    
    projectName = args.name
    if projectName is None:
        projectName = defaultProjectName
    projectName = adjust_project_name(projectName)

    cmakeVersion = args.cmake
    if cmakeVersion is None:
        cmakeVersion = defaultCMakeVersion

    if args.lib:
        create_lib_project(projectName, cmakeVersion)
    else:
        create_executable_project(projectName, cmakeVersion)

#checks if the given projectname is already in use and appends a number until the name is unique
#e.g.: "projectname" (already in use) => "projectname_1" (already in use) => "projectname_2"
def adjust_project_name(name):
    if os.path.exists(name):
        number = 1

        while os.path.exists(name + "_" + str(number)):
            number = number + 1

        name = name + "_" + str(number)
    
    return name

#creates the library project file tree structure and files
def create_lib_project(name, cmake):
    #  name
    #  |-name
    #  | |-include
    #  | | |-name
    #  | |   |-name.h
    #  | | 
    #  | |-src
    #  | | |-name.c
    #  | | 
    #  | |-CMakeLists.txt
    #  | 
    #  |-test
    #  | |-include
    #  | |-src
    #  | | |-main.c
    #  | | 
    #  | |-CMakeLists.txt
    #  |
    #  |-CMakeLists.txt
    #

    os.makedirs(name)
    os.chdir(name)
    os.makedirs(name)
    os.makedirs("test")
    content = cmake_library_root_file.replace("<PROJECT_NAME>", name).replace("<CMAKE_VERSION>", cmake)
    f = open("CMakeLists.txt", "w")
    f.write(content)
    f.close()

    os.chdir(name)
    os.makedirs("include")
    os.makedirs("src")
    content = cmake_library_project_file.replace("<PROJECT_NAME>", name)
    f = open("CMakeLists.txt", "w")
    f.write(content)
    f.close()

    os.chdir("include")
    os.makedirs(name)
    os.chdir(name)

    upperCaseName = name.upper().replace(" ", "_")
    content = library_header_file.replace("<PROJECT_NAME>", upperCaseName)
    f = open(name + ".h", "w")
    f.write(content)
    f.close()

    os.chdir("../../src")
    content = library_source_file.replace("<PROJECT_NAME>", name)
    f = open(name + ".c", "w")
    f.write(content)
    f.close()

    os.chdir("../../test")
    os.makedirs("include")
    os.makedirs("src")
    content = cmake_library_test_file.replace("<PROJECT_NAME>", name)
    f = open("CMakeLists.txt", "w")
    f.write(content)
    f.close()

    os.chdir("src")
    content = library_test_source_file.replace("<PROJECT_NAME>", name)
    f = open("main.c", "w")
    f.write(content)
    f.close()

    os.chdir("../..")

#creates the executable project file tree structure and files
def create_executable_project(name, cmake):
    #  name
    #  |-include
    #  |-src
    #  | |-main.c
    #  | 
    #  |-CMakeLists.txt

    os.makedirs(name)
    os.chdir(name)
    os.makedirs("include")
    os.makedirs("src")

    content = cmake_executable_root_file.replace("<PROJECT_NAME>", name).replace("<CMAKE_VERSION>", cmake)
    f = open("CMakeLists.txt", "w")
    f.write(content)
    f.close()

    os.chdir("src")
    content = executable_source_file.replace("<PROJECT_NAME>", name)
    f = open("main.c", "w")
    f.write(content)
    f.close()
    os.chdir("../..")

if __name__ == "__main__":
    main()
