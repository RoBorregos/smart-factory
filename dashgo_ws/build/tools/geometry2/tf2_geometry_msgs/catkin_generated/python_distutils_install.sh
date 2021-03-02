#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/geometry2/tf2_geometry_msgs"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/install/lib/python2.7/dist-packages:/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build" \
    "/usr/bin/python2" \
    "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/src/tools/geometry2/tf2_geometry_msgs/setup.py" \
     \
    build --build-base "/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/build/tools/geometry2/tf2_geometry_msgs" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/install" --install-scripts="/home/aurotb/Desktop/EAIBotSmartFactory/dashgo_ws/install/bin"
