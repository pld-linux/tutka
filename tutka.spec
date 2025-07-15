Summary:	Tracker style MIDI sequencer
Summary(pl.UTF-8):	Sekwencer MIDI w stylu trackera
Name:		tutka
Version:	0.12.4
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://savannah.nongnu.org/download/tutka/%{name}-%{version}.tar.bz2
# Source0-md5:	025d4ce39e638e7af002cb010d97d98f
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-disable_schemas_install.patch
URL:		http://www.nongnu.org/tutka/
BuildRequires:	alsa-lib-devel >= 0.9
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libglade2-devel >= 2.4.2
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.16
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tutka is a free tracker style MIDI sequencer for GNU/Linux. It is
similar to programs like SoundTracker, ProTracker and FastTracker
except that it does not support samples and is meant for MIDI use
only.

%description -l pl.UTF-8
Tutka jest wolnym sekwencerem MIDI w stylu trackera dla GNU/Linuksa.
Przypomina programy jak SoundTracker, ProTracker i FastTracker z tym
że, przeznaczony jest wyłącznie do prac z MIDI, a nie z próbkami
dźwiękowymi.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install tutka.schemas

%preun
%gconf_schema_uninstall tutka.schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
