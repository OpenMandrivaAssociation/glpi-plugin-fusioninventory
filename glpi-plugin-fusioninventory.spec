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


%changelog
* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-2mdv2012.0
+ Revision: 771127
- various fixes

* Sat Feb 04 2012 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-1
+ Revision: 771088
- 2.4.0

* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.6-1
+ Revision: 689109
- new version

* Sun Jun 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.5-1
+ Revision: 687293
- new version

* Fri May 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.4-2
+ Revision: 680302
- fix automatic dependencies

* Thu May 26 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.4-1
+ Revision: 679178
- new version

* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.2-1
+ Revision: 666419
- new version

* Sun May 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.1-1
+ Revision: 661415
- new version

* Thu Mar 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.0-0.RC1.1
+ Revision: 649402
- new version

* Tue Aug 24 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-1mdv2011.0
+ Revision: 572709
- 2.2.2 final

* Wed Aug 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.2-0.RC1.1mdv2011.0
+ Revision: 571244
- new version

* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.0-0.beta4.1mdv2010.1
+ Revision: 541805
- import glpi-plugin-fusioninventory


