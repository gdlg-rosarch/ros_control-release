Name:           ros-hydro-rqt-controller-manager
Version:        0.7.3
Release:        0%{?dist}
Summary:        ROS rqt_controller_manager package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_controller_manager
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-controller-manager
Requires:       ros-hydro-rqt-gui
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-controller-manager
BuildRequires:  ros-hydro-rqt-gui

%description
The rqt_controller_manager package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Oct 28 2014 Kelsey Hawkins <kphawkins@gatech.edu> - 0.7.3-0
- Autogenerated by Bloom

