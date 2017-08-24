%define upstream_name puppetlabs-inifile
%{!?upstream_version: %global upstream_version %{commit}}
%global commit 16fd47d7c74e9bf44ec6f6a9197f16e9a3f57092
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git

Name:           puppet-inifile
Version:        2.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Resource types for managing settings in INI files
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-inifile

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Aug 24 2017 Alfredo Moralejo <amoralej@redhat.com> 2.0.0-1.16fd47dgit
- Pike update 2.0.0 (16fd47d7c74e9bf44ec6f6a9197f16e9a3f57092)
