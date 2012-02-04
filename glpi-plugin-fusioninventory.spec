%if %mandriva_branch == Cooker
%define release %mkrel 2
%else
%define subrel 1
%define release %mkrel 0
%endif

%define _requires_exceptions pear(.*)

Summary: fusioninventory communication server
Name: glpi-plugin-fusioninventory
Version: 2.4.0
Release: %{release}
License: GPL
Group: Monitoring
URL: http://fusioninventory.org/wordpress/
Source0: http://forge.fusioninventory.org/attachments/download/515/fusioninventory-for-glpi-metapackage_0.80_1.1.tar.gz
BuildArch: noarch

%description
This plugin enables you to manage fusioninventory agents from GLPI.

%package snmp
Summary: SNMP extension for fusioninventory
Group: Monitoring
Requires: %{name} = %{version}-%{release}

%description snmp
This plugin allow to perform remote inventory with fusioninventory agents.

%package inventory
Summary: Inventory extension for fusioninventory
Group: Monitoring
Requires: %{name} = %{version}-%{release}

%description inventory
This plugin allow to perform local inventory with fusioninventory agents.

%package deploy
Summary: Deploy extension for fusioninventory
Group: Monitoring
Requires: %{name} = %{version}-%{release}

%description deploy
This plugin allow to deploy with fusioninventory agents.

%prep

%setup -q -c

find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%install

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins
cp -rp fusinvdeploy %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusinvinventory %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusinvsnmp %{buildroot}%{_datadir}/glpi/plugins/
cp -rp fusioninventory %{buildroot}%{_datadir}/glpi/plugins/

rm -rf %{buildroot}%{_datadir}/glpi/plugins/fusinvsnmp/docs
rm -rf %{buildroot}%{_datadir}/glpi/plugins/fusioninventory/docs

%files
%doc fusioninventory/docs/*.TXT
%{_datadir}/glpi/plugins/fusioninventory

%files snmp
%doc fusinvsnmp/docs/*.TXT
%{_datadir}/glpi/plugins/fusinvsnmp

%files inventory
%{_datadir}/glpi/plugins/fusinvinventory

%files deploy
%{_datadir}/glpi/plugins/fusinvdeploy
