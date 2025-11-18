Name:           rxfish-theme
Version:        1.0
Release:        1%{?dist}
Summary:        fish theme for rxdots.
License:        GPL-3.0
URL:            https://github.com/rXelelo/fedora-dots
Source1:        fish-theme
ExclusiveArch:  x86_64

# Runtime dependencies
Requires:  fish
Requires:  starship

# Build dependencies
#BuildRequires:  tar

%description

%global debug_package %{nil}

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
#install -dm0755 %{buildroot}/etc/skel
#cp -a %{SOURCE1}/* %{buildroot}/etc/skel

%files

%changelog
* Mon Nov 17 2025 Rain Xelelo <rxelelo@outlook.com> - %{Version}-%{Release}
- Initial release