# Fedora Dots

> 🚀 Personal dotfiles for Fedora with Niri compositor and Noctalia shell

[![License](https://img.shields.io/github/license/rXelelo/fedora-dots)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/rXelelo/fedora-dots)](https://github.com/rXelelo/fedora-dots/stargazers)

Beautiful, minimalist Fedora setup featuring the modern Niri scrollable-tiling Wayland compositor paired with Noctalia shell for a unique desktop experience.

## 🎨 Features

- **Niri Compositor**: Modern scrollable-tiling Wayland compositor for a fluid workflow
- **Noctalia Shell**: Beautiful and efficient shell environment
- **RPM Packages**: Pre-built packages available via GitHub releases
- **Automated Installation**: Easy setup with install scripts
- **Fedora-optimized**: Designed specifically for Fedora workstations

## 📦 Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/rXelelo/fedora-dots.git
cd fedora-dots

# Run the installation script
./install.sh
```

### Install Manualy 

```bash
# Enable copr 
sudo dnf copr enable yalter/niri-git 
sudo dnf copr enable zhangyi6324/noctalia-shell 

#Install
latest_tag=$(git describe --tags --abbrev=0)
sudo dnf install https://github.com/rXelelo/fedora-dots/releases/download/$latest_tag/rxdots-stable-1.fc42.x86_64.rpm https://github.com/rXelelo/fedora-dots/releases/download/$latest_tag/rxfish-theme-stable-1.fc42.x86_64.rpm
```

## 🔧 Requirements

- **OS**: Fedora (Latest release recommended) or any other if you fix deps on your system
- **Display**: Wayland support required
- **GPU**: Any GPU with working Wayland drivers

## 📁 Repository Structure

```
fedora-dots/
├── rpmbuild/           # RPM spec files and sources
│   ├── SPECS/          # RPM spec files
│   └── SOURCES/        # Source tarballs
├── configs/            # Configuration files
│   ├── niri/           # Niri compositor config
│   └── noctalia/       # Noctalia shell config
└── install.sh          # Main installation script
```

## 🚀 Usage

### Starting Niri

After installation, you can start Niri from your display manager (GDM, SDDM) by selecting "Niri" from the session list.

Or manually from TTY:

```bash
niri-session
```

### Key Bindings

Default key bindings (customizable in config):

| Keybinding | Action |
|------------|--------|
| `Super + Shift + /` | Show Important Hotkeys |
| `Super + Shift + E` | Exit Niri |
| `Super + Q` | Close Focused Window |
| `Super + Left` | Focus Column to the Left |
| `Super + Right` | Focus Column to the Right |
| `Super + Ctrl + Left` | Move Column Left |
| `Super + Ctrl + Right` | Move Column Right |
| `Super + Page Down` | Switch Workspace Down |
| `Super + Page Up` | Switch Workspace Up |
| `Super + Ctrl + Page Down` | Move Column to Workspace Down |
| `Super + Ctrl + Page Up` | Move Column to Workspace Up |
| `Super + R` | Switch Preset Column Widths |
| `Super + F` | Maximize Column |
| `Super + [` | Consume or Expel Window Left |
| `Super + ]` | Consume or Expel Window Right |
| `Super + Space` | Move Window Between Floating and Tiling |
| `Super + Shift + Space` | Switch Focus Between Floating and Tiling |
| `Super + S` | Open the Overview |
| `PrtSc` | Take a Screenshot |
| `Super + E` | Open a File Explorer |
| `Super + T` | Open a Terminal |
| `Super + D` | Run an Application Menu |
| `Super + L` | Lock the Screen |
| `Super + Alt + L` | Lock the Screen and Suspend |
| `Super + V` | Clipboard History |
| `Super + C` | Calculator |
| `Super + J` | Toggle Bar Visibility |
| `Super + Ctrl + W` | Wallpaper Toggle Selector |
| `Super + I` | Settings |
## 🛠️ Configuration

Configuration files are located in:
- Niri: `~/.config/niri/config.kdl`
- Noctalia: `~/.config/noctalia/`

Edit these files to customize your setup.

## 🔄 Updating

### From Git

```bash
cd fedora-dots
git pull
./install.sh
```

### From RPM

Download the latest release and reinstall:

```bash
sudo dnf reinstall ./*.rpm
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Building from Source

To build the RPM packages yourself:

```bash
# Install build dependencies
sudo dnf install -y rpm-build rpmdevtools

# Build all packages
cd fedora-dots
cp -a rpmbuild ~/
cd ~/rpmbuild
for spec in SPECS/*.spec; do
    rpmbuild -ba "$spec"
done

# Find built packages
find ~/rpmbuild/RPMS -name "*.rpm"
```

## 🐛 Troubleshooting

### Niri won't start

1. Check Wayland support: `echo $XDG_SESSION_TYPE`
2. Verify GPU drivers are installed
3. Check logs: `journalctl -u display-manager`

### Missing dependencies

If you encounter missing dependencies, install them manually:

```bash
#find on pkgs.org
sudo dnf install <package-name>
```

## 📸 Screenshots

*Add your screenshots here to showcase your setup*

## 📄 License

This project is licensed under the [LICENSE] - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Niri](https://github.com/YaLTeR/niri) - The amazing scrollable-tiling Wayland compositor
- Noctalia Shell - Beautiful shell environment
- Fedora Project - For the excellent Linux distribution

## 📞 Contact

- GitHub: [@rXelelo](https://github.com/rXelelo)
- Issues: [GitHub Issues](https://github.com/rXelelo/fedora-dots/issues)

---

⭐ Star this repo if you find it helpful!