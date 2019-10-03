# Create a CMake C Project #
Creates a CMake project structure for a C project. A script i've been using for some projects of mine.

## Command Line Interface ##

| Argument | Short | Explanation                                                                |
|----------|-------|----------------------------------------------------------------------------|
| --name   | -n    | The name of the project. (e.g.: "my_project")                              |
| --cmake  | -c    | The CMake version to use. (e.g.: "2.8")                                    |
| --lib    |       | Optional argument for building a library project instead of an exectuable. |
| --help   | -h    | Prints help text.                                                          |

## Example for a libary project ##

```bash
>py create_c_project.py --name"name" --cmake"3.2" --lib
```

This creates a the following structure where `name` is the project name:

```
name
 +--name
 |  +--include
 |  |  +--name
 |  |     +--name.h
 |  | 
 |  +--src
 |  |  +--name.c
 |  | 
 |  +--CMakeLists.txt
 | 
 +--test
 |  +--include
 |  +--src
 |  |  +--main.c
 |  | 
 |  +--CMakeLists.txt
 |
 +--CMakeLists.txt
```

## Example for a executable project ##

```bash
>py create_c_project.py --name"name" --cmake"3.2"
```

This creates a the following structure where `name` is the project name:

```
name
 +--include
 +--src
 |  +--main.c
 | 
 +--CMakeLists.txt
```

## License ##

MIT License: see [License][1] for more information.

[1]:LICENSE
