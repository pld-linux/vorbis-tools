Summary:	The OGG Vorbis lossy audio compression codec
Summary(pl):	Codec do stratnej kompresji dºwiÍku Vorbis OGG
Name:		vorbis-tools
Version:	1.0rc3
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Source0:	http://www.vorbis.com/files/rc2/unix/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xiph.org/vorbis/index.html
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libao-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	curl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	vorbis

%description 
Ogg Vorbis is a fully Open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality
(44.1-48.0kHz, 16+ bit, polyphonic) audio and music at fixed and
variable bitrates from 16 to 128 kbps/channel. This places Vorbis in
the same class as audio representations including MPEG-1 audio layer
3, MPEG-4 audio (AAC and TwinVQ), and PAC.

%description -l pl
Ogg Vorbis to wysokiej jako∂ci (44.1-48.0kHz, 16+ bit, polifonia),
kompresowalny format audio przy sta≥ej i zmiennej bitrate od 16 do 128
kbps/kana≥. To umieszcza Vorbisa w tej samej klasie co MPEG-1 audio
layer 3, MPEG-4 audio (AAC i TwinVQ) oraz PAC.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
