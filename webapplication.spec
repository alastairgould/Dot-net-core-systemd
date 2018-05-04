%global _opt /opt
%global debug_package %{nil} 
%global _build_id_links none

Name:          dotnet-core-systemd 
Version:       0.1
Release:       1%{?dist}
Summary:       An Example Web Application
Group:         Web Application

URL:           https://github.com/alastairgould/dotnet-core-systemd 
License:       MIT
Source0:       https://github.com/alastairgould/dotnet-core-systemd/archive/0.1.tar.gz 
Source1:       webapplication.service 
Source2:       webapplication-firewall.xml 
#BuildRequires: rh-dotnet20
%{?systemd_requires}
BuildRequires: systemd
# Requires: somepackage >= 0.5.0 - How to do dependencies
Requires: firewalld-filesystem
Requires(post): firewalld-filesystem
Requires(postun): firewalld-filesystem
Autoreq: 0

%description
An example webapplication to show how you can package applications as an RPM

%prep
%setup 

%build
dotnet publish WebApplication/WebApplication.csproj -c Release

%install
mkdir -p %{buildroot}/%{_opt}/%{name}
cp -a WebApplication/bin/Release/netcoreapp2.0/rhel.7.4-x64/publish/. %{buildroot}/%{_opt}/%{name}/

chmod 755 %{buildroot}/%{_opt}/%{name}

mkdir -p % %{buildroot}/%{_unitdir}
cp %{SOURCE1} %{buildroot}/%{_unitdir}

mkdir -p % %{buildroot}/%{_prefix}/lib/firewalld/services/
cp %{SOURCE2} %{buildroot}/%{_prefix}/lib/firewalld/services/

%files
/%{_opt}/%{name}/
/%{_unitdir}
/%{_prefix}/lib/firewalld/services/

%post
%firewalld_reload
systemctl enable webapplication.service
systemctl start webapplication.service
firewall-cmd --zone=public --permanent --add-service=webapplication-firewall
%firewalld_reload

%preun
%systemd_preun webapplication.service

%postun
firewall-cmd --zone=public --permanent --remove-service=webapplication-firewall
%firewalld_reload
%systemd_postun_with_restart webapplication.service
