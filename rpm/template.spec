Name:           ros-jade-sick-tim
Version:        0.0.7
Release:        0%{?dist}
Summary:        ROS sick_tim package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/sick_tim
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-driver-base
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
BuildRequires:  libusbx-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-driver-base
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs

%description
A ROS driver for the SICK TiM series of laser scanners. Currently, the package
supports serveral types of TiM310, TiM551 and TiM571 scanners.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Apr 15 2016 Martin Günther <martin.guenther@dfki.de> - 0.0.7-0
- Autogenerated by Bloom

* Fri Nov 13 2015 Martin Günther <martin.guenther@dfki.de> - 0.0.6-0
- Autogenerated by Bloom

