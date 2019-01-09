Name:		ssh-tools
Version:	1.5
Release:	1%{?dist}
Summary:	Collection of various tools using ssh

License:	GPLv3
URL:		https://github.com/vaporup/%{name}/
Source0:	https://github.com/vaporup/%{name}/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	help2man
Requires:	openssh-clients bash
Recommends:	colordiff

%description
* ssh-ping: check if host is reachable using ssh_config
* ssh-version: shows version of the SSH server you are connecting to
* ssh-diff: diff a file over SSH
* ssh-facts: get some facts about the remote system
* ssh-hostkeys: prints server host keys in several formats

%prep
%setup -q

%build
mkdir -p man

help2man -n "check if host is reachable using ssh_config"           -S SSH-TOOLS -N --version-string " " -o man/ssh-ping.1        ./ssh-ping
help2man -n "shows version of the SSH server you are connecting to" -S SSH-TOOLS -N --version-string " " -o man/ssh-version.1     ./ssh-version
help2man -n "diff a file over SSH"                                  -S SSH-TOOLS -N --version-string " " -o man/ssh-diff.1        ./ssh-diff
help2man -n "get some facts about the remote system"                -S SSH-TOOLS -N --version-string " " -o man/ssh-facts.1       ./ssh-facts
help2man -n "prints server host keys in several formats"            -S SSH-TOOLS -N --version-string " " -o man/ssh-hostkeys.1    ./ssh-hostkeys

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0755 ssh-* %{buildroot}/%{_bindir}/
install -m 0644 man/* %{buildroot}/%{_mandir}/man1/

%files
%license LICENSE
%{_bindir}/ssh-*
%{_mandir}/man1/ssh-*.1.gz

%changelog
* Wed Jan 09 2019 Sven Wick <sven.wick@gmx.de> 1.5-1
- Initial RPM release (#1662170)
