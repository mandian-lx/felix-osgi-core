%global bundle org.osgi.core

Name:    felix-osgi-core
Version: 1.4.0
Release: 8
Summary: Felix OSGi R4 Core Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org/site/apache-felix-osgi-core.html
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1: %{name}-%{version}-build.xml.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 0:1.6.0
BuildRequires: ant
BuildRequires: jpackage-utils

Requires: java >= 0:1.6.0

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

tar xf %{SOURCE1}

%__mkdir_p .m2/repository

%build
%ant -Dmaven.settings.offline=true \
     -Dmaven.repo.local=.m2/repository \
     package javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/felix/%{bundle}.jar

%add_to_maven_depmap org.apache.felix %{bundle} %{version} JPP/felix %{bundle}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
%{buildroot}%{_mavenpomdir}/JPP.felix-%{bundle}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_javadir}/felix
%{_mavenpomdir}/JPP.felix-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%defattr(-,root,root,-)
%doc LICENSE
%{_javadocdir}/%{name}

