%define name glpi-plugin-fusioninventory
%define version 2.4.0
%define release %mkrel 1

%define _requires_exceptions pear(.*)

Name:    %{name}
Version: %{version}
Release: %{release}
Summary: fusioninventory communication server
License: GPL
Group:   Monitoring
Url:     http://fusioninventory.org/wordpress/
Source0: http://forge.fusioninventory.org/attachments/download/515/fusioninventory-for-glpi-metapackage_0.80_1.1.tar.gz
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

%package deploy
Summary:        Deploy extension for fusioninventory
Group:          Monitoring
License:        GPL
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description deploy
This plugin allow to deploy with fusioninventory agents.

%prep
%setup -q -c

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins
cp -rp fusinvdeploy %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusinvinventory %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusinvsnmp %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusioninventory %{buildroot}%{_datadir}/glpi/plugins/

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

%files deploy
%defattr(-,root,root)
%{_datadir}/glpi/plugins/fusinvdeploy
