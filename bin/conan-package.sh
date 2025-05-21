#!/bin/bash

set -Eeuo pipefail

BUILD_TYPE=${1:-Release}
PACKAGE_NAME="unodb"
PACKAGE_VERSION="0.1.0"

echo "Using build type: $BUILD_TYPE"

conan install . \
  --build=missing \
  -s build_type=$BUILD_TYPE

conan build . \
  -s build_type=$BUILD_TYPE

conan export-pkg . \
  -s build_type=$BUILD_TYPE

echo "Package ${PACKAGE_NAME}/${PACKAGE_VERSION} built and exported successfully."
