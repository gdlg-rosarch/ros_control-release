# Script generated with Bloom
pkgdesc="ROS - A set of packages that include controller interfaces, controller managers, transmissions and hardware_interfaces."
url='http://ros.org/wiki/ros_control'

pkgname='ros-kinetic-ros-control'
pkgver='0.13.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-combined-robot-hw'
'ros-kinetic-combined-robot-hw-tests'
'ros-kinetic-controller-interface'
'ros-kinetic-controller-manager'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-controller-manager-tests'
'ros-kinetic-hardware-interface'
'ros-kinetic-joint-limits-interface'
'ros-kinetic-realtime-tools'
'ros-kinetic-transmission-interface'
)

conflicts=()
replaces=()

_dir=ros_control
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_control $srcdir/ros_control
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

