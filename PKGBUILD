# Script generated with Bloom
pkgdesc="ROS - The controller manager."
url='https://github.com/ros-controls/ros_control/wiki'

pkgname='ros-kinetic-controller-manager'
pkgver='0.13.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-controller-interface'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-hardware-interface'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-controller-interface'
'ros-kinetic-controller-manager-msgs'
'ros-kinetic-hardware-interface'
'ros-kinetic-pluginlib'
'ros-kinetic-realtime-tools'
)

conflicts=()
replaces=()

_dir=controller_manager
source=()
md5sums=()

prepare() {
    cp -R $startdir/controller_manager $srcdir/controller_manager
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

