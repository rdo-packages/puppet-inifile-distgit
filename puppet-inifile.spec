%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%global upstream_name puppetlabs-inifile
%global commit 687ecf34b35e3739a4c932cf8a78353ebe75d2b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-inifile
Version:        5.3.0
Release:        2.1%{?milestone}%{?alphatag}%{?dist}
Summary:        Resource types for managing settings in INI files
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-inifile

Source0:        https://github.com/puppetlabs/puppetlabs-inifile/archive/v%{version}.tar.gz

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
* Tue Oct 25 2022 Joel Capitao <jcapitao@redhat.com> 5.3.0-2.1.0rc0.687ecf3git
- Set the right commit

* Fri Sep 30 2022 RDO <dev@lists.rdoproject.org> 5.3.0-1.687ecf3git
- Update to post 5.3.0 (687ecf34b35e3739a4c932cf8a78353ebe75d2b9)


