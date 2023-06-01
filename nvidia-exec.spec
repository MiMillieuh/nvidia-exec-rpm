Name:       nvidia-exec
Version:    0.1.1
Release:    0.1.1
Summary:    RPM port of pedro00dk s nvidia-exec for nvidia-gpus 
License:    GPL-3.0

%description
RPM port of pedro00dk s nvidia-exec for nvidia-gpus

%autosetup
  
%prep
# we have no source, so nothing here

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/modprobe.d/
install -m 755 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx %{buildroot}/usr/bin/nvx
install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx.service %{buildroot}/usr/lib/systemd/system/nvx.service
install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/modprobe.conf %{buildroot}/usr/lib/modprobe.d/nvx.conf
install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx-suspend-restore %{buildroot}/usr/lib/systemd/system-sleep

%files
/usr/bin/nvx
/usr/lib/systemd/system/nvx.service
/usr/lib/modprobe.d/nvx.conf
/usr/lib/systemd/system-sleep
  
%post
systemctl stop nvidia-persistenced.service
systemctl stop nvidia-powerd.service
systemctl disable nvidia-persistenced.service
systemctl disable nvidia-powerd.service
systemctl enable --now nvx.service


%preun
if [ $1 -eq 0 ]; then
  systemctl stop nvx.service
  systemctl disable nvx.service
  systemctl enable --now nvidia-persistenced.service
  systemctl enable --now nvidia-powerd.service
fi

%changelog
# let's skip this for now
