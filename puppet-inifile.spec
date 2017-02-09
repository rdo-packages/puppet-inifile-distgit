%define upstream_name puppetlabs-inifile
%{!?upstream_version: %global upstream_version %{commit}}
%global commit 936ed07a85460fda127b2a542d3213efd19a8f2a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git

Name:           puppet-inifile
Version:        1.6.0
Release:        3%{?alphatag}%{?dist}
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
* Thu Feb 09 2017 Alfredo Moralejo <amoralej@redhat.com> 1.6.0-3.936ed07git
- Update to 1.6.0 (936ed07a85460fda127b2a542d3213efd19a8f2a)
