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
mkdir -p %{buildroot}/usr/lib/systemd/system-preset/
install -m 755 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx %{buildroot}/usr/bin/nvx
install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx.service %{buildroot}/usr/lib/systemd/system/nvx.service
install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/modprobe.conf %{buildroot}/usr/lib/modprobe.d/nvx.conf
install -m 664 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvidiaexec.preset %{buildroot}/usr/lib/systemd/system-preset/99-nvidia-exec.preset
#install -m 644 /home/runner/work/nvidia-exec-rpm/nvidia-exec-rpm/nvx-suspend-restore %{buildroot}/usr/lib/systemd/system-sleep

%files
/usr/bin/nvx
/usr/lib/systemd/system/nvx.service
/usr/lib/modprobe.d/nvx.conf
/usr/lib/systemd/system-preset/99-nvidia-exec.preset 
#/usr/lib/systemd/system-sleep
  
%post
/usr/bin/systemctl stop nvidia-persistenced.service
/usr/bin/systemctl stop nvidia-powerd.service
/usr/bin/systemctl disable nvidia-persistenced.service
/usr/bin/systemctl disable nvidia-powerd.service
/usr/bin/systemctl enable --now nvx.service


%preun
if [ $1 -eq 0 ]; then
  /usr/bin/systemctl stop nvx.service
  /usr/bin/systemctl disable nvx.service
  /usr/bin/systemctl enable --now nvidia-persistenced.service
  /usr/bin/systemctl enable --now nvidia-powerd.service
fi

%changelog
# let's skip this for now
