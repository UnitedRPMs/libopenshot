%global commit0 d3225a80b54289529b6cec3917fde5abd647c6f8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libopenshot
Version:        0.1.8
Release:        4%{?gver}%{?dist}
Summary:        Library for creating and editing videos

License:        LGPLv3+
URL:            http://www.openshot.org/
Source0:	https://github.com/OpenShot/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake swig
BuildRequires:  python3-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:	ImageMagick-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libopenshot-audio-devel >= 0.1.4
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  unittest-cpp-devel
BuildRequires:  libXinerama-devel
BuildRequires:	libXcursor-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	libXrandr-devel
BuildRequires:	cppzmq-devel czmq-devel python3-zmq czmq
BuildRequires:  zeromq-devel

%description
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world. For more information
visit <http://www.openshot.org/>.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     python3-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release} 
Requires:	python3-zmq
Group:          Development/Libraries
Obsoletes:      python-%{name} < 0.1.1-2
Provides:       python-%{name}

%description -n python3-%{name}
The python-%{name} package contains python bindings for 
applications that use %{name}.


%prep
%autosetup -n %{name}-%{commit0} 


%build
export CXXFLAGS="%{optflags} -Wl,--as-needed -Wno-error"
%cmake -DMAGICKCORE_HDRI_ENABLE=1 -DMAGICKCORE_QUANTUM_DEPTH=16 .
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files -n python3-libopenshot
%{python3_sitearch}/*


%changelog

* Wed Oct 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.8-4.gitd3225a8  
- Automatic Mass Rebuild

* Thu Sep 28 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.8-3.gitd3225a8
- Updated to current commit 

* Fri Sep 08 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.8-2.gitdb74076
- Updated to 0.1.8-1

* Tue Jun 06 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.7-2.git078c3f7
- Updated to 0.1.7-2.git078c3f7

* Thu May 25 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.6-2.gitb36d854
- Updated to 0.1.6-2.gitb36d854

* Tue Apr 18 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.4-2.gitddae58f  
- Automatic Mass Rebuild

* Mon Apr 03 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.4-1-gitddae58f
- Updated to 0.1.4-1-20170403gitddae58f

* Sat Mar 18 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.3-1-git46c25dc
- Updated to 0.1.3-1-20170321git46c25dc

* Wed Aug 31 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 0.1.2-1
- Update to 0.1.2
- Change the source URL
- New dependencys: https://docs.google.com/document/d/1V6nq-IuS9zxqO1-OSt8iTS_cw_HMCpsUNofHLYtUNjM/pub#h.1mu1kucmg351 

* Thu Jun 30 2016 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1.1-3
- Massive rebuild F25

* Mon Apr 18 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-2
- Rename python-libopenshot to python3-libopenshot.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Tue Feb  9 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.0-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

* Wed Jun 24 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags,
  instead use "export CXXFLAGS" that was override all flags .

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4
- Fix FTBFS (rf#3624)

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.0.3-4
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-3
- Rebuilt for FFmpeg 2.4.x

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-2
- Rebuilt for FFmpeg 2.4.x

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
