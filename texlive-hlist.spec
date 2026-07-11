%global tl_name hlist
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11
Release:	%{tl_revision}.1
Summary:	Horizontal and columned lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/hlist
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hlist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hlist.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This plain TeX and LaTeX package provides the "hlist" environment in
which \hitem starts a horizontal and columned item. It depends upon the
simplekv package.

