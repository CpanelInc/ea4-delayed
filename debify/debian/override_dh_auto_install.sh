#!/bin/bash

source debian/vars.sh

mkdir -p $DEB_INSTALL_ROOT$_sysconfdir/apt/sources.list.d
install -m 644 $SOURCE1 $DEB_INSTALL_ROOT$_sysconfdir/apt/sources.list.d/EA4-delayed.list
