%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name puppetlabs-inifile

Name:           puppet-inifile
Version:        3.1.0
Release:        1%{?alphatag}%{?dist}
Summary:        Resource types for managing settings in INI files
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-inifile

Source0:        https://github.com/puppetlabs/puppetlabs-inifile/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Resource types for managing settings in INI files

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/inifile/


%files
%{_datadir}/openstack-puppet/modules/inifile/


%changelog
* Thu Oct 3 2019 RDO <dev@lists.rdoproject.org> 3.1.0-1.91efcedgit
- Update to post 3.1.0 (91efced79bb9011e162eea35e4a0d9ad12e267a1)


