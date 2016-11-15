%{!?upstream_version: %global upstream_version %{commit}}
%global commit c1f1d1e22d75215fc28e3f463af4b8fd72bde781
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git

%define upstream_name puppetlabs-inifile

Name:           puppet-inifile
Version:        1.6.0
Release:        2%{?alphatag}%{?dist}
Summary:        Resource types for managing settings in INI files
License:        Apache-2.0

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 1.6.0-2.c1f1d1egit
- Newton update 1.6.0 (c1f1d1e22d75215fc28e3f463af4b8fd72bde781)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> 1.6.0-1
- Update to 1.6.0


