%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: scapy
Version: 2.2.0
Release: 1%{?dist}
Summary: Interactive packet manipulation tool and network scanner

Group: Applications/Internet
License: GPLv2
URL: http://www.secdev.org/projects/scapy/
Source0: http://www.secdev.org/projects/scapy/files/scapy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python >= 2.5
BuildRequires: python-devel >= 2.5

Requires: python >= 2.5

%description
Scapy is a powerful interactive packet manipulation program built on top 
of the Python interpreter. It can be used to forge or decode packets of 
a wide number of protocols, send them over the wire, capture them, match 
requests and replies, and much more.

%prep
%setup -q -n scapy-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 doc/scapy.1.gz %{buildroot}%{_mandir}/man1/scapy.1.gz
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -f %{buildroot}%{python_sitelib}/*egg-info/requires.txt


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/UTscapy
%{python_sitelib}/scapy/*
%{python_sitelib}/scapy-*.egg-info

%changelog
* Sat Jul 22 2012 Thiébaud Weksteen <thiebaud@weksteen.fr> - 2.2.0-1
- Update to Scapy 2.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.10-1
- Update to Scapy 2.0.0.10.

* Sun Dec 07 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 2.0.0.9-2
- Update for Scapy 2.0.0.9.

* Tue Jan 22 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-4
- Switch to using rm macro.

* Mon Jan 21 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-2
- Spec file cleanup.

* Fri Jan 18 2008 Devan Goodwin <dgoodwin@dangerouslyinc.com> 1.1.1-1
- Initial packaging for Fedora.

