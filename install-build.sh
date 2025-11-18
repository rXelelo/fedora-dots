#!/bin/bash
sudo dnf install rpm-build rpmdevtools
rpmdev-setuptree
sudo dnf copr enable yalter/niri-git -y
sudo dnf copr enable zhangyi6324/noctalia-shell -y
sudo dnf copr enable che/nerd-fonts -y
ln -s ~/fedora-dots/rpmbuild ~/rpmbuild
rpm -ba ~/rpmbuild/SPECS/rxfish-theme.spec
rpm -ba ~/rpmbuild/SPECS/fedora-dots.spec
sudo dnf install ~/rpmbuild/RPMS/rxfish-theme-*.rpm ~/rpmbuild/RPMS/rxdots-*.rpm