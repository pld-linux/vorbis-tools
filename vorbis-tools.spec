%define	vrc	rc1
Summary:	The OGG Vorbis lossy audio compression codec
Summary(pl):	Codec do stratnej kompresji d¼wiêku Vorbis OGG
Name:		vorbis-tools
Version:	1.0
Release:	0.%{vrc}
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
URL:		http://www.xiph.org/vorbis/index.html
Source0:	http://www.vorbis.com/files/rc1/unix/%{name}-%{version}%{vrc}.tar.gz
BuildRequires:	libvorbis-devel
BuildRequires:	libogg-devel
BuildRequires:	libao-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality
(44.1-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and
variable bitrates from 16 to 128 kbps/channel. This places Vorbis in
the same class as audio representations including MPEG-1 audio layer
3, MPEG-4 audio (AAC and TwinVQ), and PAC.

%description -l pl
Ogg Vorbis to wysokiej jako¶ci (44.1-48.0kHz, 16+ bit, polifonia),
kompresowalny format audio przy sta³ej i zmiennej bitrate od 16 do 128
kbps/kana³. To umieszcza Vorbisa w tej samej klasie co MPEG-1 audio
layer 3, MPEG-4 audio (AAC i TwinVQ) oraz PAC.

%prep
%setup -q -n %{name}-%{version}%{vrc}

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/man?/*
%attr(755,root,root) %{_bindir}/*
