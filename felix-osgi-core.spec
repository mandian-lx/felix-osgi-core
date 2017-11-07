%{?_javapackages_macros:%_javapackages_macros}

%global bundle org.osgi.core

Name:           felix-osgi-core
Version:        1.4.0
Release:        22.1
Summary:        Felix OSGi R4 Core Bundle
License:        ASL 2.0
Group:          Development/Java
URL:            http://felix.apache.org/site/apache-felix-osgi-core.html
BuildArch:      noarch

Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
export LC_ALL=en_US.UTF-8
%mvn_build -- -Drat.numUnapprovedLicenses=50

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 16 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-20
- Regenerate build-requires
- Update to current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-16
- Remove BuildRequires on maven-surefire-provider-junit4

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-15
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Mat Booth <fedora@matbooth.co.uk> - 1.4.0-14
- Update for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-12
- Add missing BR: maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Jaromir Capik <jcapik@redhat.com> 1.4.0-8
- Extra groupId "org.osgi" added
- Minor spec file changes according to the latest guidelines
- fixing "unmappable character for encoding ANSI_X3.4-1968"

* Wed Mar 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-7
- Build with maven 3 and drop ant buil.xml files.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-5
- Remove felix-parent from Requires to prevent pulling maven in

* Tue Dec 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4.0-4
- Add felix-parent to Requires (maven builds require this)
- Add license and jpackage-utils Requires to javadoc subpackage
- Use mavenpomdir macro

* Mon Dec 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.4.0-3
- Fix pom name.
- Adapt to current guidelines.

* Tue Jun 29 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-2
- Modify maven-build.xml to include MANIFEST.MF into JAR

* Tue Jun 22 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.4.0-1
- Update felix-osgi-core-1.4.0-build.xml.tar.gz
- Use the macros style
- Release 1.4.0

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-2
- Fix line length.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Initial package.
