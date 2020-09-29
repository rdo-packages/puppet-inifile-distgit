%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-inifile
%global commit df46d2a0293687a157c70dab128bb5f2a53ef837
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           puppet-inifile
Version:        4.2.0
Release:        1%{?alphatag}%{?dist}
Summary:        Resource types for managing settings in INI files
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppetlabs-inifile

Source0:        https://github.com/puppetlabs/puppetlabs-inifile/archive/%{upstream_version}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 4.2.0-1.df46d2agit
- Update to post 4.2.0 (df46d2a0293687a157c70dab128bb5f2a53ef837)


