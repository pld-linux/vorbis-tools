Summary:	The Ogg Vorbis Tools
Summary(es):	Utensilios Ogg Vorbis
Summary(pl):	Narzêdzia do obs³ugi plików w formacie Ogg Vorbis
Summary(pt_BR):	Ferramentas Ogg Vorbis
Name:		vorbis-tools
Version:	1.0
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	http://www.vorbis.com/files/%{version}/unix/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-amfix.patch
URL:		http://www.vorbis.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libao-devel >= 0.8.3
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:%{version}
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	vorbis

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
rm -f missing
%{__libtoolize}
aclocal
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
