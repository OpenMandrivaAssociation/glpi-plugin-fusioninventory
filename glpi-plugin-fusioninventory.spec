%define name glpi-plugin-fusioninventory
%define version 2.3.0
%define pre RC1
%define release %mkrel 0.%{pre}.1

Summary: SNMP agent plugin
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Monitoring
Url: http://fusioninventory.org/wordpress/
Source0: http://forge.fusioninventory.org/attachments/download/19/fusioninventory_%{version}-%{pre}.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
This plugin enables you get informations for networking devices by SNMP.

%prep
%setup -q -n fusioninventory

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/glpi/plugins/fusioninventory
cp -ap * %{buildroot}%{_datadir}/glpi/plugins/fusioninventory
rm -rf %{buildroot}%{_datadir}/glpi/plugins/fusioninventory/docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*.TXT
%{_datadir}/glpi/plugins/fusioninventory
