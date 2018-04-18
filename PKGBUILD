# Script generated with Bloom
pkgdesc="ROS - A set of packages that include controller interfaces, controller managers, transmissions and hardware_interfaces."
url='http://ros.org/wiki/ros_control'

pkgname='ros-lunar-ros-control'
pkgver='0.13.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-lunar-catkin'
)

depends=('ros-lunar-combined-robot-hw'
'ros-lunar-combined-robot-hw-tests'
'ros-lunar-controller-interface'
'ros-lunar-controller-manager'
'ros-lunar-controller-manager-msgs'
'ros-lunar-controller-manager-tests'
'ros-lunar-hardware-interface'
'ros-lunar-joint-limits-interface'
'ros-lunar-realtime-tools'
'ros-lunar-transmission-interface'
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
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
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

