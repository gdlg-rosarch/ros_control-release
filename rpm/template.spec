Name:           ros-indigo-controller-manager-msgs
Version:        0.9.4
Release:        0%{?dist}
Summary:        ROS controller_manager_msgs package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-std-msgs

%description
Messages and services for the controller manager.

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
* Fri Feb 12 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.9.4-0
- Autogenerated by Bloom

* Tue May 05 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.9.3-0
- Autogenerated by Bloom

* Mon May 04 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.9.2-0
- Autogenerated by Bloom

* Mon Nov 03 2014 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.9.1-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Wim Meeussen <wim@hidof.com> - 0.9.0-0
- Autogenerated by Bloom

