Summary:	The Ogg Vorbis Tools
Summary(es):	Utensilios Ogg Vorbis
Summary(pl):	Narzêdzia do obs³ugi plików w formacie Ogg Vorbis
Summary(pt_BR):	Ferramentas Ogg Vorbis
Name:		vorbis-tools
Version:	1.1.1
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# Source0-md5:	47845fd76f5f2354a3619c4097575487
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-nolibnsl.patch
URL:		http://www.vorbis.com/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	flac-devel
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

%description -l pl
Ogg Vorbis jest otwartym, niezale¿nym oraz wolnym od odp³at i patentów
formatem ogólnego przeznaczenia dla plików d¼wiêkowych wysokiej
jako¶ci. Pakiet zawiera ró¿ne narzêdzia do obs³ugi plików w tym
formacie, np.: kompresor, dekompresor, odtwarzacz, itp.

%description -l pt_BR
Ogg Vorbis e' um formato de áudio aberto de propósito geral,
não-proprietário e isento de patentes e royalties, para áudio e musica
de alta qualidade.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
