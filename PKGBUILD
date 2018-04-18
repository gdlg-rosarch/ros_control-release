# Script generated with Bloom
pkgdesc="ROS - controller_manager_tests"
url='http://ros.org/wiki/controller_manager_tests'

pkgname='ros-kinetic-controller-manager-tests'
pkgver='0.13.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-controller-manager'
'ros-kinetic-rosbash'
'ros-kinetic-rosnode'
'ros-kinetic-rosservice'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-controller-interface'
'ros-kinetic-controller-manager'
'ros-kinetic-rostest'
)

conflicts=()
replaces=()

_dir=controller_manager_tests
source=()
md5sums=()

prepare() {
    cp -R $startdir/controller_manager_tests $srcdir/controller_manager_tests
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

