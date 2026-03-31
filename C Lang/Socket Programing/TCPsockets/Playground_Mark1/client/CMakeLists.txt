cmake_minimum_required(VERSION 3.10) # More compatible version
project(client C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON) # Ensures the compiler MUST support C11

# Only list main.c once
add_executable(client main.c)
