Name:           fedora-dots
Version:        17.11.2025-12:03
Release:        1%{?dist}
Summary:        niri+noctalia-shell.
License:        GPL-3.0
URL:            https://github.com/rXelelo/fedora-dots
ExclusiveArch:  x86_64

# Runtime dependencies
Requires:  niri
Requires:  noctalia-shell
Requires:  google-noto-fonts-all
Requires:  kitty
Requires:  nautilus
Requires:  wlsunset

# Build dependencies
BuildRequires:  tar
BuildRequires: patchelf

%description

%global debug_package %{nil}
%prep
%setup -c -T


%build

%install
install -dm0755 %{buildroot}%{_bindir}
install -dm0755 %{buildroot}%{_datadir}/applications



%files
/opt/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Rain Xelelo <rxelelo@outlook.com>
- Initial package for Fedora