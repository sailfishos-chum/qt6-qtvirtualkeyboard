
%global  qt_version 6.7.2

Summary: Qt6 - VirtualKeyboard component
Name:    qt6-qtvirtualkeyboard
Version: 6.7.2
Release: 0%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
Source0: %{name}-%{version}.tar.bz2


## upstreamable patches

BuildRequires: cmake
BuildRequires: clang
BuildRequires: ninja
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{qt_version}
BuildRequires: qt6-qtsvg-devel >= %{qt_version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel
BuildRequires: hunspell-devel

# version unknown
Provides: bundled(libpinyin)

%description
The Qt Virtual Keyboard project provides an input framework and reference keyboard frontend
for Qt 6.  Key features include:
* Customizable keyboard layouts and styles with dynamic switching.
* Predictive text input with word selection.
* Character preview and alternative character view.
* Automatic capitalization and space insertion.
* Scalability to different resolutions.
* Support for different character sets (Latin, Simplified/Traditional Chinese, Hindi, Japanese, Arabic, Korean, and others).
* Support for most common input languages, with possibility to easily extend the language support.
* Left-to-right and right-to-left input.
* Hardware key support for 2-way and 5-way navigation.
* Handwriting support, with gestures for fullscreen input.
* Audio feedback.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=OFF \
  -DQT_INSTALL_EXAMPLES_SOURCES=OFF

%cmake_build


%install
%cmake_install

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6HunspellInputMethod.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboard.so.6*
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so.6*
%{_qt6_plugindir}/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_qt6_qmldir}/QtQuick/VirtualKeyboard/

%files devel
%{_qt6_headerdir}/QtHunspellInputMethod/
%{_qt6_headerdir}/QtVirtualKeyboard/
%{_qt6_headerdir}/QtVirtualKeyboardSettings/
%{_qt6_libdir}/libQt6HunspellInputMethod.prl
%{_qt6_libdir}/libQt6HunspellInputMethod.so
%{_qt6_libdir}/libQt6VirtualKeyboard.prl
%{_qt6_libdir}/libQt6VirtualKeyboard.so
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.prl
%{_qt6_libdir}/libQt6VirtualKeyboardSettings.so
%{_qt6_libdir}/cmake/Qt6/
%{_qt6_libdir}/cmake/Qt6HunspellInputMethod/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboard/
%{_qt6_libdir}/cmake/Qt6VirtualKeyboardSettings/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtVirtualKeyboardTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6BundledOpenwnn/Qt6BundledOpenwnnDependencies.cmake
%{_qt6_libdir}/cmake/Qt6BundledPinyin/Qt6BundledPinyinDependencies.cmake
%{_qt6_libdir}/cmake/Qt6BundledTcime/Qt6BundledTcimeDependencies.cmake
%{_qt6_libdir}/cmake/Qt6Gui/Qt6QVirtualKeyboardPlugin*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_virtualkeyboard*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/*.pc
