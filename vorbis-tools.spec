Summary:	The OGG Vorbis lossy audio compression codec
Summary(es):	Utensilios Ogg Vorbis
Summary(pl):	Codec do stratnej kompresji dºwiÍku Vorbis OGG
Summary(pt_BR):	Ferramentas Ogg Vorbis
Name:		vorbis-tools
Version:	1.0rc3
Release:	3
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
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	libao-devel
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel = %{version}
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

%description -l pt_BR
Ogg Vorbis e' um formato de ·udio aberto de propÛsito geral,
n„o-propriet·rio e isento de patentes e royalties, para ·udio e musica
de alta qualidade.

Este pacote contem as seguintes ferramentas Vorbis: oggenc, o encoder
Ogg Vorbis; ogg123, reprodutor de ·udio de linha de comando;
vorbiscomment, um editor de coment·rios para arquivos Ogg Vorbis;
ogginfo, mostra as informaÁıes de arquivos Ogg Vorbis; e vcut, que
permite dividir arquivos Ogg Vorbis.

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
