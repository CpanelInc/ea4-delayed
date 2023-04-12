#!/bin/bash

source debian/vars.sh

mkdir -p $DEB_INSTALL_ROOT$_sysconfdir/apt/sources.list.d
install -m 644 EA4-delayed-$OBS_REPO.list $DEB_INSTALL_ROOT$_sysconfdir/apt/sources.list.d/
