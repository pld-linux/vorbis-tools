Summary: 	The OGG Vorbis lossy audio compression codec.
Name:  		vorbis-tools
Version: 	1.0.0_cvs2000.10.29
Release: 	1
Copyright: 	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
URL: 		http://www.xiph.org/vorbis/index.html
Source:		ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
BuildRequires:  libvorbis-devel
BuildRequires:  libao-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality (44.1-48.0kHz,
16+ bit, polyphonic) audio and music at fixed and variable bitrates
from 16 to 128 kbps/channel. This places Vorbis in the same class as
audio representations including MPEG-1 audio layer 3, MPEG-4
audio (AAC and TwinVQ), and PAC.

%prep
%setup -q -n vorbis-tools
%patch0 -p1

%build
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh --prefix=%{_prefix}
else
  CFLAGS="$RPM_OPT_FLAGS" %configure --prefix=%{_prefix}
fi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
