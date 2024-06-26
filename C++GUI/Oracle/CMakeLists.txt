cmake_minimum_required(VERSION 3.5)

project(Oracle VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets)

set(PostgreSQL_INCLUDE_DIR "C:/Program Files/PostgreSQL/16/include")
set(PostgreSQL_LIBRARY_DIR "C:/Program Files/PostgreSQL/16/lib")
set(PostgreSQL_BIN_DIR "C:/Program Files/PostgreSQL/16/bin")

include_directories(${PostgreSQL_INCLUDE_DIR})
link_directories(${PostgreSQL_LIBRARY_DIR})

set(PROJECT_SOURCES
        main.cpp
        mainwindow.cpp
        mainwindow.h
        mainwindow.ui
)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(Oracle
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}


        hero.h hero.cpp hero.ui
        predict_user.h predict_user.cpp predict_user.ui
        predict_pro.h predict_pro.cpp predict_pro.ui
        oracle.qrc

        database_manager.h database_manager.cpp

        widget_initializer.h widget_initializer.cpp
        row.txt
        config.txt
        predictmanager.h predictmanager.cpp
        text_file_manager.h text_file_manager.cpp

    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET Oracle APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(Oracle SHARED
            ${PROJECT_SOURCES}
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(Oracle
            ${PROJECT_SOURCES}
        )
    endif()
endif()

target_link_libraries(Oracle PRIVATE Qt${QT_VERSION_MAJOR}::Widgets ${PQ_LIB} "${PQXX_LIBRARIES}")

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
if(${QT_VERSION} VERSION_LESS 6.1.0)
  set(BUNDLE_ID_OPTION MACOSX_BUNDLE_GUI_IDENTIFIER com.example.Oracle)
endif()
set_target_properties(Oracle PROPERTIES
    ${BUNDLE_ID_OPTION}
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

include(GNUInstallDirs)
install(TARGETS Oracle
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(Oracle)
endif()

find_library(PQ_LIB pq PATHS ${PostgreSQL_LIBRARY_DIR} NO_DEFAULT_PATH)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/row.txt
        ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/config.txt
        ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
