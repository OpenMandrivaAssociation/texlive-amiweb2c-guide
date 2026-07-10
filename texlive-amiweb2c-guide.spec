%global tl_name amiweb2c-guide
%global tl_revision 56878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	How to install AmiWeb2c
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/amiweb2c-guide
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amiweb2c-guide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amiweb2c-guide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a guide for the installation of (La)TeX with the Amiga port of
Web2C named AmiWeb2C in the version 2.1 on an emulated Amiga 4000
computer running Workbench 3.1. Furthermore the installation of an ARexx
server for calling LaTeX from an editor is described and some tips for
the installation of new fonts are given.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/amiweb2c-guide
%doc %{_datadir}/texmf-dist/doc/latex/amiweb2c-guide/README
%doc %{_datadir}/texmf-dist/doc/latex/amiweb2c-guide/amiweb2c-guide.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amiweb2c-guide/amiweb2c-guide.tex
