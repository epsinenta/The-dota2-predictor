# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\qt_dota_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\qt_dota_autogen.dir\\ParseCache.txt"
  "qt_dota_autogen"
  )
endif()
