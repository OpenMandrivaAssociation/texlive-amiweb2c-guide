Name:		texlive-amiweb2c-guide
Version:	56878
Release:	1
Summary:	How to install AmiWeb2c
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/amiweb2c-guide
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiweb2c-guide.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiweb2c-guide.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a guide for the installation of (La)TeX with the Amiga
port of Web2C named AmiWeb2C in the version 2.1 on an emulated
Amiga 4000 computer running Workbench 3.1. Furthermore the
installation of an ARexx server for calling LaTeX from an
editor is described and some tips for the installation of new
fonts are given.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/amiweb2c-guide

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
