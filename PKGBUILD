# Script generated with Bloom
pkgdesc="ROS - The combined_robot_hw_tests package"
url='https://github.com/ros-controls/ros_control/wiki'

pkgname='ros-melodic-combined-robot-hw-tests'
pkgver='0.14.0_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-melodic-catkin'
'ros-melodic-combined-robot-hw'
'ros-melodic-controller-manager'
'ros-melodic-controller-manager-tests'
'ros-melodic-hardware-interface'
'ros-melodic-roscpp'
'ros-melodic-rostest'
)

depends=('ros-melodic-combined-robot-hw'
'ros-melodic-controller-manager'
'ros-melodic-controller-manager-tests'
'ros-melodic-hardware-interface'
'ros-melodic-roscpp'
)

conflicts=()
replaces=()

_dir=combined_robot_hw_tests
source=()
md5sums=()

prepare() {
    cp -R $startdir/combined_robot_hw_tests $srcdir/combined_robot_hw_tests
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/melodic/setup.bash ] && source /opt/ros/melodic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/melodic \
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

