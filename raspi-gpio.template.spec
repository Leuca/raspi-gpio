Name:       {{{ git_dir_name }}}
Version:    {{{ git_dir_version }}}
Release:    %{?dist}
Summary:    Tool to help debug / hack at the BCM283x GPIO

BuildRequires:  automake gcc

License:    BSD-3
URL:        https://github.com/RPi-Distro/raspi-gpio
VCS:        {{{ git_dir_vcs }}}

Source:     {{{ git_dir_pack }}}

%description
Tool to help debug / hack at the BCM283x GPIO.
You can dump the state of a GPIO or (all GPIOs).
You can change a GPIO mode and pulls (and level if set as an output).
Beware this tool writes directly to the BCM283x GPIO registers, ignoring anything else that may be using them (like Linux drivers).

%prep
{{{ git_dir_setup_macro }}}

%build
./configure --prefix=%{buildroot}
make

%install
make install

%files
%license LICENSE
%{_bindir}/raspi-gpio

%changelog
{{{ git_dir_changelog }}}
