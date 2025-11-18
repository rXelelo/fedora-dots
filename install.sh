#!/bin/bash
sudo dnf copr enable yalter/niri-git -y
sudo dnf copr enable zhangyi6324/noctalia-shell -y
sudo dnf copr enable che/nerd-fonts -y
latest_tag=$(git describe --tags --abbrev=0)
sudo dnf install https://github.com/rXelelo/fedora-dots/releases/download/$latest_tag/rxdots-stable-1.fc42.x86_64.rpm https://github.com/rXelelo/fedora-dots/releases/download/$latest_tag/rxfish-theme-stable-1.fc42.x86_64.rpm
