#
# spec file for package libopenshot
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

# 
%define _legacy_common_support 1

%global commit0 517f2896d1e12c313f5a5f62f0945648352eb533
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           libopenshot
Version:        0.2.5
Release:        9%{?gver}%{?dist}
Summary:        Library for creating and editing videos

License:        LGPLv3+
URL:            http://www.openshot.org/
Source0:	https://github.com/OpenShot/libopenshot/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake swig
BuildRequires:	make
%if 0%{?fedora} >= 33
BuildRequires:  python3.9-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  ImageMagick-c++-devel
BuildRequires:	ImageMagick-devel
BuildRequires:  ffmpeg-devel >= 4.3
BuildRequires:  libopenshot-audio-devel >= 0.2.0
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
%cmake -DMAGICKCORE_HDRI_ENABLE=1 -DMAGICKCORE_QUANTUM_DEPTH=16 -DFFMPEG_INCLUDE_DIR=/usr/include/ffmpeg .

pushd %{_target_platform}
%make_build V=0


%install
pushd %{_target_platform}
%make_install V=0


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files -n python3-libopenshot
%{python3_sitearch}/*


%changelog

* Tue Jun 23 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.5-9.git517f289
- Rebuilt for ffmpeg

* Sun May 31 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.5-8.git782d764
- Updated to current commit
- Rebuilt for python3.9

* Wed Mar 11 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.5-7.gitd0e884df
- Updated to 0.2.5-7.gitd0e884df

* Mon Feb 10 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.4-7.git63e28a0
- Updated to 0.2.4-7.git63e28a0

* Tue Dec 03 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.3-11.gitc04dc94
- Updated to current commit

* Wed Nov 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.3-10.gitc271352
- Updated to current commit because our openshot use a devel version thanks to Blender 2.80

* Wed Sep 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.3-8.git101f25a
- Python3 fix for F32

* Wed Apr 10 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.3-7.git101f25a
- Updated to 0.2.3

* Thu Dec 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.2-8.gitc90fb9b
- Rebuilt for ffmpeg

* Sat Sep 22 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.2-7.gitc90fb9b
- Updated to 0.2.2-7.gitc90fb9b

* Thu Sep 20 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.1-7.git6c4c9cc 
- Updated to 0.2.1-7.git6c4c9cc

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.0-8.git9972600  
- Rebuilt for Python 3.7

* Sat Jun 30 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.2.0-7.git9972600  
- Updated to 0.2.0-7.git9972600

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.9-8.git  
- Automatic Mass Rebuild

* Mon Apr 23 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.9-7.git7fc657c
- Updated to 0.1.9-7.git7fc657c
- Fix for ffmpeg 4.x

* Thu Nov 16 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.9-1.git67d355d
- Updated to 0.1.9-1.git67d355d

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
