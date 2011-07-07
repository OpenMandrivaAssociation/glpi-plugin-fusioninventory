%define name glpi-plugin-fusioninventory
%define version 2.3.6
%define release %mkrel 1

%define _requires_exceptions pear(.*)

Name:    %{name}
Version: %{version}
Release: %{release}
Summary: fusioninventory communication server
License: GPL
Group:   Monitoring
Url:     http://fusioninventory.org/wordpress/
Source0: http://forge.fusioninventory.org/attachments/download/19/fusioninventory-for-glpi-metapackage_%{version}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin enables you to manage fusioninventory agents from GLPI.

%package snmp
Summary:        SNMP extension for fusioninventory
Group:          Monitoring
License:        GPL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description snmp
This plugin allow to perform remote inventory with fusioninventory agents.

%package inventory
Summary:        Inventory extension for fusioninventory
Group:          Monitoring
License:        GPL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description inventory
This plugin allow to perform local inventory with fusioninventory agents.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins
cp -pr fusioninventory %{buildroot}%{_datadir}/glpi/plugins
cp -pr fusinvsnmp %{buildroot}%{_datadir}/glpi/plugins
cp -pr fusinvinventory %{buildroot}%{_datadir}/glpi/plugins

rm -rf %{buildroot}%{_datadir}/glpi/plugins/fusinvsnmp/docs
rm -rf %{buildroot}%{_datadir}/glpi/plugins/fusioninventory/docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc fusioninventory/docs/*.TXT
%{_datadir}/glpi/plugins/fusioninventory

%files snmp
%defattr(-,root,root)
%doc fusinvsnmp/docs/*.TXT
%{_datadir}/glpi/plugins/fusinvsnmp

%files inventory
%defattr(-,root,root)
%{_datadir}/glpi/plugins/fusinvinventory
