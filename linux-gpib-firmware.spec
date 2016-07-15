Summary:	Firmware for GPIB devices using Linux-GPIB drivers
Summary(pl.UTF-8):	Firmware dla urządzeń GPIB wykorzystujących sterowniki Linux-GPIB
Name:		linux-gpib-firmware
Version:	2008.08.10
%define	fver	%(echo %{version} | tr . -)
Release:	1
License:	unknown
Group:		Applications/System
Source0:	http://linux-gpib.sourceforge.net/firmware/gpib_firmware-%{fver}.tar.gz
# Source0-md5:	68cce91f2169fa94022dfcaac1651b6a
URL:		http://linux-gpib.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware for GPIB devices using Linux-GPIB drivers:
- NI GPIB-USB-B
- Agilent 82357A and 82357B
- Agilent (HP) 82341C and 82341D
- Agilent (HP) 82350A

%description -l pl.UTF-8
Firmware dla urządzeń GPIB wykorzystujących sterowniki Linux-GPIB:
- NI GPIB-USB-B
- Agilent 82357A oraz 82357B
- Agilent (HP) 82341C oraz 82341D
- Agilent (HP) 82350A

%prep
%setup -q -n gpib_firmware-%{fver}

for d in agilent_82357a hp_82341 ni_gpib_usb_b ; do
	cp -l ${d}/README README.${d}
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/{agilent_82357a,hp_82341,hp_82350a,ni_usb_gpib}

cp -p agilent_82357a/*.hex $RPM_BUILD_ROOT/lib/firmware/agilent_82357a
cp -p hp_82341/*.bin $RPM_BUILD_ROOT/lib/firmware/hp_82341
cp -p hp_82350a/*.bin $RPM_BUILD_ROOT/lib/firmware/hp_82350a
cp -p ni_gpib_usb_b/*.hex $RPM_BUILD_ROOT/lib/firmware/ni_usb_gpib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.*
/lib/firmware/agilent_82357a
/lib/firmware/hp_82341
/lib/firmware/hp_82350a
/lib/firmware/ni_usb_gpib
