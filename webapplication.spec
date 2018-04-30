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
# BuildRequires: rh-dotnet20
# Requires: somepackage >= 0.5.0 - How to do dependencies
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
mkdir -p % %{buildroot}/usr/lib/systemd/system/
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/

%files
/%{_opt}/%{name}/
/usr/lib/systemd/system/
