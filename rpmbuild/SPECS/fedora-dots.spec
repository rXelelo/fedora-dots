Name:           rxdots
Version:        1.0
Release:        1%{?dist}
Summary:        niri+noctalia-shell.
License:        GPL-3.0
URL:            https://github.com/rXelelo/fedora-dots
Source1:        dots
ExclusiveArch:  x86_64

# Runtime dependencies
Requires:  niri
Requires:  noctalia-shell
Requires:  google-noto-fonts-all
Requires:  kitty
Requires:  nautilus
Requires:  wlsunset
Requires:  zen-browser
#Requires:  rxfish-theme
Requires:  neovim

# Build dependencies
#BuildRequires:  tar

%description

%global debug_package %{nil}

#%pre: Script runs just before the package is installed.
#%post: Script runs just after the package is installed.
#%preun: Script runs just before the package is uninstalled.
#%postun: Script runs just after the package is uninstalled. 
%post
#!/bin/bash
exec </dev/tty >/dev/tty 2>&1
users=$(awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd)
user_count=$(echo "$users" | wc -l)
# If only one user, use it automatically
if [ "$user_count" -eq 1 ]; then
    selected_user="$users"
    echo "Auto-selected user: $selected_user"
else
    # Multiple users - show selection menu
    echo "Available users:"
    select selected_user in $users; do
        if [ -n "$selected_user" ]; then
            break
        else
            echo "Invalid selection. Please try again."
        fi
    done
fi
echo "Selected user: $selected_user"

%prep

%setup -c -T


%build

%install
install -dm0755 %{buildroot}/etc/skel
cp -a %{SOURCE1}/* %{buildroot}/etc/skel

%files
/etc/skel

%changelog
* Mon Nov 17 2025 Rain Xelelo <rxelelo@outlook.com> - %{Version}-%{Release}
- Initial release