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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a guide for the installation of (La)TeX with the Amiga port of
Web2C named AmiWeb2C in the version 2.1 on an emulated Amiga 4000
computer running Workbench 3.1. Furthermore the installation of an ARexx
server for calling LaTeX from an editor is described and some tips for
the installation of new fonts are given.

