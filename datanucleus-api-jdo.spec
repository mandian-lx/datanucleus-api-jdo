%{?_javapackages_macros:%_javapackages_macros}

%global commit 3c0a06622831bd7af6c231c1b5d5398f3afc7271
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:          datanucleus-api-jdo
Version:       3.2.8
Release:       4
Summary:       DataNucleus JDO API plugin
License:       ASL 2.0
URL:           https://github.com/datanucleus/datanucleus-api-jdo
Source:        https://github.com/datanucleus/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires: java-devel

# note this HAS to be jdo-api 3.x, not jdo2-api 2.2
BuildRequires: mvn(javax.jdo:jdo-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(org.datanucleus:datanucleus-core)
# Test deps
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j)

BuildRequires: maven-local
BuildRequires: datanucleus-maven-parent

BuildArch:     noarch

%description
Plugin providing DataNucleus implementation of JDO API.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{commit}

sed -i 's/\r//' META-INF/LICENSE.txt META-INF/NOTICE.txt META-INF/README.txt
cp -p META-INF/LICENSE.txt .
cp -p META-INF/NOTICE.txt .
cp -p META-INF/README.txt .

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 19 2014 Peter MacKinnon <pmackinn@redhat.com> - 3.2.8-1
- updated to 3.2.8
- added datanucleus-maven-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Peter MacKinnon <pmackinn@redhat.com> - 3.2.6-4
- removed wagon-ssh-external extension

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.2.6-3
- Use Requires: java-headless rebuild (#1067528)

* Mon Dec 16 2013 Peter MacKinnon <pmackinn@redhat.com> 3.2.6-2
- injected missing ASL2 license text in DTD

* Tue Dec 10 2013 Peter MacKinnon <pmackinn@redhat.com> 3.2.6-1
- updated to version 3.2.6

* Fri Sep 20 2013 gil cattaneo <puntogil@libero.it> 3.2.4-1
- initial rpm
