Name: ea4-delayed
Version: 0.1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4600 for more details
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
Summary: Get EA4 production packages a few days after they go to production

Group: Development/Tools
License: BSD 2-Clause
Vendor: cPanel, Inc.

Source1: EA4-delayed.repo

%description
This package changes the server from EA4-production to EA4-delayed.
EA4-delayed containes packages from EA4-production but it is a few
days behind. This gives extra-cautious admins a buffer to see how
production shakes out.

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/EA4-delayed.repo

%clean
rm -rf %{buildroot}

# TODO: need to disable EA4 on install, enable EA4 on uninstall

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/EA4-delayed.repo

%changelog
* Wed Mar 23 2022 Dan Muey <dan@cpanel.net> - 0.1-1
- Initial version
