Summary:	The Ogg Vorbis Tools
Summary(es.UTF-8):	Utensilios Ogg Vorbis
Summary(pl.UTF-8):	Narzędzia do obsługi plików w formacie Ogg Vorbis
Summary(pt_BR.UTF-8):	Ferramentas Ogg Vorbis
Name:		vorbis-tools
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# Source0-md5:	df976d24e51ef3d87cd462edf747bf9a
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-nolibnsl.patch
URL:		http://www.vorbis.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	gettext-devel
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libogg-devel >= 2:1.1
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.1.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	speex-devel
Requires:	libvorbis >= 1:1.1.1
Obsoletes:	vorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for high quality audio. This
package contains various tools for Ogg Vorbis files such as command
line encoder, decoder, player, etc.

%description -l pl.UTF-8
Ogg Vorbis jest otwartym, niezależnym oraz wolnym od odpłat i patentów
formatem ogólnego przeznaczenia dla plików dźwiękowych wysokiej
jakości. Pakiet zawiera różne narzędzia do obsługi plików w tym
formacie, np.: kompresor, dekompresor, odtwarzacz, itp.

%description -l pt_BR.UTF-8
Ogg Vorbis e' um formato de áudio aberto de propósito geral,
não-proprietário e isento de patentes e royalties, para áudio e musica
de alta qualidade.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README
%attr(755,root,root) %{_bindir}/ogg123
%attr(755,root,root) %{_bindir}/oggdec
%attr(755,root,root) %{_bindir}/oggenc
%attr(755,root,root) %{_bindir}/ogginfo
%attr(755,root,root) %{_bindir}/vorbiscomment
%{_mandir}/man1/ogg123.1*
%{_mandir}/man1/oggdec.1*
%{_mandir}/man1/oggenc.1*
%{_mandir}/man1/ogginfo.1*
%{_mandir}/man1/vorbiscomment.1*
