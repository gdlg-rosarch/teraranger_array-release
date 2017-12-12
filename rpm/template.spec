Name:           ros-kinetic-teraranger-array
Version:        1.2.3
Release:        0%{?dist}
Summary:        ROS teraranger_array package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/teraranger_array
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-serial
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-serial
BuildRequires:  ros-kinetic-std-msgs

%description
The teraranger_array package for TeraRanger Array Products (Multiflex, One)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Dec 12 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.2.3-0
- Autogenerated by Bloom

* Thu Dec 07 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.2.2-0
- Autogenerated by Bloom

* Wed Dec 06 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.2.1-0
- Autogenerated by Bloom

* Fri Nov 17 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.1.0-0
- Autogenerated by Bloom

* Wed Sep 20 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.0.1-0
- Autogenerated by Bloom

* Mon Sep 18 2017 Pierre-Louis Kabaradjian <pierre-louis.kabaradjian@terabee.com> - 1.0.0-0
- Autogenerated by Bloom

