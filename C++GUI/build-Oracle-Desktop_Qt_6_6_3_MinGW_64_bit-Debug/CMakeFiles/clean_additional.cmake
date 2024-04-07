# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\Oracle_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\Oracle_autogen.dir\\ParseCache.txt"
  "Oracle_autogen"
  )
endif()
