Name:           ros-indigo-sick-tim
Version:        0.0.10
Release:        0%{?dist}
Summary:        ROS sick_tim package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/sick_tim
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  libusbx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
A ROS driver for the SICK TiM series of laser scanners.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Jan 07 2017 Martin Günther <martin.guenther@dfki.de> - 0.0.10-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Martin Günther <martin.guenther@dfki.de> - 0.0.9-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther@dfki.de> - 0.0.8-0
- Autogenerated by Bloom

* Fri Apr 15 2016 Martin Günther <martin.guenther@dfki.de> - 0.0.7-0
- Autogenerated by Bloom

* Fri Nov 13 2015 Martin Günther <martin.guenther@dfki.de> - 0.0.6-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <mguenthe@uos.de> - 0.0.5-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uos.de> - 0.0.4-0
- Autogenerated by Bloom

* Mon Mar 16 2015 Martin Günther <mguenthe@uos.de> - 0.0.3-1
- Autogenerated by Bloom

* Fri Jan 09 2015 Martin Günther <mguenthe@uos.de> - 0.0.3-0
- Autogenerated by Bloom

