Name:           vim
Version:        9.1.0660
Release:        1%{?dist}
Summary:        Visual editor improved
License:        Vim and MIT

%global         version2    91

Source:         https://github.com/vim/vim/archive/v%{version}/vim-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
VIM (VIsual editor iMproved) is an updated and improved version of the vi
editor. Vi was the first real screen-based editor for UNIX, and is still very
popular. VIM improves on vi by adding new features: multiple windows,
multi-level undo, block highlighting and more. The vim-minimal package includes
a minimal version of VIM, which is installed into /bin/vi for use when only the
root partition is present. NOTE: The online help is only available when the
vim-common package is installed.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h

# Remove reference to csh for now
rm runtime/tools/vim132

./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

ln -sv vim %{buildroot}/usr/bin/vi
for L in  %{buildroot}/usr/share/man/{,*/}man1/vim.1; do
    ln -sv vim.1 $(dirname $L)/vi.1
done

mkdir %{buildroot}/etc
cat > %{buildroot}/etc/vimrc << "EOF"
" Begin /etc/vimrc

" Ensure defaults are set before customizing settings, not after
source $VIMRUNTIME/defaults.vim
let skip_defaults_vim=1

set nocompatible
set backspace=2
set mouse=
syntax on
if (&term == "xterm") || (&term == "putty")
  set background=dark
endif

" End /etc/vimrc
EOF

#---------------------------------------------------------------------------
%files
%config(noreplace) /etc/vimrc
/usr/bin/ex
/usr/bin/rview
/usr/bin/rvim
/usr/bin/vi
/usr/bin/view
/usr/bin/vim
/usr/bin/vimdiff
/usr/bin/vimtutor
/usr/bin/xxd
/usr/share/applications/*.desktop
/usr/share/icons/hicolor/48x48/apps/gvim.png
/usr/share/icons/locolor/16x16/apps/gvim.png
/usr/share/icons/locolor/32x32/apps/gvim.png
/usr/share/vim/vim%{version2}

%files doc
/usr/share/man/*.ISO8859-{1,2,9}/man*/*
/usr/share/man/*.UTF-8/man*/*
/usr/share/man/??/man*/*
/usr/share/man/ru.KOI8-R/man*/*
/usr/share/man/man*/*
