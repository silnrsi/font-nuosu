%define fontname @PACKAGE@
%define fontdir %{_datadir}/fonts/%{fontname}
%define fontconfdir %{_sysconfdir}/fonts/conf.d
%define archivename @RELEASE_DIR@

Name: %{fontname}-fonts
Version: %TTF_VERSION%
Release: @BUILD@
Summary: @DESC_SHORT@
Group: User Interface/X
License: @LICENSE@

Source0: %{archivename}.tar.gz

BuildRoot: %{mktemp -ud %{_tmppath}/%{name}-@VERSION@-%{release}}

BuildArch: noarch

%description
@DESC_LONG@

%prep

%setup -q -n ${archivename}

%build

%install
rm -fr ${buildroot}
install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

%clean
rm -fr %{buildroot}

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache -f %{fontdir} || ;
fi

%postun
if [ "$1" = "0" ]; then
    if [ -x %{_bindir}/fc-cache ]; then
        %{_bindir}/fc-cache -f %{fontdir} || ;
    fi
fi

%files
%defattr(0644,root,root,0755)

%doc *.txt
%dir %{fontdir}
%{fontdir}/*.ttf

%changelog



